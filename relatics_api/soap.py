from suds.client import Client

from relatics_api.utils import *

WSDL_URL = ("https://", ".relaticsonline.com/api/relaticsapi.asmx?WSDL", ".relaticsonline.com/DataExchange.asmx?wsdl",
            ".relaticsonline.com/api/relaticsapi.asmx?op=", ".relaticsonline.com/DataExchange.asmx?op=GetResult")


class RelaticsAPI:
	"""
	This class creates an object that simulates the Relatics API)
	"""

	def __init__(self, company_name: str, environment_id: str, workspace_id: str):
		self.token = None
		self.url = WSDL_URL[0] + company_name + WSDL_URL[1]
		self.client = Client(self.url)
		self.company_name = company_name
		self.environment_id = environment_id
		self.workspace_id = workspace_id

	def __repr__(self):
		return 'You called a RelaticsApi Object'

	def __getattr__(self, item):
		self.method = item
		return self.invoke_method

	def login(self, username: str, password: str, retxml: bool = False) -> str:
		client = Client(self.url, retxml=retxml)
		url_method = WSDL_URL[0] + self.company_name + WSDL_URL[3] + 'Login'
		xml_definition = get_xml_for_method(url_method)
		xml = str.encode(xml_definition.format(username, password))
		response_login = client.service.Login(__inject={'msg': xml})
		self.token = response_login
		return self.token

	def invoke_method(self, data):

		url_method = WSDL_URL[0] + self.company_name + WSDL_URL[3] + self.method

		if self.token is not None:
			xml_definition = get_xml_for_method(url_method)
			if isinstance(data, tuple):
				xml = str.encode(
					xml_definition.format(self.token, self.environment_id, self.workspace_id, *data)
				)
			else:
				xml = str.encode(
					xml_definition.format(self.token, self.environment_id, self.workspace_id, data)
				)
		else:
			raise RelaticsException('Please login first by calling ().login(username,password)')

		method_to_call = getattr(self.client.service, self.method)
		response = method_to_call(__inject={'msg': xml})
		return response

	def read_data(self, operation_name: str, entry_code: str, parameters: str = 'None', retxml: bool = False) -> str:
		"""
		retrieving data from Relatics

		:param str operation_name: The operation name of the webservice
		:param str entry_code: The entry-code of the webservice
		:param tuple parameters: provide a list of tuples if there are more parameters
		:param str retxml: If True return xml, otherwise return Object. default: false

		:return: soap data object
		"""

		method_url = WSDL_URL[0] + self.company_name + WSDL_URL[2]
		# TODO print the exact data url.
		url__method = WSDL_URL[0] + self.company_name + WSDL_URL[4]
		xml_definition = get_xml_for_method(url__method)
		print(xml_definition)
		client = Client(method_url, retxml=retxml)

		if validate_url(method_url):
			# Sending read xml and encode byte to string
			xml_filled_in = xml_definition.format(operation_name,

			                                      '<Identification><Workspace>' + self.workspace_id + '</Workspace></Identification>',

			                                      '<Parameters>' + create_parameter_xml(parameters) + '</Parameters>',

			                                      '<Authentication><Entrycode>' + entry_code + '</Entrycode></Authentication>')

			xml = str.encode(xml_filled_in)

			# Create a Client object & get response
			response = client.service.GetResult(__inject={'msg': xml})
			return response

# def import_data(company_name: str, workspace: str, operation: str, entry_code: str, data) -> str:
# 	"""
# 	import data into Relatics; create and update data
#
# 	:param str company_name: The company_name
# 	:param str operation: The operation name of the webservice
# 	:param str workspace: The workspace ID
# 	:param str entry_code: The entry-code of the webservice
# 	:param dict data: dictionary of imported data
# 	:return: soap data object imported data
# 	"""
#
# 	# WSDL environment url
# 	url = WSDL_URL[0] + company_name + WSDL_URL[2]
# 	validate_url(url)
#
# 	# Data to send to the server
#
# 	if type(data) == dict:
#
# 		string_data = convert_dict_to_string(data)
#
# 		# Encode byte to string
# 		xml = str.encode(
# 			import_xml.format(Operation=operation, Workspace=workspace, Entrycode=entry_code,
# 			                  Data=encode_data(string_data)))
#
# 		# Create a Client object
# 		client = Client(url)
#
# 		# Get response
# 		response = client.service.Import(__inject={'msg': xml})
#
# 		return response
#
# 	else:
# 		return "data must be a dictionary"

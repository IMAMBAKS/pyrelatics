from suds.client import Client

from relatics_api.xml_strings import retrieve_xml, import_xml, retrieve_token
from relatics_api.utils import *

WSDL_URL = ("https://", ".relaticsonline.com/api/relaticsapi.asmx?WSDL", ".relaticsonline.com/DataExchange.asmx?wsdl",
            ".relaticsonline.com/api/relaticsapi.asmx?op=")


def import_data(company_name: str, workspace: str, operation: str, entry_code: str, data) -> str:
	"""
	import data into Relatics; create and update data

	:param str company_name: The company_name
	:param str operation: The operation name of the webservice
	:param str workspace: The workspace ID
	:param str entry_code: The entry-code of the webservice
	:param dict data: dictionary of imported data
	:return: soap data object imported data
	"""

	# WSDL environment url
	url = WSDL_URL[0] + company_name + WSDL_URL[2]
	validate_url(url)

	# Data to send to the server

	if type(data) == dict:

		string_data = convert_dict_to_string(data)

		# Encode byte to string
		xml = str.encode(
			import_xml.format(Operation=operation, Workspace=workspace, Entrycode=entry_code,
			                  Data=encode_data(string_data)))

		# Create a Client object
		client = Client(url)

		# Get response
		response = client.service.Import(__inject={'msg': xml})

		return response

	else:
		return "data must be a dictionary"


class RelaticsAPI:
	"""
	This class creates an object that simulates the Relatics API)
	"""

	def __init__(self, company_name: str, environment_id: str,
	             workspace_id: str):
		self.url = WSDL_URL[0] + company_name + WSDL_URL[1]
		self.client = Client(self.url)
		self.company_name = company_name
		self.environment_id = environment_id
		self.workspace_id = workspace_id

	def login(self, username: str, password: str) -> str:
		client = Client(self.url)
		xml = str.encode(retrieve_token.format(Username=username, Password=password))
		response_login = client.service.Login(__inject={'msg': xml})
		self.token = response_login
		return response_login

	def __repr__(self):
		return 'You called a RelaticsApi Object; username: {} \n company_name: {}'.format(self.__username,
		                                                                                  self.company_name)

	def __getattr__(self, item):
		self.method = item
		return self.invoke_method

	def invoke_method(self, data):
		self.url_api = WSDL_URL[0] + self.company_name + WSDL_URL[3] + self.method
		xml_definition = get_xml_for_method(self.url_api)
		if self.token is not None:
			if isinstance(data, tuple):
				self.xml = str.encode(
					xml_definition.format(self.token, self.environment_id, self.workspace_id, *data)
				)
			else:
				self.xml = str.encode(
					xml_definition.format(self.token, self.environment_id, self.workspace_id, data)
				)
		else:
			raise RelaticsException('Please login first by calling ().login')

		method_to_call = getattr(self.client.service, self.method)
		self.response = method_to_call(__inject={'msg': self.xml})
		return self.response

	# TODO will be deprecated because
	def read_data(self, operation_name: str, entry_code: str, retxml: bool = True) -> str:
		"""
		retrieving data from Relatics

		:param str company_name: The company_name
		:param str operation: The operation name of the webservice
		:param str workspace: The workspace ID
		:param str entry_code: The entry-code of the webservice
		:return: soap data object
		"""

		if validate_url(self.url):
			# Sending read xml and encode byte to string
			xml = str.encode(
				retrieve_xml.format(Operation=operation_name, Workspace=self.workspace_id, Entrycode=entry_code))
			# Create a Client object & get response
			response = self.client.service.GetResult(__inject={'msg': xml})
			return response

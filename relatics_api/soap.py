from suds.client import Client

from relatics_api.utils import *

WSDL_URLS = ("https://", ".relaticsonline.com/api/relaticsapi.asmx?WSDL", ".relaticsonline.com/DataExchange.asmx?wsdl",
             ".relaticsonline.com/api/relaticsapi.asmx?op=", ".relaticsonline.com/DataExchange.asmx?op=GetResult",
             ".relaticsonline.com/DataExchange.asmx?op=Import")


class RelaticsAPI:
    """
    This class creates an object that simulates the Relatics API
    """

    def __init__(self, company_name: str, environment_id: str, workspace_id: str):
        self.token = None
        self.url = WSDL_URLS[0] + company_name + WSDL_URLS[1]
        self.client = Client(self.url)
        self.company_name = company_name
        self.environment_id = environment_id
        self.workspace_id = workspace_id

    def __repr__(self):
        return 'This Object has the following parameters: ' \
               'Company name: {}' \
               'Environment ID: {}' \
               'Workspace ID: {}' \
               'Token: {}'.format(self.company_name, self.environment_id, self.workspace_id, self.token)

    def __getattr__(self, item):
        self.method = item
        return self.invoke_method

    def login(self, username: str, password: str, retxml: bool = False) -> str:
        client = Client(self.url, retxml=retxml)
        url_method = WSDL_URLS[0] + self.company_name + WSDL_URLS[3] + 'Login'
        xml_definition = get_xml_for_method(url_method)
        xml = str.encode(xml_definition.format(username, password))
        response_login = client.service.Login(__inject={'msg': xml})
        self.token = response_login
        return self.token

    def invoke_method(self, data):

        url_method = WSDL_URLS[0] + self.company_name + WSDL_URLS[3] + self.method

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

    def GetResult(self, operation_name: str, entry_code: str, parameters: TYPINGS_ROW = 'None',
                  retxml: bool = False) -> object:
        """
        retrieving data from Relatics

        :param str operation_name: The operation name of the webservice
        :param str entry_code: The entry-code of the webservice
        :param tuple parameters: provide a list of tuples if there are more parameters
        :param str retxml: If True return xml, otherwise return Object. default: false

        :return: soap data object
        """

        method_url_SOAP = WSDL_URLS[0] + self.company_name + WSDL_URLS[2]
        method_url_API = WSDL_URLS[0] + self.company_name + WSDL_URLS[4]
        xml_definition = get_xml_for_method(method_url_API)
        client = Client(method_url_SOAP, retxml=retxml)

        if validate_url(method_url_SOAP):
            # Sending read xml and encode byte to string
            xml_filled_in = xml_definition.format(operation_name,
                                                  '<Identification><Workspace>' + self.workspace_id + '</Workspace></Identification>',
                                                  '<Parameters>' + create_parameter_xml(parameters) + '</Parameters>',
                                                  '<Authentication><Entrycode>' + entry_code + '</Entrycode></Authentication>')

            xml = str.encode(xml_filled_in)
            # Create a Client object & get response
            response = client.service.GetResult(__inject={'msg': xml})
            return response

    def Import(self, operation_name: str, entry_code: str, data: TYPINGS_ROW, retxml=False) -> object:
        """
        import data into Relatics; create and update data

        :param str operation_name: The operation name of the webservice
        :param str entry_code: The entry-code of the webservice
        :param dict data: dictionary of imported data
        :return: soap data object imported data
        """

        # WSDL URLS
        method_url_SOAP = WSDL_URLS[0] + self.company_name + WSDL_URLS[2]
        method_url_API = WSDL_URLS[0] + self.company_name + WSDL_URLS[5]

        # Get xml definition for specific method
        xml_definition = get_xml_for_method(method_url_API)
        client = Client(method_url_SOAP, retxml=retxml)

        if validate_url(method_url_SOAP):
            # Sending read xml and encode byte to string
            xml_filled_in = xml_definition.format(operation_name,
                                                  '<Identification><Workspace>' + self.workspace_id + '</Workspace></Identification>',
                                                  '<Authentication><Entrycode>' + entry_code + '</Entrycode></Authentication>',
                                                  'import_data.xml',
                                                  encode_data(create_row_xml(data)))
            xml = str.encode(xml_filled_in)
            response = client.service.Import(__inject={'msg': xml})
            return response

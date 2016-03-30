from suds.client import Client

from .xml_strings import retrieve_xml, import_xml, retrieve_token, remove_xml
from .utils import *

WSDL_URL = ("https://", ".relaticsonline.com/api/relaticsapi.asmx?WSDL", ".relaticsonline.com/DataExchange.asmx?wsdl",
            ".relaticsonline.com/api/relaticsapi.asmx?op=")


def read_data(company: str, workspace: str, operation: str, entry_code: str) -> str:
    """
    retrieving data from Relatics

    :param str company: The company name
    :param str operation: The operation name of the webservice
    :param str workspace: The workspace ID
    :param str entry_code: The entry-code of the webservice
    :return: soap data object
    """

    # WSDL environment url
    url = WSDL_URL[0] + company + WSDL_URL[2]
    if validate_url(url):
        # Sending read xml and encode byte to string
        xml = str.encode(retrieve_xml.format(Operation=operation, Workspace=workspace, Entrycode=entry_code))

        # Create a Client object & get response
        client = Client(url, retxml=True)
        response = client.service.GetResult(__inject={'msg': xml})

        return response


def send_data(company: str, workspace: str, operation: str, entry_code: str, data) -> str:
    """
    import data into Relatics; create and update data

    :param str company: The company name
    :param str operation: The operation name of the webservice
    :param str workspace: The workspace ID
    :param str entry_code: The entry-code of the webservice
    :param dict data: dictionary of imported data
    :return: soap data object imported data
    """

    # WSDL environment url
    url = WSDL_URL[0] + company + WSDL_URL[2]
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


def login_to_relatics(url: str, username: str, password: str) -> str:
    client = Client(url, retxml=True)
    xml = str.encode(retrieve_token.format(Username=username, Password=password))
    response_login = client.service.Login(__inject={'msg': xml})
    return response_login


def delete_data(username: str, password: str, company: str, environmentid: str, workspaceid: str, data_list: list):
    """
    :param str username: login username Relatics
    :param str password: password username Relatics
    :param str company: company name
    :param str environmentid: environment ID
    :param str workspaceid:  workspace ID
    :param list data_list: list of data
    :param str type_of_data: property, relation or element
    :return: deleted object from Relatics
    """

    # WSDL environment url
    url = WSDL_URL[0] + company + WSDL_URL[1]
    validate_url(url)

    client = Client(url, retxml=True)

    token = login_to_relatics(url, username, password)

    for element in data_list:
        xml = str.encode(
            remove_xml.format(Token=token, EnvironmentID=environmentid, WorkspaceID=workspaceid,
                              InstanceElement=element))
        response = client.service.DeleteInstanceElement(__inject={'msg': xml})
        print(response)


def invoke_relatics_api_method_alpha(username: str, password: str, company: str, environmentid: str, workspaceid: str,
                                     data_list: list, method: str, *args):
    """
      :param str username: login username Relatics
      :param str password: password username Relatics
      :param str company: company name
      :param str environmentid: environment ID
      :param str workspaceid:  workspace ID
      :param list data_list: list of data
      :param str method: method name e.g. CreateInstanceElement
      :param *args *args: arguments for specific method data
      :return: object from Relatics
      """

    # API method environment url
    url_api = WSDL_URL[0] + company + WSDL_URL[2] + method
    validate_url(url_api)

    # WSDL environment url
    url = WSDL_URL[0] + company + WSDL_URL[1]
    client = Client(url, retxml=True)
    token = login_to_relatics(url, username, password)
    validate_url(url)

    # Retrieve XML method definition
    xml_definition = get_xml_for_method(url_api)

    for element in data_list:
        xml = str.encode(
            xml_definition.format(token, environmentid, workspaceid, *args))
        method_to_call = getattr(client.service, method)
        response = method_to_call(__inject={'msg': xml})
        print(response)

from suds.client import Client
from .xml_strings import retrieve_xml, import_xml, retrieve_token, remove_xml
from .utils import validate_url, encode_data, convert_dict_to_string

WSDL_URL = ("https://", ".relaticsonline.com/api/relaticsapi.asmx?WSDL", ".relaticsonline.com/DataExchange.asmx?wsdl",)


def read_data(company, workspace, operation, entry_code):
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
        client = Client(url)
        response = client.service.GetResult(__inject={'msg': xml})

        return response


def send_data(company, workspace, operation, entry_code, data):
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


def login_to_relatics(url, username, password):
    client = Client(url)
    xml = str.encode(retrieve_token.format(Username=username, Password=password))
    response_login = client.service.Login(__inject={'msg': xml})
    return response_login


def delete_data(username, password, company, environmentid, workspaceid, instanceid):
    """
    :param str username: login username Relatics
    :param str password: password username Relatics
    :param str environmentid: environment ID
    :param str workspaceid:  workspace ID
    :param str instanceid: id of object which should be deleted
    :return: deleted object from Relatics
    """

    # WSDL environment url
    url = WSDL_URL[0] + company + WSDL_URL[1]
    validate_url(url)

    client = Client(url)

    token = login_to_relatics(url, username, password)
    xml = str.encode(
        remove_xml.format(Token=token, EnvironmentID=environmentid, WorkspaceID=workspaceid,
                          InstanceElement=instanceid))

    response = client.service.DeleteInstanceElement(__inject={'msg': xml})
    return response

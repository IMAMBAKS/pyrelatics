import base64, sys
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

def validate_url(url):
    """
    returns url if exist otherwise fails

    :param str url: the url
    :return: url or error
    """

    if sys.version_info.major == 2:
        import urllib2

        req = urllib2.Request(url)
        try:
            urllib2.urlopen(req)
            return url
        except urllib2.HTTPError as e:
            return url, "does not exist: ", e.code
        except urllib2.URLError as e:
            return url, "does not exist: ", e.reason

    else:
        import urllib.request
        import urllib.error

        req = urllib.request.Request(url)
        try:
            urllib.request.urlopen(req)
            return url

        except urllib.request.HTTPError as e:
            return url, "does not exist: ", e.code
        except urllib.request.URLError as e:
            return url, "does not exist: ", e.reason





def convert_dict_to_string(dict_row):
    """
    convert dictionary to an xml-like string

    :param dict dictRow: dictionary of items
    :return: string row
    """
    if type(dict_row) == dict:

        dict_items = ' '.join(["{k}='{v}'".format(k=key, v=value) for (key, value) in dict_row.items()])
        xml_row = ('<Row ' + dict_items + '></Row>')
        return xml_row
    else:
        return "Input must be dictionary"


def encode_data(non_encoded_data)->bytes:
    """
    converts data to a base64 string (python 2) and then to a UTF-8 string (python 3).

    :param str non_encoded_data: The non encoded data.
    :return: encoded_data object
    """
    if sys.version_info.major == 2:
        _data = base64.b64encode(bytes(non_encoded_data, encoding='UTF-8'))
        return _data
    else:
        _data = base64.b64encode(bytes(non_encoded_data, encoding='UTF-8'))
        _data = _data.decode(encoding='UTF-8')
        return _data


def filter_pre_string(_string: str, lines_to_cut: int):
    """
    filter the xml
    """

    filtered_array = _string.splitlines()[lines_to_cut:]
    filtered_string = "".join(filtered_array)
    filtered_string = filtered_string.strip()
    return filtered_string

# Helper function, unescaping HTML
def unescape_html(s: str) -> str:
    s = s.replace('&lt;', '<')
    s = s.replace('&gt;', '>')
    s = s.replace('string', '{}')
    return s

# Get xml for method
def get_xml_for_method(method_url: str) -> str:
    """
    get method specific xml data
    """
    html_doc = urlopen(method_url)
    bs_obj = BeautifulSoup(html_doc, 'html.parser')
    pre_string = unescape_html((bs_obj.find("pre").text))
    xml_string = filter_pre_string(pre_string, 7)
    xml_string = re.sub(r'(?<=>)\s*?(?=<)','', xml_string).strip()
    return xml_string
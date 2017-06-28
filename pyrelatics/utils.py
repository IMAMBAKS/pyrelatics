import base64
import re
from urllib.error import URLError
from urllib import request
from urllib.request import urlopen
from functools import lru_cache
from pyrelatics.typings import *
from bs4 import BeautifulSoup


def validate_url(url: str) -> str:
    """
    Return url if exists otherwise raises Error

    :param str url: the url
    :return: url or error
    """

    req = request.Request(url)
    try:
        request.urlopen(req)
        return url
    except URLError as e:
        return url, "does not exist: ", e.reason


def encode_data(non_encoded_data: str) -> str:
    """
    Encode a UTF-8 string.

    :param str non_encoded_data: The non encoded data.
    :return: encoded_data string
    """
    data = base64.b64encode(bytes(non_encoded_data, encoding='UTF-8'))
    data = data.decode(encoding='UTF-8')
    return data


def filter_pre_string(_string: str, lines_to_cut: int) -> str:
    """
    Filter the xml out of html

    :param str _string:
    :param int lines_to_cut:
    """

    filtered_array = _string.splitlines()[lines_to_cut:]
    filtered_string = "".join(filtered_array)
    filtered_string = filtered_string.strip()
    return filtered_string

def escape_html(s: str)-> str:
    """
    Escape html

    :param str s: string
    :return: replaced html-string
    """
	
	s = s.replace('&','&amp;')
    s = s.replace('<','&lt;')
    s = s.replace( '>','&gt;')
    s = s.replace('"','&quot;')
    s = s.replace("'", '&apos;')
    return s


def unescape_html(s: str) -> str:
    """
    Unescape html

    :param str s: html-string
    :return: replaced string
    """
    s = s.replace('&lt;', '<')
    s = s.replace('&gt;', '>')
    s = s.replace('string', '{}')
    s = s.replace('>xml<', '>{}<')
    return s


@lru_cache()
def get_xml_for_method(method_url: str) -> str:
    """
    Get xml for specific method
    """

    # Open url
    html_doc = urlopen(method_url)
    bs_obj = BeautifulSoup(html_doc, 'html.parser')

    # Find xml part of the given method
    pre_string = unescape_html(bs_obj.find("pre").text)

    # Filter xml
    xml_string = filter_pre_string(pre_string, 7)
    xml_string = re.sub(r'(?<=>)\s*?(?=<)', '', xml_string).strip()
    return xml_string


def create_parameter_xml(data: tuple_or_list_tuple) -> str:
    """
    Return xml string for parameters

    :param dict data:
    :return str:
    """
    parameter_xml_string = '<Parameter Name="{}" Value="{}" />'
    total_string = ''
    if isinstance(data, List[Tuple]):
        for parameter in data:
            total_string += parameter_xml_string.format(parameter[0], parameter[1])
    elif isinstance(data, tuple):
        total_string += parameter_xml_string.format(data[0], data[1])
    elif isinstance(data, str):
        return ''
    else:
        raise TypeError('Please provide a tuple or list of tuple')

    return total_string


def create_row_xml(data: dict_or_list_dict) -> str:
    """
    Return xml string for importing data

    :param data:
    :return:
    """
    total_string = '<Import>'

    if isinstance(data, List[Dict]):
        for item in data:
            xml_string = '<Row'
            item = {key: escape_html(str(value)) for key,value in item.items()}
            for key, value in item.items():
                xml_string += ' {}="{}"'.format(key, value)
            xml_string += '/>'
            total_string += xml_string

        total_string += '</Import>'
        return total_string
    elif isinstance(data, Dict):
        xml_string = '<Row'
        data = {key: escape_html(str(value)) for key,value in data.items()}
        for key, value in data.items():
            xml_string += ' {}="{}"'.format(key, value)
        xml_string += '/>'
        total_string += xml_string
        total_string += '</Import>'
    else:
        raise TypeError('Please provide a dict or list of dicts')

    return total_string


class RelaticsException(PermissionError):
    pass


if __name__ == '__main__':
    pass

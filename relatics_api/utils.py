__author__ = 'imambaksr'
import base64, sys


def validate_url(url):
    """
    returns url if exist otherwise fails

    :param str url: the url
    :return: company url or Error
    """

    if sys.version_info.major == 2:
        import urllib2

        req = urllib2.Request(url)
        try:
            urllib2.urlopen(req)
            return url
        except urllib2.HTTPError as e:
            return url, "couldn't be reached, please check the company: ", e.code
        except urllib2.URLError as e:
            return url, "couldn't be reached: ", e.reason

    else:
        import urllib.request
        import urllib.error

        req = urllib.request.Request(url)
        try:
            urllib.request.urlopen(req)
            return url

        except urllib.request.HTTPError as e:
            return url, "couldn't be reached, please check the company: ", e.code
        except urllib.request.URLError as e:
            return url, "couldn't be reached: ", e.reason





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


def encode_data(non_encoded_data):
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

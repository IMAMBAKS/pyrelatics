import pytest
from relatics_api.utils import *


def test_validate_url():
    assert validate_url('https://google.nl') == 'https://google.nl'


def test_validate_url_raises_error():
    url = 'http://ggasdasassad.com'
    assert 'does not exist: ' in  validate_url(url)


def test_unescape_html():
    input = '&lt;asdasd&gt;asdasdasdasstringasdasd>xml<sss'
    output = '<asdasd>asdasdasdas{}asdasd>{}<sss'
    assert unescape_html(input) == output


def test_filter_pre_string():
    assert filter_pre_string('asdasdasd \n asdasdasd \n \n ddee', 3) == 'ddee'


def test_create_parameter_xml():
    assert create_parameter_xml([('test', 'test2')]) == '<Parameter Name="test" Value="test2" />'
    assert create_parameter_xml(('test', 'test2')) == '<Parameter Name="test" Value="test2" />'


def test_create_parameter_xml_raise_type_error():
    with pytest.raises(TypeError):
        assert create_parameter_xml({'test': 'test2'})


def test_create_row_xml_raise_type_error():
    with pytest.raises(TypeError):
        assert create_row_xml(('test', 'test2')) == '<Row test="test2"/>'


def test_create_row_xml():
    assert create_row_xml({'test': 'test2'}) == '<Import><Row test="test2"/></Import>'
    assert create_row_xml(
        [{'test': 'test2'}, {'test': 'test4'}]) == '<Import><Row test="test2"/><Row test="test4"/></Import>'


def test_encode_data_returns_byte():
    assert type(encode_data('string')) == str


def test_get_xml_for_method():
    url = 'https://kb.relaticsonline.com/api/relaticsapi.asmx?op=CloneInstanceElement'
    assert get_xml_for_method(
        url) == """<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Header><Authentication xmlns="http://www.relatics.com/"><Token>{}</Token></Authentication></soap:Header><soap:Body><CloneInstanceElement xmlns="http://www.relatics.com/"><EnvironmentID>{}</EnvironmentID><WorkspaceID>{}</WorkspaceID><InstanceElement>{}</InstanceElement></CloneInstanceElement></soap:Body></soap:Envelope>"""

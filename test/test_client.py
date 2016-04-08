import pytest

from pyrelatics.client import *
import suds


def test_relaticsapi_raise_exception_with_fake_url():
    with pytest.raises(URLError):
        relaticsapi = RelaticsAPI('fake_company', 'fake_env_id', 'fake_wid')


def test_relaticsapi_initializes_properties():
    relaticsapi = RelaticsAPI('kb', 'fake_env_id', 'fake_wid')
    assert relaticsapi.environment_id == 'fake_env_id'
    assert relaticsapi.workspace_id == 'fake_wid'
    assert relaticsapi.__repr__() != ''


def test_relaticsapi_login_returns_token_or_falsy_message():
    relaticsapi = RelaticsAPI('kb', 'fake_env_id', 'fake_wid')
    assert type(relaticsapi.login('fake_name', 'fake_password')) != str

    with pytest.raises(AttributeError):
        relaticsapi.CreateInstancelement('asdas')


def test_relaticsapi_login_fake_token_raises_exeption():
    relaticsapi = RelaticsAPI('kb', 'fake_env_id', 'fake_wid')
    with pytest.raises(RelaticsException):
        relaticsapi.CreateInstanceElement('asdas')


def test_get_result():
    relaticsapi = RelaticsAPI('kb', 'fake_env_id', 'fake_wid')
    relaticsapi.token = '123123'
    assert isinstance(relaticsapi.GetResult('fake_operation', 'fake_entry_code'), object)


def test_invoke_method_string():
    relaticsapi = RelaticsAPI('kb', 'fake_env_id', 'fake_wid')
    relaticsapi.token = '123123'
    assert isinstance(relaticsapi.CreateInstanceElement('FakeCOR'), object)


def test_invoke_method_tuple():
    relaticsapi = RelaticsAPI('kb', 'fake_env_id', 'fake_wid')
    relaticsapi.token = '123123'
    assert isinstance(relaticsapi.CreateInstanceRelation(('fakeR1', 'fakeR2', 'fakeRR')), object)


def test_Import():
    relaticsapi = RelaticsAPI('kb', 'fake_env_id', 'fake_wid')
    relaticsapi.token = '123123'
    assert isinstance(relaticsapi.Import('fake_operation', 'fake', data=[]), object)

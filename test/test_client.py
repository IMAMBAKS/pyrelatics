import pytest

from pyrelatics.client import *


def test_relaticsapi_raise_exception_with_dummy_url():
    with pytest.raises(URLError):
        RelaticsAPI('dummy_company', 'dummy_env_id', 'dummy_wid')


def test_relaticsapi_initializes_properties():
    relaticsapi = RelaticsAPI('kb', 'dummy_env_id', 'dummy_wid')
    assert relaticsapi.environment_id == 'dummy_env_id'
    assert relaticsapi.workspace_id == 'dummy_wid'
    assert relaticsapi.__repr__() != ''


def test_relaticsapi_login_returns_token_or_falsy_message():
    relaticsapi = RelaticsAPI('kb', 'dummy_env_id', 'dummy_wid')
    assert type(relaticsapi.login('dummy_name', 'dummy_password')) != str

    with pytest.raises(AttributeError):
        relaticsapi.CreateInstancelement('asdas')


def test_relaticsapi_login_dummy_token_raises_exeption():
    relaticsapi = RelaticsAPI('kb', 'dummy_env_id', 'dummy_wid')
    with pytest.raises(RelaticsException):
        relaticsapi.CreateInstanceElement('asdas')


def test_get_result():
    relaticsapi = RelaticsAPI('kb', 'dummy_env_id', 'dummy_wid')
    relaticsapi.token = '123123'
    assert isinstance(relaticsapi.GetResult('dummy_operation', 'dummy_entry_code'), object)


def test_invoke_method_string():
    relaticsapi = RelaticsAPI('kb', 'dummy_env_id', 'dummy_wid')
    relaticsapi.token = '123123'
    assert isinstance(relaticsapi.CreateInstanceElement('dummyCOR'), object)


def test_invoke_method_tuple():
    relaticsapi = RelaticsAPI('kb', 'dummy_env_id', 'dummy_wid')
    relaticsapi.token = '123123'
    assert isinstance(relaticsapi.CreateInstanceRelation(('dummyR1', 'dummyR2', 'dummyRR')), object)


def test_Import():
    relaticsapi = RelaticsAPI('kb', 'dummy_env_id', 'dummy_wid')
    relaticsapi.token = '123123'
    assert isinstance(relaticsapi.Import('dummy_operation', 'dummy', data=[]), object)


# TODO test if user gets warning when login fails.
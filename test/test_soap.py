import pytest

from relatics_api.soap import *


def test_relaticsapi_raise_exception_with_fake_url():
    with pytest.raises(urllib.request.URLError):
        relaticsapi = RelaticsAPI('fake_company', 'fake_env_id', 'fake_wid_d')

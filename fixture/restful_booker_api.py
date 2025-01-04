import pytest
from fixture.api_context import api_request_context
from api.restful_booker_api import RestfulBookerApi


@pytest.fixture(scope="function")
def restful_booker_api(api_request_context) -> RestfulBookerApi:
    """Фикстура для работы с restful booker api"""
    return RestfulBookerApi(request_context=api_request_context)

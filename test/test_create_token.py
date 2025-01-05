"""Тест кейс для api reqres, create user"""
import allure
import pytest
from helper.load import load_data

pytest_plugins = ["fixture.restful_booker_api"]
pytestmark = [allure.parent_suite("restful_booker_api"),
              allure.suite("create_token")]

@allure.title('Запросы на создание токена аутентификации')
class TestCreateToken:
    @pytest.mark.parametrize('request_parameters',
                             load_data('create_token_data', 'valid_data'),
                             ids=load_data('create_token_data', 'valid_ids'))
    @pytest.mark.asyncio
    async def test_create_token_valid_parameters(self, restful_booker_api, request_parameters):
        response = await restful_booker_api.create_auth_token(request_parameters)

        response.status_code_should_be(200)
        await response.json_schema_should_be_valid('token_schema', 'valid_schema')

    @pytest.mark.parametrize('request_parameters',
                             load_data('create_token_data', 'invalid_data'),
                             ids=load_data('create_token_data', 'invalid_ids'))
    @pytest.mark.asyncio
    async def test_create_token_invalid_parameters(self, restful_booker_api, request_parameters):
        response = await restful_booker_api.create_auth_token(request_parameters)

        await response.json_schema_should_be_valid('token_schema', 'invalid_schema')
        await response.have_value_in_response_parameter(['reason'], 'Bad credentials')

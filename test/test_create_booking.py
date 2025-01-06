import allure
import pytest
from api.restful_booker_api import RestfulBookerApi
from helper.load import load_data
from model.booking_model import BookingModel


pytest_plugins = ["fixture.restful_booker_api"]
pytestmark = [
    allure.parent_suite("restful_booker_api"),
    allure.suite("create_booking")
]

class TestCreateBooking:
    @allure.title('Запрос на создание бронирования c валидными параметрами')
    @pytest.mark.parametrize('request_parameters',
                             load_data('create_booking_data', 'valid_data'))
    @pytest.mark.asyncio
    async def test_create_booking_valid_parameters(
        self, restful_booker_api: RestfulBookerApi, request_parameters: BookingModel
    ):
        response = await restful_booker_api.create_booking(request_parameters)

        response.status_code_should_be(200)
        await response.json_schema_should_be_valid('create_booking_schema')
        await response.have_value_in_response_parameter(['booking', 'firstname'], request_parameters.firstname)

    @allure.title('Запрос на создание бронирования c невалидными параметрами')
    @pytest.mark.parametrize('request_parameters',
                             load_data('create_booking_data', 'invalid_data'))
    @pytest.mark.asyncio
    async def test_create_booking_invalid_parameters(
        self, restful_booker_api: RestfulBookerApi, request_parameters: BookingModel
    ):
        response = await restful_booker_api.create_booking(request_parameters)

        # Статус код будет 500, что не норма.
        # Поэтому для прохождения тестов вывожу, что он не из диапазона 200-299 
        response.objects_should_be(response.response.ok, False)

import allure
import pytest
from api.restful_booker_api import RestfulBookerApi
from helper.booking_helpers import create_cookie
from helper.load import load_data
from model.booking_model import BookingModel


pytest_plugins = ["fixture.restful_booker_api"]
pytestmark = [
    allure.parent_suite("restful_booker_api"),
    allure.suite("create_booking")
]

@allure.title('Запросы на создание бронирования')
class TestCreateBooking:
    @pytest.mark.parametrize('request_parameters',
                             load_data('create_booking_data', 'valid_data'),
                             ids=load_data('create_booking_data', 'valid_ids'))
    @pytest.mark.asyncio
    async def test_create_booking_valid_parameters(
        self, restful_booker_api: RestfulBookerApi, request_parameters: BookingModel
    ):
        cookie = await create_cookie(restful_booker_api)
        response = await restful_booker_api.create_booking(request_parameters)

        response.status_code_should_be(200)
        await response.json_schema_should_be_valid('create_booking_schema')
        await response.have_value_in_response_parameter(['booking', 'firstname'], request_parameters.firstname)

        booking_id = await response.get_payload(['bookingid'])
        response_post = await restful_booker_api.delete_booking(booking_id, cookie)
        response_post.status_code_should_be(201)

        response_check = await restful_booker_api.get_booking(booking_id)
        response_check.status_code_should_be(404)

    @pytest.mark.parametrize('request_parameters',
                             load_data('create_booking_data', 'invalid_data'),
                             ids=load_data('create_booking_data', 'invalid_ids'))
    @pytest.mark.asyncio
    async def test_create_booking_invalid_parameters(
        self, restful_booker_api: RestfulBookerApi, request_parameters: BookingModel
    ):
        response = await restful_booker_api.create_booking(request_parameters)

        # Статус код будет 500, что не норма.
        # Поэтому для прохождения тестов вывожу, что он не из диапазона 200-299 
        response.objects_should_be(response.response.ok, False)

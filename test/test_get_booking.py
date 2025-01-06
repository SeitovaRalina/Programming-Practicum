from typing import Any
import allure
import pytest
from api.restful_booker_api import RestfulBookerApi
from helper.booking_helpers import create_booking
from helper.load import load_data


pytest_plugins = ["fixture.restful_booker_api"]
pytestmark = [
    allure.parent_suite("restful_booker_api"),
    allure.suite("get_booking")
]

class TestGetBooking:
    @allure.title('Запрос на получение бронирования по валидному id')
    @pytest.mark.asyncio
    async def test_get_booking_valid_id(self, restful_booker_api: RestfulBookerApi):
        booking = await create_booking(restful_booker_api)

        response = await restful_booker_api.get_booking(booking['bookingid'])

        response.status_code_should_be(200)
        await response.json_schema_should_be_valid('booking_schema')
        response.objects_should_be(booking['booking'], await restful_booker_api.deserialize_booking())

    @allure.title('Запрос на получение бронирования по невалидному id')
    @pytest.mark.parametrize(
        'invalid_booking_id', load_data('get_booking_data'))
    @pytest.mark.asyncio
    async def test_get_booking_invalid_id(
        self, restful_booker_api: RestfulBookerApi, invalid_booking_id: Any
    ):
        response = await restful_booker_api.get_booking(invalid_booking_id)
        
        response.status_code_should_be(404)
        response.objects_should_be('Not Found', await response.response.text())

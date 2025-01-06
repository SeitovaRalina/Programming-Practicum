from typing import Any
import allure
import pytest
from api.restful_booker_api import RestfulBookerApi
from helper.booking_helpers import create_cookie, create_booking
from helper.load import load_data

pytest_plugins = ["fixture.restful_booker_api"]
pytestmark = [
    allure.parent_suite("restful_booker_api"),
    allure.suite("delete_booking"),
]

class TestDeleteBooking:
    @allure.title("Запрос на удаление бронирования с валидным id")
    @pytest.mark.asyncio
    async def test_delete_booking_valid_id(self, restful_booker_api: RestfulBookerApi):
        cookie = await create_cookie(restful_booker_api)
        booking = await create_booking(restful_booker_api)
        booking_id = booking["bookingid"]

        response = await restful_booker_api.delete_booking(booking_id, cookie)

        response.status_code_should_be(201)
        get_response = await restful_booker_api.get_booking(booking_id)
        get_response.status_code_should_be(404)

    @allure.title("Запрос на удаление бронирования с невалидным id")
    @pytest.mark.parametrize(
        "invalid_booking_id", load_data("delete_booking_data")
    )
    @pytest.mark.asyncio
    async def test_delete_booking_invalid_id(
        self, restful_booker_api: RestfulBookerApi, invalid_booking_id: Any
    ):
        cookie = await create_cookie(restful_booker_api)

        response = await restful_booker_api.delete_booking(invalid_booking_id, cookie)

        response.status_code_should_be(405)

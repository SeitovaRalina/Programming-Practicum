import pytest
import allure
from helper.booking_helpers import create_cookie, create_booking
from helper.load import load_data
from api.restful_booker_api import RestfulBookerApi
from model.booking_model import BookingModel


pytest_plugins = ["fixture.restful_booker_api"]
pytestmark = [
    allure.parent_suite("restful_booker_api"),
    allure.suite("update_booking")
]

class TestUpdateBooking:
    @allure.title("Запрос на обновление бронирования с валидными параметрами")
    @pytest.mark.parametrize(
        "request_parameters", load_data("update_booking_data", "valid_data")
    )
    @pytest.mark.asyncio
    async def test_update_booking_valid_parameters(
        self, restful_booker_api: RestfulBookerApi, request_parameters: BookingModel
    ):
        cookie = await create_cookie(restful_booker_api)
        booking = await create_booking(restful_booker_api)
        booking_id = booking["bookingid"]

        response = await restful_booker_api.update_booking(booking_id, cookie, request_parameters)

        response.status_code_should_be(200)
        await response.json_schema_should_be_valid("booking_schema")
        await response.have_value_in_response_parameter(["firstname"], request_parameters.firstname)
        await response.have_value_in_response_parameter(["lastname"], request_parameters.lastname)

    @allure.title("Запрос на обновление бронирования с невалидными параметрами")
    @pytest.mark.parametrize(
        "request_parameters", load_data("update_booking_data", "invalid_data")
    )
    @pytest.mark.asyncio
    async def test_update_booking_invalid_parameters(
        self, restful_booker_api: RestfulBookerApi, request_parameters: BookingModel
    ):
        cookie = await create_cookie(restful_booker_api)
        booking_id = await create_booking(restful_booker_api)

        response = await restful_booker_api.update_booking(booking_id, cookie, request_parameters)

        response.status_code_should_be(400)
        response.objects_should_be("Bad Request", await response.response.text())

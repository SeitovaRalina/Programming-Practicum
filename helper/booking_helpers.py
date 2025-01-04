from api.restful_booker_api import RestfulBookerApi
from helper.load import load_data


async def create_cookie(restful_booker_api: RestfulBookerApi) -> dict:
    """
    Создает токен аутентификации и возвращает заголовок Cookie.
    """
    request_parameters = load_data("create_token_data", "valid_data")[0]
    response = await restful_booker_api.create_auth_token(request_parameters)
    token = await response.get_payload(["token"])
    return {"Cookie": f"token={token}"}


async def create_booking(restful_booker_api: RestfulBookerApi) -> int:
    """
    Создает бронирование и возвращает его ID.
    """
    request_parameters= load_data("create_booking_data", "valid_data")[0]
    response = await restful_booker_api.create_booking(request_parameters)
    return await response.get_payload([])

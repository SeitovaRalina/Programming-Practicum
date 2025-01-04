import allure
from playwright.async_api import APIRequestContext
from jsonschema import validate
from helper.logger import log
from helper.load import load_json_schema
from helper.parser import get_data


class Api:
    """Основной класс для работы с Api"""
    _HEADERS = {"Content-Type": "application/json"}
    _TIMEOUT = 1000
    
    def __init__(self, request_context: APIRequestContext):
        self.response = None
        self.request_context = request_context

    @allure.step("Отправление POST запроса")
    async def post(self, url: str, endpoint: str, json_body: dict = None):
        with allure.step(f"POST запрос на url: {url}{endpoint}"
                         f"\n тело запроса: \n {json_body}"):
            self.response = await self.request_context.post(url=f"{url}{endpoint}",
                                          headers=self._HEADERS,
                                          data=json_body,
                                          timeout=self._TIMEOUT)
        await log(response=self.response, method="POST",request_body=json_body)
        return self

    @allure.step("Отправление PUT запроса")
    async def put(self, url: str, endpoint: str, params: dict = None, json_body: dict = None):
        with allure.step(f"PUT запрос на url: {url}{endpoint}"
                         f"\n тело запроса: \n {json_body}"):
            self.response = await self.request_context.put(url=f"{url}{endpoint}",
                                         headers=self._HEADERS | params,
                                         data=json_body,
                                         timeout=self._TIMEOUT)
        await log(response=self.response, method="PUT", request_body=json_body)
        return self

    @allure.step("Отправление GET запроса")
    async def get(self, url: str, endpoint: str):
        with allure.step(f"GET запрос на url: {url}{endpoint}"):
            self.response = await self.request_context.get(url=f"{url}{endpoint}",
                                         headers=self._HEADERS,
                                         timeout=self._TIMEOUT)
        await log(response=self.response, method="GET")
        return self

    @allure.step("Отправление DELETE запроса")
    async def delete(self, url: str, endpoint: str, params: dict = None):
        with allure.step(f"DELETE запрос на url: {url}{endpoint}"):
            self.response = await self.request_context.delete(url=f"{url}{endpoint}",
                                         headers=self._HEADERS | params,
                                         timeout=self._TIMEOUT)
        await log(response=self.response, method="DELETE")
        return self

    # ASSERTIONS:

    @allure.step("ОР: Статус код ответа равен {expected_code}")
    def status_code_should_be(self, expected_code: int):
        """Проверяем статус код ответа actual_code на соответствие expected_code"""
        actual_code = self.response.status
        assert expected_code == actual_code, f"\nОжидаемый результат: {expected_code} " \
                                             f"\nФактический результат: {actual_code}"
        return self

    @allure.step("ОР: Cхема ответа json валидна")
    async def json_schema_should_be_valid(self, path_json_schema: str, name_json_schema: str = "schema"):
        """Проверяем полученный ответ на соответствие json схеме"""
        json_schema = load_json_schema(path_json_schema, name_json_schema)
        validate(await self.response.json(), json_schema)
        return self

    @allure.step("ОР: Объекты равны")
    def objects_should_be(self, expected_object, actual_object):
        """Сравниваем два объекта"""
        assert expected_object == actual_object, f"\nОжидаемый результат: {expected_object} " \
                                                 f"\nФактический результат: {actual_object}"
        return self

    @allure.step("ОР: В поле ответа содержится искомое значение")
    async def have_value_in_response_parameter(self, keys: list, value: str):
        """Сравниваем значение необходимого параметра"""
        payload = await self.get_payload(keys)
        assert value == payload, f"\nОжидаемый результат: {value} " \
                                 f"\nФактический результат: {payload}"
        return self

    async def get_payload(self, keys: list):
        """Получаем payload переходя по ключам, и возвращаем полученный payload"""
        response = await self.response.json()
        payload = get_data(keys, response)
        return payload

import allure
from api.api import Api
from model.booking_model import BookingModel
from model.token_model import TokenModel
from datetime import datetime as dt, date


class RestfulBookerApi(Api):
    _URL = 'https://restful-booker.herokuapp.com'
    _ENDPOINTS = {'auth': '/auth/', 'booking': '/booking/'}

    @allure.step('Аутентификация')
    async def create_auth_token(self, param_request_body: TokenModel):
        return await self.post(url=self._URL,
                         endpoint=self._ENDPOINTS['auth'], 
                         json_body=param_request_body.to_dict())
    
    @allure.step('Создание бронирования')
    async def create_booking(self, param_request_body: BookingModel):
        return await self.post(url=self._URL,
                         endpoint=self._ENDPOINTS['booking'],
                         json_body=param_request_body.to_dict())
    
    @allure.step('Получение бронирования по ID')
    async def get_booking(self, booking_id: int):
        return await self.get(url=self._URL,
                         endpoint=self._ENDPOINTS['booking'] + f'{booking_id}')
    
    @allure.step('Обновление бронирования')
    async def update_booking(self, booking_id: int, cookie: dict, param_request_body: BookingModel):
        return await self.put(url=self._URL,
                         endpoint=self._ENDPOINTS['booking'] + f'{booking_id}',
                         params=cookie,
                         json_body=param_request_body.to_dict())
    
    @allure.step('Удаление бронирования')
    async def delete_booking(self, booking_id: int, cookie: dict):
        return await self.delete(url=self._URL,
                         params=cookie,
                         endpoint=self._ENDPOINTS['booking'] + f'{booking_id}')
    
    async def deserialize_booking(self):
        payload = await self.get_payload([])
        return BookingModel(firstname=payload['firstname'],
                            lastname=payload['lastname'],
                            totalprice=payload['totalprice'],
                            depositpaid=payload['depositpaid'],
                            checkin=dt.strptime(payload['bookingdates']['checkin'], '%Y-%m-%d').date(),
                            checkout=dt.strptime(payload['bookingdates']['checkout'], '%Y-%m-%d').date(),
                            additionalneeds=payload['additionalneeds']).to_dict() if payload else None

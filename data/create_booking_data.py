from model.booking_model import BookingModel
from datetime import date


valid_data = (
    BookingModel(
        firstname="John", 
        lastname="Doe", 
        totalprice=1000, 
        depositpaid=True, 
        checkin=date(2019, 12, 4), 
        checkout=date(2019, 12, 10), 
        additionalneeds="Breakfast"
    ),
    BookingModel(
        firstname="",                          # поле допускает пустую строку
        lastname="",                           # поле допускает пустую строку
        totalprice=-1,                         # поле заменится на null
        depositpaid="no",                      # поле заменится на true
        checkin=date(2019, 12, 4),             # checkin позже checkout, нет ошибки (¬_¬ )
        checkout="2018/01/01 or 2018/01/02",   # поле заменится на 1970-01-01
        # поле additionalneeds необязательно
    ),
)
valid_ids = (
    'All fields are valid',
    'All fields contain errors, but they are handled by the API',
)

invalid_data = (
    BookingModel(
        lastname="Doe", 
        totalprice=100, 
        depositpaid=True, 
        checkin=date(2019, 12, 4), 
        checkout=date(2019, 12, 10)
    ),
    BookingModel(
        firstname="John", 
        totalprice=100, 
        depositpaid=True, 
        checkin=date(2019, 12, 4), 
        checkout=date(2019, 12, 10)
    ),
    BookingModel(
        firstname="John", 
        lastname="Doe", 
        depositpaid=True, 
        checkin=date(2019, 12, 4), 
        checkout=date(2019, 12, 10)
    ),
    BookingModel(
        firstname="John", 
        lastname="Doe", 
        totalprice=100,  
        checkin=date(2019, 12, 4), 
        checkout=date(2019, 12, 10)
    ),
    BookingModel(
        firstname="John", 
        lastname="Doe", 
        totalprice=100, 
        depositpaid=True, 
    ),
    BookingModel(
        firstname="John",
        lastname="Doe",
        totalprice=100,
        depositpaid=True,
        checkin=date(2023, 1, 1),
    ),
    BookingModel(
        firstname=123, 
        lastname="Doe", 
        totalprice=100, 
        depositpaid=True, 
        checkin=date(2025, 1, 1), 
        checkout=date(2025, 1, 10)
    ),
    BookingModel(
        firstname="John", 
        lastname=True,
        totalprice=100,
        depositpaid=0, 
        checkin=date(1000, 1, 1),
        checkout=date(2025, 1, 10),
    ),
    BookingModel()
)
invalid_ids = (
    'Missing required parameter: firstname',
    'Missing required parameter: lastname',
    'Missing required parameter: totalprice',
    'Missing required parameter: depositpaid',
    'Missing required parameter: bookingdates',
    'Missing required parameter: checkout',
    'Invalid data type: int in firstname',
    'Invalid data type: bool in lastname',
    'All parameters are missing',
)

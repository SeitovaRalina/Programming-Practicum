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
        firstname="John",
        lastname="Doe",
        totalprice=-1,
        depositpaid=True,
        checkin=date(2023, 1, 1),
        checkout=date(2019, 12, 10), 
        additionalneeds="Breakfast&Lunch"
    ),
)

invalid_data = (
    BookingModel(
        firstname="John",
        lastname="Doe",
        totalprice=100,
        depositpaid=True,
        checkin=date(2023, 1, 1),
    ),
    BookingModel(
        firstname="", 
        lastname="", 
        totalprice=0, 
        checkin=date(2020, 1, 12), 
        checkout=date(2019, 12, 12), 
        additionalneeds=""
    )
)

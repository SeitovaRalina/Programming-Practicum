from datetime import date
from model.booking_model import BookingModel


valid_data = (BookingModel(
    firstname="Ivan", 
    lastname="Ivanov", 
    totalprice=1000, 
    depositpaid=True, 
    checkin=date(2019, 12, 4), 
    checkout=date(2019, 12, 10), 
    additionalneeds="Breakfast"
),)

invalid_data = (BookingModel(
    firstname="John", 
    lastname="Doe", 
    totalprice=1000, 
    depositpaid=True, 
    checkout=date(2019, 12, 10), 
    additionalneeds="Breakfast"
),)
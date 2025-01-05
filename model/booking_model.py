from dataclasses import dataclass, asdict
from datetime import date
from typing import Optional


@dataclass
class BookingModel:
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    totalprice: Optional[int] = None
    depositpaid: Optional[bool] = None
    checkin: Optional[date] = None
    checkout: Optional[date] = None
    additionalneeds: Optional[str] = None

    def to_dict(self):
        data = asdict(self)
        result = {key: value for key, value in data.items() if value is not None}

        bookingdates = {}
        if self.checkin:
            bookingdates["checkin"] = self.checkin.isoformat() if type(self.checkin) is date else self.checkin
        if self.checkout:
            bookingdates["checkout"] = self.checkout.isoformat() if type(self.checkout) is date else self.checkout

        if bookingdates:
            result["bookingdates"] = bookingdates
        
        result.pop("checkin", None)
        result.pop("checkout", None)
        
        return result

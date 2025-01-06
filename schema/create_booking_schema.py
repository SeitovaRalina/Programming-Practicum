from .booking_schema import schema

schema = {
    "type": "object",
    "properties": {
        "bookingid": {"type": "integer"},
        "booking": schema,
    },
    "required": ["bookingid", "booking"]
}

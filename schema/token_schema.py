valid_schema = {
    "type": "object",
    "properties": {
        "token": {"type": "string"}
    },
    "required": ["token"]
}

invalid_schema = {
    "type": "object",
    "properties": {
        "reason": {"type": "string"}
    },
    "required": ["reason"]
}

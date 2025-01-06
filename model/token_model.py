from dataclasses import dataclass, asdict


@dataclass
class TokenModel:
    username: str
    password: str

    def to_dict(self):
        return asdict(self)

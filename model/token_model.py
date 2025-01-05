from dataclasses import dataclass, field, asdict
from typing import Optional


@dataclass
class TokenModel:
    username: Optional[str] = field(default=None)
    password: Optional[str] = field(default=None)

    def to_dict(self):
        return {k: v for k, v in asdict(self).items() if v is not None}

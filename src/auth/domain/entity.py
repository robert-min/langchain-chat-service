from __future__ import annotations

from dataclasses import dataclass
from shared.domain.entity import Entity


@dataclass(eq=False)
class Auth(Entity):
    email: str
    password: bytes

    @classmethod
    def new(cls, email: str, password: bytes) -> Auth:
        return cls(email=email, password=password)

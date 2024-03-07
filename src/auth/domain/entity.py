from __future__ import annotations

from dataclasses import dataclass
from shared.domain.entity import Entity


@dataclass(eq=False)
class Auth(Entity):
    email: str
    password: str | bytes = None

    @classmethod
    def new(cls, email: str, password: bytes = None) -> Auth:
        return cls(email=email, password=password)


@dataclass
class Token:
    id: str
    token: str

    @classmethod
    def new(cls, email: str, token: str) -> Token:
        return cls(id=email, token=token)

from dataclasses import dataclass


@dataclass
class Account:
    id: str
    pasword: bytes
    status: bool

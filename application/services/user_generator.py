from typing import NamedTuple, Iterator
from application.services import faker


class User(NamedTuple):
    name: str
    email: str

    def get_dict(self) -> dict:
        return self._asdict()

    @classmethod
    def get_fieldnames(cls) -> list[str]:
        return list(cls._fields)

    @classmethod
    def from_dict(cls, data: dict) -> "User":
        return cls(**data)


def generate_user() -> User:
    return User(
        name=faker.first_name(),
        email=faker.email()
    )


def generate_users(amount: int) -> Iterator[User]:
    for _ in range(amount):
        yield generate_user()

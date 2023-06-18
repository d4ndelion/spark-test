from dataclasses import dataclass


@dataclass
class Quote:
    text: str
    author: str
    tags: list[str]


@dataclass
class Author:
    name: str
    readable_name: str
    birthdate: str
    birthplace: str
    description: str

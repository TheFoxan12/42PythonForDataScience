import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """class to represent a student"""
    name: str
    surname: str
    login: str
    id: str = field(default=generate_id())

    def __init__(self, name, surname):
        """initiate a student with name and surname passed as an argument"""
        self.name = name
        self.surname = surname
        self.login = name[0] + surname

from abc import ABC, abstractmethod


class Character(ABC):
    """Base abstract class for characters, containing first_name
and living state"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initiate a character with first name and living state
        according to is_alive"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        pass


class Stark(Character):
    """Concrete implementation of character class"""
    def __init__(self, first_name: str, is_alive: bool = True):
        """Initiate a character with first name and living state\
according to is_alive"""
        super().__init__(first_name, is_alive)

    def die(self):
        """Change the state of the character to dead, is_alive=False"""
        self.is_alive = False

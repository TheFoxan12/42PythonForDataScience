from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initiate a character with first name and living state\
according to is_alive, which belongs to Baratheon family"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self._eyes = "brown"
        self._hairs = "dark"

    def __repr__(self):
        return (f"Vector: ('{self.family_name}', "
                f"'{self._eyes}', '{self._hairs}')")

    def __str__(self):
        return self.__repr__()

    def die(self):
        """Change the state of the character to dead, is_alive=False"""
        self.is_alive = False


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initiate a character with first name and living state\
according to is_alive, which belongs to Lannister family"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self._eyes = "blue"
        self._hairs = "light"

    def __repr__(self):
        return (f"Vector: ('{self.family_name}', "
                f"'{self._eyes}', '{self._hairs}')")

    def __str__(self):
        return self.__repr__()

    def die(self):
        """Change the state of the character to dead, is_alive=False"""
        self.is_alive = False

    @staticmethod
    def create_lannister(first_name: str, is_alive: bool = True):
        """static method to create characters in a chain easily"""
        return Lannister(first_name, is_alive)

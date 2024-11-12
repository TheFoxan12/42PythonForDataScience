from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """The King"""

    def __init(self, first_name: str,
               is_alive: bool = True):
        """initiate the King"""
        super().__init__(first_name, is_alive)

    # eyes getter
    def get_eyes(self):
        """get the eyes color"""
        return self._eyes

    # eyes setter
    def set_eyes(self, color: str):
        """set the eyes color"""
        self._eyes = color

    # hairs getter
    def get_hairs(self):
        """get the hairs color"""
        return self._hairs

    # hairs setter
    def set_hairs(self, color: str):
        """set the hairs color"""
        self._hairs = color

    eyes = property(
        fget=get_eyes,
        fset=set_eyes
    )

    hairs = property(
        fget=get_hairs,
        fset=set_hairs
    )

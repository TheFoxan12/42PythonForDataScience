
class calculator:
    """calculations (addition, multiplication,
subtraction, division) of vector with a scalar"""

    def __init__(self, vector):
        """initiate a vector object"""
        self.vector = vector

    def __add__(self, value) -> None:
        """scalar addition on vector"""
        self.vector = [x + value for x in self.vector]
        print(self.vector)

    def __mul__(self, value) -> None:
        """scalar multiplication on vector"""
        self.vector = [x * value for x in self.vector]
        print(self.vector)

    def __sub__(self, value) -> None:
        """scalar substraction on vector"""
        self.vector = [x - value for x in self.vector]
        print(self.vector)

    def __truediv__(self, value) -> None:
        """scalar division on vector"""
        if value == 0:
            print("can't divide by 0")
        else:
            self.vector = [x / value for x in self.vector]
            print(self.vector)

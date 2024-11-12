
class calculator:
    """dotproduct, addition and substraction of two vectors,
without instanciation"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Dot product of two vectors"""
        result = 0
        for elt in zip(V1, V2):
            result += elt[0] * elt[1]
        print(f"Dot product is {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Addition of two vectors"""
        result = []
        for elt in zip(V1, V2):
            result.append(float(elt[0] + elt[1]))
        print(f"Add vector is : {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Substraction of two vectors"""
        result = []
        for elt in zip(V1, V2):
            result.append(float(elt[0] - elt[1]))
        print(f"Sous vector is : {result}")

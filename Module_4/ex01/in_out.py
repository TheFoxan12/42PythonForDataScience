
def square(x: int | float) -> int | float:
    """return the square of a number passed as an argument"""
    return x ** 2


def ft_pow(x: int | float) -> int | float:
    """returns the exponentiation of a number by itself"""
    return x ** x


def outer(x: int | float, function) -> object:
    """returns an object when called perform the next operation of a function
passed as an argument on a number passed as an argument"""
    count = 0

    def inner() -> float:
        nonlocal count
        r = function(x)
        for _ in range(count):
            r = function(r)
        count += 1
        return r

    return inner

import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float])\
        -> list[int | float]:
    """calculates the bmi of every couple height/weight passed as \
a parameter"""
    h = np.array(height)
    w = np.array(weight)
    try:
        return (w / (h ** 2)).tolist()
    except TypeError:
        print("List must contains int or float")
        return []
    except ValueError:
        print("List must have the same size")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """returns a list with true for values above the limit passed as\
a parameter and else false"""
    return [x > limit for x in bmi]

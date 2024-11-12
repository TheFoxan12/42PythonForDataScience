import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """takes as parameters a 2D array, prints its shape, and returns a
truncated version of the array based on the provided start and end arguments"""
    fam = np.array(family)
    print(f"My shape is : {fam.shape}")
    res = fam[start:end]
    print(f"My new shape is : {res.shape}")
    return res.tolist()

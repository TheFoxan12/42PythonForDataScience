import numpy as np
from PIL import Image, UnidentifiedImageError


def ft_load(path: str) -> np.ndarray | None:
    """function that loads the image passed as a parameter as a ndarray"""
    try:
        img = Image.open(path)
        img_array = np.array(img)
        print(f"The shape of the image is : {img_array.shape}")
        return img_array
    except FileNotFoundError:
        print("File not found")
        return None
    except UnidentifiedImageError:
        print("File is not a good image")
        return None

import numpy as np
from matplotlib import pyplot as plt


def ft_invert(array) -> np.ndarray:
    """Inverts the color of the image received."""
    result = np.array(array)
    for row in result:
        for pixel in row:
            pixel[0] = 255 - pixel[0]
            pixel[1] = 255 - pixel[1]
            pixel[2] = 255 - pixel[2]

    display_image(result)
    return result


def ft_red(array) -> np.ndarray:
    """Redify the color of the image received."""
    result = np.array(array)
    for row in result:
        for pixel in row:
            pixel[0] *= 1
            pixel[1] *= 0.1
            pixel[2] *= 0.1

    display_image(result)
    return result


def ft_green(array) -> np.ndarray:
    """Greenify the color of the image received."""
    result = np.array(array)
    for row in result:
        for pixel in row:
            if pixel[0] >= 10:
                pixel[0] -= (pixel[0] - 10)
            else:
                pixel[0] = pixel[0]
            pixel[1] -= 0
            if pixel[2] >= 10:
                pixel[2] -= (pixel[2] - 10)
            else:
                pixel[2] = pixel[2]

    display_image(result)
    return result


def ft_blue(array) -> np.ndarray:
    """Blueify the color of the image received."""
    result = np.array(array)
    for row in result:
        for pixel in row:
            pixel[0] = 10
            pixel[1] = 10
            pixel[2] = pixel[2]

    display_image(result)
    return result


def ft_grey(array) -> np.ndarray:
    """Greyify the color of the image received."""
    result = np.array(array)
    for row in result:
        for pixel in row:
            val = int(pixel[0]) + int(pixel[1]) + int(pixel[2])
            val /= 3
            pixel[0] = val
            pixel[1] = val
            pixel[2] = val

    display_image(result)
    return result


def display_image(array):
    """Displays the image received."""
    plt.imshow(array)
    plt.show()

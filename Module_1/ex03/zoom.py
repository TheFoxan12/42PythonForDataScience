from load_image import ft_load
import numpy as np
from matplotlib import pyplot as plt


def main():
    """programs that load an image and performs a zoom"""
    img = ft_load("animal.jpeg")
    if img is None:
        print("There was a problem with the image")
        return

    print(f"The image is {img.shape[1]} pixel wide and"
          f" {img.shape[0]} pixels tall")
    print(f"The image has {img.shape[2]} color channels")

    img_sliced: np.ndarray = img[100:500, 450:850, 0:1]
    img_sliced2: np.ndarray = img[100:500, 450:850, 0]
    print(f"New shape after slicing : {img_sliced.shape}"
          f" or {img_sliced2.shape}")
    print(img_sliced)
    plt.imshow(img_sliced, cmap="gray")
    plt.show()


if __name__ == '__main__':
    main()

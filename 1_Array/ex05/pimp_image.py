from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def main():
    path = "landscape.jpg"
    img = ft_load(path)
    plt.imshow(img)
    plt.show()


if __name__ == "__main__":
    main()

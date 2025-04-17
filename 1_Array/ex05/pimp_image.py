from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def ft_invert(array) -> np.ndarray:
    invert = array
    for y in range(len(invert)):
        for x in range(len(invert[0])):
            invert[y][x] = 255 - invert[y][x]
    plt.imshow(invert)
    plt.show()
    return invert


#def ft_red(array) -> np.ndarray:
#    print(array)


#def ft_blue(array) -> array:
#    print(array)


#def ft_green(array) -> array:
#    print(array)


#def ft_gray(array) -> array:
#    print(array)


def main():
    path = "landscape.jpg"
    array = ft_load(path)
    ft_invert(array)


if __name__ == "__main__":
    main()

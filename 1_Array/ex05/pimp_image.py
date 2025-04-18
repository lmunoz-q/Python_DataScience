from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def ft_invert(array) -> np.ndarray:
    for y in range(len(array)):
        for x in range(len(array[0])):
            array[y][x] = 255 - array[y][x]
    plt.imshow(array)
    plt.show()
    return array


def ft_red(array) -> np.ndarray:
    for y in range(len(array)):
        for x in range(len(array[0])):
            array[y][x][1] = 0
            array[y][x][2] = 0
    plt.imshow(array)
    plt.show()
    return array


def ft_blue(array) -> np.ndarray:
    for y in range(len(array)):
        for x in range(len(array[0])):
            array[y][x][0] = 0
            array[y][x][1] = 0
    plt.imshow(array)
    plt.show()
    return array


def ft_green(array) -> np.ndarray:
    for y in range(len(array)):
        for x in range(len(array[0])):
            array[y][x][0] = 0
            array[y][x][2] = 0
    plt.imshow(array)
    plt.show()
    return array


def ft_gray(array) -> np.array:
    for y in range(len(array)):
        for x in range(len(array[0])):
            gray = int(int(array[y][x][0]) + int(array[y][x][1]) + int(array[y][x][2])) / 3
            array[y][x][0] = np.uint8(gray)
            array[y][x][1] = np.uint8(gray)
            array[y][x][2] = np.uint8(gray)
    plt.imshow(array)
    plt.show()
    return array


def main():
    path = "landscape.jpg"
    array = ft_load(path)
    ft_gray(array)


if __name__ == "__main__":
    main()

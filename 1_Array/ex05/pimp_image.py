import matplotlib.pyplot as plt
import numpy as np


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Invert the colors of the image received, and return a np.ndarray.

    Parameters
    ----------
    array : np.ndarray

    Returns
    -------
    np.ndarray
        The same image array, modified in-place with invert colors.
    """
    for y in range(len(array)):
        for x in range(len(array[0])):
            array[y][x] = 255 - array[y][x]
    print(f"the shape of image is : {array.shape}")
    print(array[0])
    plt.imshow(array)
    plt.show()
    return array


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Removes all colors except red of the image received and return into
    np.ndarray.

    Parameters
    ----------
    array : np.ndarray
        Input image array of shape (H, W, 3)

    Returns
    -------
    np.ndarray
        The same image array, modified in-place and removing all colors except
        red.
    """
    print(f"the shape of image is : {array.shape}")
    for y in range(len(array)):
        for x in range(len(array[0])):
            array[y][x][1] = 0
            array[y][x][2] = 0
    print(f"the shape of image is : {array.shape}")
    print(array[0])
    plt.imshow(array)
    plt.show()
    return array


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Removes all colors except blue of the image received and return into
    np.ndarray.

    Parameters
    ----------
    array : np.ndarray
        Input image array of shape (H, W, 3)

    Returns
    -------
    np.ndarray
        The same image array, modified in-place removing all colors except
        blue.
    """
    for y in range(len(array)):
        for x in range(len(array[0])):
            array[y][x][0] = 0
            array[y][x][1] = 0
    print(f"the shape of image is : {array.shape}")
    print(array[0])
    plt.imshow(array)
    plt.show()
    return array


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Removes all colors except green of the image received and return into a
    np.ndarray.

    Parameters
    ----------
    array : np.ndarray
        Input image array of shape (H, W, 3)

    Returns
    -------
    np.ndarray
        The same image array, modified in-place removing all colors except
        green.
    """
    for y in range(len(array)):
        for x in range(len(array[0])):
            array[y][x][0] = 0
            array[y][x][2] = 0
    print(f"the shape of image is : {array.shape}")
    print(array[0])
    plt.imshow(array)
    plt.show()
    return array


def ft_grey(array: np.ndarray) -> np.array:
    """
    Converts a color image to grayscale by averaging RGB channels.

    Parameters
    ----------
    array : np.ndarray
        Input image array of shape (H, W, 3)

    Returns
    -------
    np.ndarray
        The same image array, modified in-place as grayscale.
    """
    for y in range(len(array)):
        for x in range(len(array[0])):
            gray = int(int(array[y][x][0]) + int(array[y][x][1])
                       + int(array[y][x][2])) / 3
            array[y][x][0] = np.uint8(gray)
            array[y][x][1] = np.uint8(gray)
            array[y][x][2] = np.uint8(gray)
    print(f"the shape of image is : {array.shape}")
    print(array[0])
    plt.imshow(array)
    plt.show()
    return array

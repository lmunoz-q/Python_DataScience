from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def ft_zoom(path: str) -> np.ndarray:
    """
    Extracts a 400x400 square from the red channel of an image

    Parameters
    ----------
    path: str
        Path to the image file.

    Returns
    -------
    np.ndarray
        Zoomed region of the image with shape (400, 400, 1).
    """
    img_array = ft_load(path)

    if img_array is not None:
        channel = img_array[:, :, 0]
        zoom = channel[100:500, 450:850]
        zoom = np.array(zoom)
        if zoom.ndim == 2:
            zoom = np.expand_dims(zoom, axis=-1)
    return zoom


def ft_print_shape(img: np.ndarray) -> None:
    """
    Display the first and last 3 pixels from the first and last row of The
    image

    Parameters
    ----------
    img: np.ndarray
        Image array to preview.
    """
    print(img[0:1, 0:3])
    print("   ...")
    print(img[-1:, -3:])


def ft_rotate(img: np.ndarray) -> None:
    """
    Rotates a grayscale image by transposing it (90 degrees of rotation)

    Parameters
    ----------
    img: np.ndarray
        Input image shape (H, W, 1).
    """
    if isinstance(img, np.ndarray):
        print(f"The shape of image is: {img.shape}")
        ft_print_shape(img)
        img2d = img[:, :, 0]
        rows = len(img2d)
        cols = len(img2d[0])
        transposed = []
        for j in range(cols):
            new_row = []
            for i in range(rows):
                new_row.append(img2d[i][j])
            transposed.append(new_row)

        transposed = np.array(transposed)
        transposed = np.expand_dims(transposed, axis=-1)
        print(f"New shape after Transpose: {transposed.shape}")
        ft_print_shape(transposed)
        plt.imshow(transposed, cmap="gray")
        plt.show()


def main():
    img = ft_zoom("animal.jpeg")
    ft_rotate(img)


if __name__ == "__main__":
    main()

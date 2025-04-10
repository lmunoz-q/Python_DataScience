from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray | None:
    """
    Load an image file and return its content as a NumPy array.

    Parameters
    ----------
    path : str
        Path to the image file (JPEG or JPG).

    Returns
    -------
    np.ndarray | None
        The image converted into a NumPy array, or None if an error occurred.

    Raises
    ------
    ValueError
        If the image format is not JPEG or JPG.

    Notes
    -----
    The function also prints the shape of the image if loading is successful.
    """
    try:
        img = Image.open(path)
        if img.format not in ["JPEG", "JPG"]:
            raise ValueError("Error: Only JPG and JPEG are allowed")
        img_array = np.array(img)
        print(f"The shape of image is: {img_array.shape}")
        return img_array

    except Exception as e:
        print(f"Error: {e}")

    return None

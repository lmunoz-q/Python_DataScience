from PIL import Image
import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    cols = len(family[0])
    for i in family:
        if not isinstance(i, list):
            raise AssertionError("'family' must be a array2D")
        for x in i:
            if not isinstance(x, (int | float)):
                raise AssertionError("array2D must contain integers or floats")
        if cols != len(i):
            raise AssertionError("List must contain lines with columns equal")

    sFamily = family[start:end]

    return sFamily


def ft_load(path: str):
    try:
        img = Image.open(path)
        if img.format not in ["JPEG", "JPG"]:
            raise ValueError("Error: Only JPG and JPEG are allowed")
        img_array = np.array(img)
        print(f"The shape of image is: {img_array.shape}")
        return img_array[0]

    except Exception as e:
        print(f"Error: {e}")

    return None

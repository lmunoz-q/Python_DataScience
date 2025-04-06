from PIL import Image
import numpy as np


def ft_load(path: str):
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

from PIL import Image
import numpy as np


def ft_load(path: str) -> list:
    if not path.lower().endswith((".jpg", ".jpeg")):
        raise ValueError("File must be .jpg or .jpeg")


    try:
        image = Image.open(path)
    except IOError:
        raise IOError("Impossible to open file, make sure it's a .jpg or .jpeg valid")


    ret = np.array(image)
    return ret

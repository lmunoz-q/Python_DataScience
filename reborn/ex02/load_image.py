from PIL import Image

import matplotlib.pyplot as plt
import numpy as np

def ft_load(path: str):
    img = Image.open(path)
    img_array = np.array(img)
    print(f"The shape if image is: {img_array.shape}")

    return img_array

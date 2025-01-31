from PIL import Image
import numpy as np

def ft_load(path: str):
    img = Image.open("landscape.jpg")
    img_array = np.array(img)
    print(img_array.shape)

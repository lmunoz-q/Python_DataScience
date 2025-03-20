from load_image import ft_load
from PIL import Image
import numpy as np

img_array = ft_load("animal.jpeg")

if img_array is not None:
    img = Image.fromarray(np.array(ft_load))

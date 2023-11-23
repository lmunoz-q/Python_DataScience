from PIL import Image
import numpy as np

image = Image.open("animal.jpeg")

print(f"the shape of image is: {image.size[1]} x {image.size[0]}, {len(image.getbands())} channels")

image_array = np.array(image)

print(image_array)

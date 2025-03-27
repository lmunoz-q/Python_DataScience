from load_image import ft_load
from array2D import slice_me
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np



pathImg = "animal.jpeg"
#print(ft_load(pathImg))

img = Image.open(pathImg)
img_array = np.array(img)
print(img_array)

plt.imshow(img)
plt.show()

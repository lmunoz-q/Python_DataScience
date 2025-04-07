from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load, slice_me


pathImg = "animal.jpeg"
img_array = ft_load(pathImg)

if img_array is not None:
    print(img_array)

    img = Image.open(pathImg)
    img_array_full = np.array(img)

    channel = img_array_full[:, :, 0]
    z_image = slice_me(channel.tolist(), 100, 500)
    z_image = [row[450:850] for row in z_image]
    z_image = np.array(z_image)
    if z_image.ndim == 2:
        z_image = np.expand_dims(z_image, axis=-1)
    print(f"New shape after slicing: {z_image.shape}")
    print(z_image)

    plt.imshow(z_image, cmap="gray")
    plt.show()

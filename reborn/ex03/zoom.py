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
    z_image = slice_me(channel.tolist(), 0, 400)
    z_image = [row[:400] for row in z_image]
    print(f"New shape after slicing: ({len(z_image)}, {len(z_image[0])})")
    print(np.array(channel)[0])

    plt.imshow(z_image, cmap="gray")
    plt.show()

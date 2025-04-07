import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load


pathImg = "animal.jpeg"
img_array = ft_load(pathImg)

if img_array is not None:
    channel = img_array[:, :, 0]
    zoom = channel[100:500, 450:850]
    zoom = np.array(zoom)
    if zoom.ndim == 2:
        zoom = np.expand_dims(zoom, axis=-1)
    print(f"New shape after slicing: {zoom.shape}")
    print(zoom[0:1, 0:3])
    print("   ...")
    print(zoom[-1:, -3:])

    plt.imshow(zoom, cmap="gray")
    plt.show()

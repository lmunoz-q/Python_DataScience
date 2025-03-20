from load_image import ft_load
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


def on_zoom(event, img_array):
    current_xlim = plt.gca().get_xlim()
    current_ylim = plt.gca().get_ylim()

    if current_xlim != on_zoom.prev_xlim or current_ylim != on_zoom.prev_ylim:
        y_min, y_max = current_ylim
        y_min_idx = int(np.floor(y_min))
        y_max_idx = int(np.floor(y_max))
        print(f"New shape after slicing: {img_array[y_min_idx]}")
        on_zoom.prev_xlim = current_xlim
        on_zoom.prev_ylim = current_ylim


on_zoom.prev_xlim = None
on_zoom.prev_ylim = None

pathImg = "animal.jpeg"
print(ft_load(pathImg))

#img = np.asarray(Image.open(pathImg))
img = Image.open(pathImg)
img_array = np.array(img)

plt.imshow(img)

plt.gcf().canvas.mpl_connect('draw_event', lambda event: on_zoom(event, img_array))


plt.show()

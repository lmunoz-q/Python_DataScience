from load_image import ft_load
import matplotlib.pyplot as plt

new_img_array = None


def on_click(event):
    global new_img_array
    if new_img_array is not None:
        print(f"The new shape of image is: {new_img_array.shape}")
    else:
        print("No image data available")

    new_img_array = img_array
    print(new_img_array)


pathImg = "animal.jpeg"
img_array = ft_load(pathImg)

if img_array is not None:
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.imshow(img_array)
    fig.canvas.mpl_connect('button_release_event', on_click)
    plt.show(block=True)

from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def ft_zoom(path: str) -> np.ndarray:
    img_array = ft_load(path)

    if img_array is not None:
        channel = img_array[:, :, 0]
        zoom = channel[100:500, 450:850]
        zoom = np.array(zoom)
        if zoom.ndim == 2:
            zoom = np.expand_dims(zoom, axis=-1)

    return zoom


def ft_rotate(img: np.ndarray) -> None:
    if isinstance(img, np.ndarray):
        print(f"The shape if image is: {img.shape}")
        print(img[0:1, 0:3])
        print("   ...")
        print(img[-1:, -3:])
        transpose[i][j] = img[j][i]
        print(f"New shape after Transpose: {img.shape}")
        plt.imshow(img, cmap="gray")
        plt.show()


def main():
    path = "animal.jpeg"
    img = ft_zoom(path)
    ft_rotate(img)


if __name__ == "__main__":
    main()

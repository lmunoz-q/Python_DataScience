import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def main():
	try:
		# Load the image
		img = Image.open("animal.jpeg")
		img_array = np.array(img)

		# Print image information
		print(f"The shape of image is: {img_array.shape}")
		print(f"Pixel content of the image:\n{img_array}")

		# Display the image
		plt.imshow(img_array)
		plt.title('Sexy Raccoon')
		plt.axis('on')  # Display axes
		plt.show()

	except FileNotFoundError:
		print("Error: The file 'animal.jpeg' was not found.")
	except Exception as e:
		print(f"An error occurred: {e}")


if __name__ == "__main__":
	main()
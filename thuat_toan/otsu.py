import cv2
import numpy as np
import matplotlib.pyplot as plt

def otsu_algorithm(image_path):
    # Read the image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Check if the image is valid
    if image is None:
        print("Unable to read the image.")
        return

    # Apply Otsu's thresholding
    _, otsu_thresholded = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Display the results
    plt.figure(figsize=(10, 4))

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(otsu_thresholded, cmap='gray')
    plt.title("Otsu's Thresholding")

    plt.show()

# Image path
image_path = r'img\gojo.jpg'  # Change the path to your actual image

# Apply Otsu's algorithm
otsu_algorithm(image_path)

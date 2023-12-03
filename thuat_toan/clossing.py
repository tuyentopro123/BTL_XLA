import cv2
import numpy as np
import matplotlib.pyplot as plt

def closing_image(image_path, kernel_size=(5, 5)):
    # Read the grayscale image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Check if the image is valid
    if image is None:
        print("Unable to read the image.")
        return

    # Create a kernel for closing
    kernel = np.ones(kernel_size, np.uint8)

    # Perform closing
    closed_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

    # Display the results
    plt.figure(figsize=(10, 4))

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(closed_image, cmap='gray')
    plt.title('Closed Image')

    plt.show()

# Example usage
image_path = r'img\gojo.jpg'  # Change the path to your actual image
closing_image(image_path)

import cv2
import numpy as np
import matplotlib.pyplot as plt

def roberts_operator(image_path):
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Check if the image is valid
    if image is None:
        print("Unable to read the image.")
        return

    # Define Roberts kernels
    kernel_x = np.array([[1, 0], [0, -1]], dtype=np.float32)
    kernel_y = np.array([[0, 1], [-1, 0]], dtype=np.float32)

    # Apply convolution with Roberts kernels
    gradient_x = cv2.filter2D(image, cv2.CV_64F, kernel_x)
    gradient_y = cv2.filter2D(image, cv2.CV_64F, kernel_y)

    # Compute the magnitude of the gradient
    gradient_magnitude = np.sqrt(np.square(gradient_x) + np.square(gradient_y))

    # Display the results
    plt.figure(figsize=(10, 4))

    plt.subplot(1, 3, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')

    plt.subplot(1, 3, 2)
    plt.imshow(gradient_x, cmap='gray')
    plt.title('Roberts Operator (X-direction)')

    plt.subplot(1, 3, 3)
    plt.imshow(gradient_y, cmap='gray')
    plt.title('Roberts Operator (Y-direction)')

    plt.show()

# Image path
image_path = r'img\king_emperor.jpg' # Change the path to your actual image

# Apply Roberts Operator
roberts_operator(image_path)

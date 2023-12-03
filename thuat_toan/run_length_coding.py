import cv2
import numpy as np

def run_length_encode(image_path):
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Check if the image is valid
    if image is None:
        print("Unable to read the image.")
        return

    # Flatten the 2D array into a 1D sequence
    flat_sequence = image.flatten()

    # Initialize variables
    encoded_sequence = []
    current_count = 1

    # Run-Length Encode the 1D sequence
    for i in range(1, len(flat_sequence)):
        if flat_sequence[i] == flat_sequence[i - 1]:
            current_count += 1
        else:
            encoded_sequence.extend([flat_sequence[i - 1], current_count])
            current_count = 1

    # Append the last run
    encoded_sequence.extend([flat_sequence[-1], current_count])

    return encoded_sequence

# Example usage
image_path = r'img\gojo.jpg' # Change the path to your actual image
encoded_sequence = run_length_encode(image_path)

print("Encoded Sequence:", encoded_sequence)

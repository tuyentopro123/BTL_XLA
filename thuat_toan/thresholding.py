import cv2
import numpy as np
import matplotlib.pyplot as plt

def threshold_image(image_path, threshold_value):
    # Đọc ảnh từ đường dẫn
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Kiểm tra xem ảnh có tồn tại không
    if image is None:
        print("Không thể đọc được ảnh.")
        return

    # Thực hiện Thresholding
    _, thresholded_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)

    # Hiển thị ảnh gốc và ảnh đã Thresholding
    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Ảnh Gốc')

    plt.subplot(1, 2, 2)
    plt.imshow(thresholded_image, cmap='gray')
    plt.title(f'Thresholding với giá trị {threshold_value}')

    plt.show()

# Đường dẫn của ảnh và giá trị Threshold
image_path = r'img\gojo.jpg'  # Thay đổi đường dẫn của ảnh thực tế
threshold_value = 128  # Thay đổi giá trị Threshold nếu cần

# Gọi hàm để thực hiện Thresholding
threshold_image(image_path, threshold_value)

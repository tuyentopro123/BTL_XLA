import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def show_image():
    # Hiển thị hộp thoại chọn tệp và lấy đường dẫn tệp ảnh
    file_path = filedialog.askopenfilename(initialdir="/", title="Chọn ảnh", filetypes=(("JPEG files", "*.jpg"), ("all files", "*.*")))

    # Kiểm tra nếu người dùng đã chọn ảnh
    if file_path:
        # Tạo đối tượng Image từ đường dẫn
        img = Image.open(file_path)

        # Tạo đối tượng PhotoImage từ đối tượng Image
        img = ImageTk.PhotoImage(img)

        # Hiển thị ảnh trong cửa sổ Tkinter
        label = tk.Label(root, image=img)
        label.image = img  # Lưu tham chiếu để tránh bị giải phóng bộ nhớ
        label.pack()

# Tạo cửa sổ Tkinter
root = tk.Tk()
root.title("Hiển thị ảnh")

# Tạo nút bấm "Select" để chọn ảnh
select_button = tk.Button(root, text="Select", command=show_image)
select_button.pack()

# Khởi chạy vòng lặp mainloop của Tkinter
root.mainloop()

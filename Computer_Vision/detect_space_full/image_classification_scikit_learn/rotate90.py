from PIL import Image
import os

# Đường dẫn đến thư mục chứa ảnh
folder_path = "C:\\Users\\Admin\\Documents\\GitHub\\Smart_parking_car_computer_vision\\Detect_vitri\\image_classification_scikit_learn\\data\\empty"

# Lấy danh sách tệp tin trong thư mục
file_list = os.listdir(folder_path)

# Lặp qua từng tệp tin
for file_name in file_list:
    # Kiểm tra định dạng tệp tin
    if file_name.endswith(".png") or file_name.endswith(".jpg"):
        # Đường dẫn đến tệp tin ảnh
        image_path = os.path.join(folder_path, file_name)

        # Đọc ảnh
        image = Image.open(image_path)

        # Xoay ảnh 90 độ theo chiều kim đồng hồ
        rotated_image = image.rotate(90, expand=True)

        # Lưu ảnh đã xoay vào cùng thư mục với tên gốc
        rotated_image.save(image_path)

        print(f"Đã xoay và ghi đè tệp tin: {file_name}")
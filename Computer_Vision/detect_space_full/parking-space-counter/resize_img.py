from PIL import Image

# Đường dẫn đến ảnh 1 và ảnh 2
path_to_image1 = "F:\Work\SPARC\Smart_parking_car_computer_vision\Detect_vitri\parking-space-counter\original.jpg"
path_to_image2 = "f:\Work\SPARC\Smart_parking_car_computer_vision\Detect_vitri\parking-space-counter\mask_hust_c7.png"

# Mở ảnh 1 và lấy kích thước
image1 = Image.open(path_to_image1)
width1, height1 = image1.size

# Mở ảnh 2 và thay đổi kích thước
image2 = Image.open(path_to_image2)
resized_image2 = image2.resize((width1, height1))

# Lưu ảnh 2 đã chỉnh kích thước
resized_image2.save("mask_hust_c7.png")
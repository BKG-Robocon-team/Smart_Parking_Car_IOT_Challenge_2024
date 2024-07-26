import os
import torch
import torch.nn as nn
from skimage.transform import resize
import numpy as np
import cv2

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

EMPTY = True
NOT_EMPTY = False

# Định nghĩa mô hình mạng nơ-ron (phải khớp với kiến trúc mô hình đã huấn luyện)
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)
        self.fc1 = nn.Linear(32 * 7 * 7, 128)
        self.fc2 = nn.Linear(128, 2)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.pool(self.relu(self.conv1(x)))
        x = x.view(-1, 32 * 7 * 7)
        x = self.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Tải mô hình
MODEL_PATH = "model.pth"
model = SimpleCNN()
model.load_state_dict(torch.load(MODEL_PATH))
model.eval()  # Đặt mô hình ở chế độ đánh giá

def preprocess_image(image):
    """ Tiền xử lý hình ảnh cho mô hình """
    img_resized = resize(image, (15, 15), anti_aliasing=True)
    img_resized = np.expand_dims(img_resized, axis=0)  # Thêm chiều batch
    img_resized = np.expand_dims(img_resized, axis=0)  # Thêm chiều kênh
    img_resized = torch.tensor(img_resized, dtype=torch.float32)
    img_resized = (img_resized - 0.5) / 0.5  # Chuẩn hóa về khoảng [-1, 1]
    return img_resized

def empty_or_not(spot_bgr):
    spot_bgr_gray = cv2.cvtColor(spot_bgr, cv2.COLOR_BGR2GRAY)
    img_preprocessed = preprocess_image(spot_bgr_gray)
    
    with torch.no_grad():
        output = model(img_preprocessed)
        _, predicted = torch.max(output.data, 1)
    
    if predicted.item() == 0:
        return EMPTY
    else:
        return NOT_EMPTY

def get_parking_spots_bboxes(connected_components):
    (totalLabels, label_ids, values, centroid) = connected_components

    slots = []
    coef = 1
    for i in range(1, totalLabels):
        # Trích xuất tọa độ
        x1 = int(values[i, cv2.CC_STAT_LEFT] * coef)
        y1 = int(values[i, cv2.CC_STAT_TOP] * coef)
        w = int(values[i, cv2.CC_STAT_WIDTH] * coef)
        h = int(values[i, cv2.CC_STAT_HEIGHT] * coef)
        slots.append([x1, y1, w, h])

    return slots

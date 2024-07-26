import os
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import transforms, datasets
from torch.utils.data import DataLoader, Dataset, random_split
from sklearn.metrics import accuracy_score
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.transform import resize

# Custom Dataset class
class ImageDataset(Dataset):
    def __init__(self, data_dir, transform=None):
        self.data_dir = data_dir
        self.transform = transform
        self.categories = ['empty', 'not_empty']
        self.data = []
        self.labels = []
        for category_idx, category in enumerate(self.categories):
            category_path = os.path.join(data_dir, category)
            for file in os.listdir(category_path):
                img_path = os.path.join(category_path, file)
                self.data.append(img_path)
                self.labels.append(category_idx)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        img_path = self.data[idx]
        label = self.labels[idx]
        image = imread(img_path)
        image = rgb2gray(image)  # Chuyển đổi từ RGB sang ảnh xám
        image = resize(image, (15, 15), anti_aliasing=True)
        image = image.astype(np.float32)  # Chuyển đổi thành kiểu float32
        if self.transform:
            image = self.transform(image)
        return image, label

# Data transformations
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

# Prepare dataset
input_dir = 'C:/Users/DUYEN/OneDrive/Documents/GitHub/Smart_parking_car_computer_vision/Detect_vitri/parking-space-counter/data'
dataset = ImageDataset(input_dir, transform=transform)

# Train/test split
train_size = int(0.8 * len(dataset))
test_size = len(dataset) - train_size
train_dataset, test_dataset = random_split(dataset, [train_size, test_size])

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)

# Define the neural network model
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

# Initialize model, loss function, and optimizer
model = SimpleCNN()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training the model
num_epochs = 100
model.train()
for epoch in range(num_epochs):
    running_loss = 0.0
    for images, labels in train_loader:
        images = images.float()  # Chuyển đổi kiểu dữ liệu của hình ảnh thành float32
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        running_loss += loss.item()
    print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {running_loss/len(train_loader)}")

# Testing the model
model.eval()
all_labels = []
all_predictions = []
with torch.no_grad():
    for images, labels in test_loader:
        images = images.float()  # Chuyển đổi kiểu dữ liệu của hình ảnh thành float32
        outputs = model(images)
        _, predicted = torch.max(outputs.data, 1)
        all_labels.extend(labels.numpy())
        all_predictions.extend(predicted.numpy())

accuracy = accuracy_score(all_labels, all_predictions)
print(f'{accuracy * 100}% of samples were correctly classified')

# Save the model
torch.save(model.state_dict(), 'model.pth')

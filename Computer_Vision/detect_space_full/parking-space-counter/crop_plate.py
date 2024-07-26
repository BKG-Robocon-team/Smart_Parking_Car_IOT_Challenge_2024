import os
import cv2
import matplotlib.pyplot as plt

output_dir = 'image_classification_scikit_learn/data/'
mask_path = 'parking-space-counter/Mask_final.jpg'
original_image_dir = 'image_classification_scikit_learn/data/original_images'

mask = cv2.imread(mask_path, 0)

for original_image in os.listdir(original_image_dir):

    if not os.path.isfile(os.path.join(original_image_dir, original_image)):
        continue
    image_path = os.path.join(original_image_dir, original_image)
    image = cv2.imread(image_path)

    if image is None:
        print(f"Khong load duoc anh {original_image}.")
        continue

    # Cat anh
    analysis = cv2.connectedComponentsWithStats(mask, 4, cv2.CV_32S)
    (totalLabels, labels_ids, values, centroids) = analysis

    for i in range(1, totalLabels):
        
        x1 = values[i, cv2.CC_STAT_LEFT]
        y1 = values[i, cv2.CC_STAT_TOP]
        w = values[i, cv2.CC_STAT_WIDTH]
        h = values[i, cv2.CC_STAT_HEIGHT]

        slot_image = image[y1:y1+h, x1:x1+w]

        slot_output_path = os.path.join(output_dir, f'{os.path.splitext(original_image)[0]}_slot{i}.jpg')

        cv2.imwrite(slot_output_path, slot_image)

        plt.imshow(cv2.cvtColor(slot_image, cv2.COLOR_BGR2RGB))
        plt.title(f'{original_image} - Slot {i}')
        plt.show


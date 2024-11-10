import os
import random
import shutil

# Define paths to annotation and image folders
annotation_folder = 'defect_img/yolo_anno'
image_folder = 'defect_img/cameraPers'

# Create directories for training and validation data
train_annotation_folder = 'defect_img/yolo_dataset/labels/train'
train_image_folder = 'defect_img/yolo_dataset/images/train'
val_annotation_folder = 'defect_img/yolo_dataset/labels/val'
val_image_folder = 'defect_img/yolo_dataset/images/val'

os.makedirs(train_annotation_folder, exist_ok=True)
os.makedirs(train_image_folder, exist_ok=True)
os.makedirs(val_annotation_folder, exist_ok=True)
os.makedirs(val_image_folder, exist_ok=True)

# List files in annotation and image folders
annotations = os.listdir(annotation_folder)
images = os.listdir(image_folder)

# Shuffle the lists to ensure random splitting
random.shuffle(annotations)
random.shuffle(images)

# Calculate the number of files for training and validation
total_files = len(annotations)
train_size = int(0.8 * total_files)

# Split the files into training and validation sets
train_annotations = annotations[:train_size]
val_annotations = annotations[train_size:]
train_images = [annotation.replace('.txt', '.jpg') for annotation in train_annotations]
val_images = [annotation.replace('.txt', '.jpg') for annotation in val_annotations]

# Move annotation files and images to their respective folders
for annotation, image in zip(train_annotations, train_images):
    shutil.copy(os.path.join(annotation_folder, annotation), train_annotation_folder)
    shutil.copy(os.path.join(image_folder, image), train_image_folder)

for annotation, image in zip(val_annotations, val_images):
    shutil.copy(os.path.join(annotation_folder, annotation), val_annotation_folder)
    shutil.copy(os.path.join(image_folder, image), val_image_folder)

print("Data splitting completed successfully.")

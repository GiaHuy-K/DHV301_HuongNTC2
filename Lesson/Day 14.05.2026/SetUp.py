import kagglehub
import os
import shutil

# == Path setup ==
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_DIR = os.path.join(BASE_DIR, "dataset")

if not os.path.exists(DATASET_DIR):
    os.makedirs(DATASET_DIR)

# == Download dataset ==
temp_path = kagglehub.dataset_download("boss0ayush/salary-survey-data")

print("Đã tải về cache tại:", temp_path)

for filename in os.listdir(temp_path):
    source = os.path.join(temp_path, filename)
    destination = os.path.join(DATASET_DIR, filename)
    shutil.copy(source, destination) 

print(f"Dataset đã được đưa về: {DATASET_DIR}")
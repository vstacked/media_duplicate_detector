import os
import random

folder_path = r'D:/assets'  # Replace with the actual folder path

image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.endswith(('.jpg', '.jpeg', '.png'))]

for filename in image_files:
    extension = os.path.splitext(filename)[1]  # Get the file extension
    random_name = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=10))  # Generate a random name of length 10
    new_filename = random_name + extension
    old_path = os.path.join(folder_path, filename)
    new_path = os.path.join(folder_path, new_filename)
    os.rename(old_path, new_path)

import os
import shutil
from PIL import Image
import imagehash
from move import move_single_file_folders
from delete import delete_empty_folders

def get_image_hash(image_path):
    img = Image.open(image_path)
    return imagehash.phash(img)

def group_images_by_hash(target_folder):
    # Create a dictionary to store image hashes and corresponding image paths
    image_groups = {}

    # Loop through all files in the target folder
    for filename in os.listdir(target_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            image_path = os.path.join(target_folder, filename)
            image_hash = get_image_hash(image_path)

            # Add the image path to the corresponding image group based on the hash
            if image_hash in image_groups:
                image_groups[image_hash].append(image_path)
            else:
                image_groups[image_hash] = [image_path]

    # Create folders for each image group and move the images
    for group_id, image_paths in image_groups.items():
        group_folder = os.path.join(target_folder, f"group_{group_id}")
        os.makedirs(group_folder, exist_ok=True)

        for image_path in image_paths:
            shutil.move(image_path, group_folder)

if __name__ == "__main__":
    target_folder = "D:/Media"

    group_images_by_hash(target_folder)

    move_single_file_folders(target_folder, target_folder)

    delete_empty_folders(target_folder)

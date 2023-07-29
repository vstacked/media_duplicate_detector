from PIL import Image
import os
import shutil
import hashlib

def get_image_hash(image_path):
    with open(image_path, 'rb') as f:
        image_hash = hashlib.md5(f.read()).hexdigest()
    return image_hash

def move_duplicates_to_folder(src_folder, dest_folder):
    image_hashes = {}
    
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(root, file)
                image_hash = get_image_hash(image_path)
                
                if image_hash in image_hashes:
                    duplicate_folder = os.path.join(dest_folder, image_hashes[image_hash])
                    if not os.path.exists(duplicate_folder):
                        os.makedirs(duplicate_folder)
                    shutil.move(image_path, os.path.join(duplicate_folder, file))
                else:
                    image_hashes[image_hash] = file

if __name__ == "__main__":
    source_folder = "D:/Media"  # Replace this with the path to your source folder
    destination_folder = "D:/Media_new"  # Replace this with the path to the destination folder
    
    move_duplicates_to_folder(source_folder, destination_folder)

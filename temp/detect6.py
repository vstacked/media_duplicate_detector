from PIL import Image
import imagehash
import os
import shutil

def compute_image_hash(image_path):
    img = Image.open(image_path)
    hash = imagehash.average_hash(img)
    return str(hash)

def group_similar_images(target_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    hash_to_paths = {}

    for root, dirs, files in os.walk(target_folder):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(root, file)
                img_hash = compute_image_hash(image_path)
                if img_hash in hash_to_paths:
                    hash_to_paths[img_hash].append(image_path)
                else:
                    hash_to_paths[img_hash] = [image_path]

    for images_list in hash_to_paths.values():
        if len(images_list) > 1:
            for image_path in images_list:
                filename = os.path.basename(image_path)
                new_path = os.path.join(output_folder, filename)
                shutil.copy(image_path, new_path)

if __name__ == "__main__":
    target_folder = "D:/Media"
    output_folder = "D:/Media_new"

    group_similar_images(target_folder, output_folder)

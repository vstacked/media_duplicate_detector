from PIL import Image
import os
import shutil

def dhash(image_path, hash_size=8):
    image = Image.open(image_path).convert('L').resize((hash_size + 1, hash_size))
    pixels = list(image.getdata())

    diff = [pixels[i * hash_size + j] > pixels[i * hash_size + j + 1] for i in range(hash_size) for j in range(hash_size - 1)]

    decimal_hash = sum([2 ** i for i, v in enumerate(diff) if v])
    hexadecimal_hash = hex(decimal_hash)[2:].rjust(hash_size // 4, '0')
    return hexadecimal_hash

def move_duplicates_to_folder(src_folder, dest_folder):
    image_hashes = {}

    for root, dirs, files in os.walk(src_folder):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(root, file)

                # Calculate the dHash of the image
                image_hash = dhash(image_path)

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

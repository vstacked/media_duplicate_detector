import os
from PIL import Image
import imagehash

def find_duplicate_images(folder_path):
    image_hashes = {}
    duplicates = []

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Check if the file is an image
        try:
            with Image.open(file_path) as img:
                img_hash = imagehash.average_hash(img)

                # Check if the image hash is already in the dictionary
                if img_hash in image_hashes:
                    duplicates.append((filename, image_hashes[img_hash]))
                else:
                    image_hashes[img_hash] = filename
        except (OSError, IOError):
            # Skip non-image files
            continue

    return duplicates

if __name__ == "__main__":
    folder_path = "D:/Media"  # Replace this with the path to your folder

    duplicate_pairs = find_duplicate_images(folder_path)

    if not duplicate_pairs:
        print("No duplicate images found.")
    else:
        print("Duplicate images found:")
        for file1, file2 in duplicate_pairs:
            print(f"{file1} is a duplicate of {file2}.")

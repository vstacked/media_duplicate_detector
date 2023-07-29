from PIL import Image
import os
import shutil

def dhash(image_path, hash_size=8):
    # Resize the image and convert it to grayscale
    image = Image.open(image_path).convert('L').resize((hash_size + 1, hash_size))
    pixels = list(image.getdata())

    # Calculate the difference between adjacent pixels
    diff = [pixels[i * hash_size + j] > pixels[i * hash_size + j + 1] for i in range(hash_size) for j in range(hash_size)]
    
    # Convert the binary difference to a hexadecimal hash
    return ''.join(['{:x}'.format(int(''.join([str(pixel) for pixel in diff[i:i+4]]), 2)) for i in range(0, len(diff), 4)])

def move_duplicates_to_folder(src_folder, dest_folder):
    image_hashes = {}
    
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(root, file)
                
                # Calculate the dHash or pHash of the image
                image_hash = dhash(image_path)  # Use dhash() for dHash or phash() for pHash
                
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

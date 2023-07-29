import os
import shutil
from PIL import Image
import imagehash

def move_duplicates(source_folder, target_folder, similarity_threshold=5):
    # Create the target folder if it doesn't exist
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    
    # Dictionary to store image hashes and their respective filenames
    image_hashes = {}

    # Loop through all files in the source folder
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        # Check if the file is an image
        try:
            image = Image.open(file_path)
        except:
            continue

        # Calculate the hash of the image
        hash_value = imagehash.average_hash(image)

        # Check if the hash already exists in the dictionary
        if hash_value in image_hashes:
            # If a similar image is found, move it to the target folder
            shutil.move(file_path, os.path.join(target_folder, filename))
        else:
            # If not, add the hash and filename to the dictionary
            image_hashes[hash_value] = filename

if __name__ == "__main__":
    source_folder = "D:/Media"
    target_folder = "D:/Media_new"
    similarity_threshold = 5  # Adjust this value to set the similarity threshold (lower value = stricter matching)

    move_duplicates(source_folder, target_folder, similarity_threshold)

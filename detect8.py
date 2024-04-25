import os
import shutil
from PIL import Image
import imagehash
import hashlib
from move import move_single_file_folders
from delete import delete_empty_folders
from videohash import VideoHash

def hash_file(filename):
   """"This function returns the SHA-256 hash
   of the file passed into it"""

   # make a hash object
   h = hashlib.sha256()

   # open file for reading in binary mode
   with open(filename,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()

def get_image_hash(image_path):
    img = Image.open(image_path)
    return imagehash.phash(img)

def group_files_by_hash(target_folder, selected_extensions):
    # Create a dictionary to store file hashes and corresponding file paths
    file_groups = {}

    image_extensions = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".tiff", ".psd", ".bmp"}
    video_extensions = {".mp4", ".mkv", ".mov", ".avi", ".wmv", ".flv"}

    # Loop through all files in the target folder
    for filename in os.listdir(target_folder):
        if os.path.isfile(os.path.join(target_folder, filename)) and filename.lower().endswith(selected_extensions):
            filename_lower = filename.lower()
            if filename_lower.endswith(tuple(image_extensions)):
                file_path = os.path.join(target_folder, filename)
                image_hash = get_image_hash(file_path)
                data = str(image_hash)

                # Add the image path to the corresponding file group based on the hash
                if data in file_groups:
                    file_groups[data].append(file_path)
                else:
                    file_groups[data] = [file_path]
            elif filename_lower.endswith(tuple(video_extensions)):
                video_path = os.path.join(target_folder, filename)
                video_hash = VideoHash(path=video_path)
                data = str(video_hash)

                # Add the video path to the corresponding file group based on the hash
                if data in file_groups:
                    file_groups[data].append(video_path)
                else:
                    file_groups[data] = [video_path]
            else:
                file_path = os.path.join(target_folder, filename)
                file_hash = hash_file(file_path)
                data = str(file_hash)

                # Add the file path to the corresponding file group based on the hash
                if data in file_groups:
                    file_groups[data].append(file_path)
                else:
                    file_groups[data] = [file_path]

    # Create folders for each file group and move the files
    for group_id, file_paths in file_groups.items():
        parts = file_paths[0].split("\\")
        file_name = parts[-1]
        group_name = f"group_{file_name}"
        group_folder = os.path.join(target_folder, group_name)
        os.makedirs(group_folder, exist_ok=True)

        print(f"Created Group: {group_name}")

        for file_path in file_paths:
            parts = file_paths[0].split("\\")
            file_name = parts[-1]
            shutil.move(file_path, group_folder)
            print(f"Moved \"{file_name}\" to \"{group_name}\"")

def main(path, selected_extensions):
    target_folder = path

    try:
        group_files_by_hash(target_folder, selected_extensions)
    
        move_single_file_folders(target_folder)

        delete_empty_folders(target_folder)
    except OSError as e:
        print(f"Error: {e}")

    print("Completed.")

    return True
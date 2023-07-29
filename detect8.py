import os
import shutil
from PIL import Image
import imagehash
from move import move_single_file_folders
from delete import delete_empty_folders
from videohash import VideoHash

def get_image_hash(image_path):
    img = Image.open(image_path)
    return imagehash.phash(img)

def group_files_by_hash(target_folder):
    # Create a dictionary to store file hashes and corresponding file paths
    file_groups = {}

    # Loop through all files in the target folder
    for filename in os.listdir(target_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.gif', '.JPG')):
            file_path = os.path.join(target_folder, filename)
            image_hash = get_image_hash(file_path)
            data = str(image_hash)

            # Add the image path to the corresponding file group based on the hash
            if data in file_groups:
                file_groups[data].append(file_path)
            else:
                file_groups[data] = [file_path]
        elif filename.endswith(('.mp4', '.mkv', '.MP4')):
            video_path = os.path.join(target_folder, filename)
            video_hash = VideoHash(path=video_path)
            data = str(video_hash)

            # Add the video path to the corresponding file group based on the hash
            if data in file_groups:
                file_groups[data].append(video_path)
            else:
                file_groups[data] = [video_path]

    # Create folders for each file group and move the files
    for group_id, file_paths in file_groups.items():
        group_folder = os.path.join(target_folder, f"group_{group_id}")
        os.makedirs(group_folder, exist_ok=True)

        for file_path in file_paths:
            shutil.move(file_path, group_folder)

if __name__ == "__main__":
    target_folder = "D:/Media"

    group_files_by_hash(target_folder)

    move_single_file_folders(target_folder, target_folder)

    delete_empty_folders(target_folder)

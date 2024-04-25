import os
import re

def delete_empty_folders(target_folder):
    for root, dirs, files in os.walk(target_folder, topdown=False):
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            pattern = r"group\_"  # raw string for verbatim interpretation
            match = re.search(pattern, str(folder_path))
            if not os.listdir(folder_path) and bool(match):
                try:
                    os.rmdir(folder_path)
                    print(f"Deleted empty folder: {folder_path}")
                except OSError as e:
                    print(f"Error while deleting folder: {folder_path}/n{e}")
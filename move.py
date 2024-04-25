import os
import shutil
import re

def move_single_file_folders(target_folder):
    for root, dirs, files in os.walk(target_folder):
        pattern = r"group\_"  # raw string for verbatim interpretation
        match = re.search(pattern, str(root))
        # Check if the current directory contains exactly one file
        if len(files) == 1 and not dirs and bool(match):
            file_to_move = os.path.join(root, files[0])
            # Move the file to the destination folder
            shutil.move(file_to_move, target_folder)
            print(f"Moved {files[0]} to {target_folder}")
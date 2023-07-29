import os
import shutil
# from temp.a import target_folder

def move_single_file_folders(target_folder, destination_folder):
    for root, dirs, files in os.walk(target_folder):
        # Check if the current directory contains exactly one file
        if len(files) == 1 and not dirs:
            file_to_move = os.path.join(root, files[0])
            # Move the file to the destination folder
            shutil.move(file_to_move, destination_folder)
            print(f"Moved {files[0]} to {destination_folder}")

# if __name__ == "__main__":
    # move_single_file_folders(target_folder, target_folder)

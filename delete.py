import os
# from temp.a import target_folder

def delete_empty_folders(target_folder):
    for root, dirs, files in os.walk(target_folder, topdown=False):
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            if not os.listdir(folder_path):
                try:
                    os.rmdir(folder_path)
                    print(f"Deleted empty folder: {folder_path}")
                except OSError as e:
                    print(f"Error while deleting folder: {folder_path}/n{e}")

# if __name__ == "__main__":
#     delete_empty_folders(target_folder)

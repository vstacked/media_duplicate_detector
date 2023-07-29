import os

def add_custom_name_to_files(folder_path, custom_name):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    for filename in files:
        # Create the new filename by adding the custom name
        new_filename = filename + custom_name

        # Get the full path of the original and new files
        old_filepath = os.path.join(folder_path, filename)
        new_filepath = os.path.join(folder_path, new_filename)

        # Rename the file with the custom name
        os.rename(old_filepath, new_filepath)

if __name__ == "__main__":
    folder_path = "D:/Media"  # Replace this with the path to your folder
    custom_name = "new.jpg"  # Replace this with your desired custom name

    add_custom_name_to_files(folder_path, custom_name)

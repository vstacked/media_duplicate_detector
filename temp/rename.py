import os
import random
import string
# from temp.a import target_folder

def generate_random_string(length):
    # Generate a random string of alphanumeric characters
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))

def randomize_file_names(target_folder):
    for filename in os.listdir(target_folder):
        file_path = os.path.join(target_folder, filename)
        if os.path.isfile(file_path):
            # Get the file extension
            _, file_extension = os.path.splitext(filename)

            # Generate a random name for the file
            new_filename = generate_random_string(12) + file_extension

            # Rename the file
            os.rename(file_path, os.path.join(target_folder, new_filename))
            print(f"Renamed {filename} to {new_filename}")

# if __name__ == "__main__":
#     randomize_file_names(target_folder)

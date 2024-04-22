import os
import hashlib

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

def group_files_by_hash(target_folder):
    # Create a dictionary to store file hashes and corresponding file paths
    file_groups = {}

    # Loop through all files in the target folder
    for filename in os.listdir(target_folder):
        if filename.endswith(('.docx', '.pdf', '.pptx')):
            file_path = os.path.join(target_folder, filename)
            print(f"result: {filename} {hash_file(file_path)}")

def main(path):
    target_folder = path

    group_files_by_hash(target_folder)

    print("Completed.")

    return True
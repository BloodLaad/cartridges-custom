#!/usr/bin/python
import os
import shutil
import subprocess

def copy_all_files_and_directories(src_folder, dest_folder):
    # Create the destination folder if it doesn't exist
    if os.path.exists(dest_folder):
        shutil.rmtree(dest_folder)
        os.makedirs(dest_folder)
    else:
        os.makedirs(dest_folder)

    # Get the list of all files and directories in the source folder
    items = os.listdir(src_folder)

    # Copy each item to the destination folder
    for item in items:
        src_path = os.path.join(src_folder, item)
        dest_path = os.path.join(dest_folder, item)

        # Use shutil.copytree for directories and shutil.copy2 for files
        if os.path.isdir(src_path):
            shutil.copytree(src_path, dest_path, symlinks=True)
        else:
            if item == "install.py" or item == "PKGBUILD":
                continue
            else:
                shutil.copy2(src_path, dest_path)

    print(f"All files and directories from {src_folder} copied to {dest_folder}")

if __name__ == "__main__":
    # Set the source and destination folders
    copy_all_files_and_directories(".", "./src")
    # Makepkg
    process = subprocess.Popen('makepkg', shell=True)
    return_code = process.wait()
    if return_code == 0:
        print("completed successfully.")
    else:
        print(f"failed with return code {return_code}.")
    print("-"*20 +"\nUSER INTERVENTION REQUIRED\n" + "-"*20)
    input("To install the package, run 'makepkg -i' in this folder.\nOnce completed, press enter here: ")
    print("DONE!")
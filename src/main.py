import shutil
import os

from textnode import *
from htmlnode import *
from generatepage import generate_page


def main():
    init_public_dir()
    generate_page("content/index.md", "template.html", "public/index.html")
    
    
    
def init_public_dir():
    working_directory = os.getcwd()
    destination_path = os.path.join("", working_directory, "public")
    source_path= os.path.join("", working_directory, "static")
    print(destination_path)
    if os.path.exists(destination_path):
        content_files = os.listdir(destination_path)
        if content_files:
            shutil.rmtree(destination_path)
            os.mkdir(destination_path)
    else:
        os.mkdir(destination_path)
        
    copy_dir(source_path, destination_path)

def copy_dir(source_path, destination_path):
    if not os.path.exists(source_path) and not os.path.isdir(source_path):
        raise FileExistsError(f"Source directory - {source_path} - is not a directory")
    source_files = os.listdir(source_path)
    if not source_files:
        raise FileExistsError(f"Empty directory: {source_path}")
    
    for file in source_files:
        file_path = os.path.join("", source_path, file)
        
        if os.path.isdir(file_path):
            dir_destination = os.path.join("", destination_path, file)
            if not os.path.exists(dir_destination) or not os.path.isdir(dir_destination):
                os.mkdir(dir_destination)
            copy_dir(file_path, dir_destination)
            continue
        
        print(f"Copying file: {file}\nFrom {file_path} to {destination_path}")
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Incorrect path: {file}")
            continue
        if not os.path.isfile(file_path):
            raise FileExistsError(f"{file} is not a file")
            continue
        
        shutil.copy(file_path, destination_path)

if __name__ == "__main__":
    main()
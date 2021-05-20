import os
import sys
from os import path
import pathlib
import shutil

def main():
    if len(sys.argv) < 2:
        print('Please, inform the source directory')
        return

    destination_directory = "organize"

    source_directory = str(sys.argv[1]) + "/"

    if not os.path.isdir(source_directory):
        print('User\'s Downloads directory not found')
        return

    destination_path = source_directory + destination_directory + "/"
    destination_images_path = source_directory + destination_directory + "/images/"

    def create_directory(dir_path):
        if not path.exists(dir_path):
            try:
                os.mkdir(dir_path)
            except OSError:
                print('Error while trying to create %s directory' % dir_path)
            else:
                print("Directory %s created successfully" % dir_path)

    create_directory(destination_path)
    create_directory(destination_images_path)
    
    i = 0

    for filename in os.listdir(source_directory):
        file_extension = pathlib.Path(filename).suffix
        
        if file_extension == '.jpg' or file_extension == '.png':
            shutil.move(source_directory + filename, destination_images_path + filename)
            continue

        ext_dir = file_extension.replace('.', '')
        final_dir = destination_path + ext_dir + '/'

        create_directory(final_dir)

        if not os.path.isdir(source_directory  + filename):
            shutil.move(source_directory  + filename, final_dir + filename)

        i += 1

    print("Finish organizing files :)")

if __name__ == '__main__':
    main()

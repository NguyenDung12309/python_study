import os

import pathlib

import zipfile


def zip_creator(file_paths, dest_dir):
    format_dest_dir = pathlib.Path(dest_dir) / 'compress.zip'
    with zipfile.ZipFile(format_dest_dir, 'w') as archive:
        list_file_paths = file_paths.split(';')
        print(list_file_paths)
        for path in list_file_paths:
            archive.write(path, arcname=os.path.basename(path))

if __name__ == '__main__':
    zip_creator('test.txt;test2.txt' , 'output')
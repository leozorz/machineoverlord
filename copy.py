import os
import shutil

def pendrive_copy (src='/Users/leonor/Documents/Origin', dest='/Users/leonor/Desktop/output_folder'):
        src_files = os.listdir(src)
        for file_name in src_files:
                full_file_name = os.path.join(src, file_name)
                if (os.path.isfile(full_file_name)):
                        shutil.copy(full_file_name, dest)

pendrive_copy()

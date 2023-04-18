import os
import shutil

from_dir=r"C:\Users\17034\Pictures\myimages"
to_dir=r"C:\Users\17034\Pictures\Saved Pictures"

list_of_files=os.listdir(from_dir)
# print(list_of_files)

for i in list_of_files:
    name,extension=os.path.splitext(i)
    print(extension)
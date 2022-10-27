# conding:utf-8

import os
from mp3tag.id3tag import id3tag
# from numpy import full

# Return the package version
def get_version(file_path):
    i3t = id3tag()
    i3t.tag_analyze(file_path)
    # print("mp3tag version is 0.0.2")

# Find mp3 file under specific folder and return id3 tag version
# 在指定的目录下查找 mp3 文件
def analyze_folder(mp3_folder_path = ''):
    mtr = id3tag()
    
    # print(mp3_folder_path)
    for parent, _, file_names in os.walk(mp3_folder_path):
        for file_name in file_names:
            if file_name.endswith('mp3'):
                full_file_name = os.path.join(parent, file_name)
                # print(full_file_name)

                # print(full_file_name)
                t_info  = mtr.tag_analyze(full_file_name)
                # t_info = mtr.get_tag(full_file_name)
                print(t_info)

# Get single mp3 file's tag info
# file_path can be a specific file name or a folder path
def get_tag(file_path, char_detect = False):
    i3t = id3tag()

    t_info = i3t.get_tag(file_path, char_detect)
    print(t_info)

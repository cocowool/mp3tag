import os
from mp3tag.id3tag import id3tag

# Return the package version
def get_version():
    print("mp3tag version is 0.0.1")

# Find mp3 file under specific folder
# 在指定的目录下查找 mp3 文件
def search_folder(mp3_folder_path = ''):
    mtr = id3tag()
    
    # print(mp3_folder_path)
    for parent, _, file_names in os.walk(mp3_folder_path):
        for file_name in file_names:
            if file_name.endswith('mp3'):
                full_file_name = os.path.join(parent, file_name)
                # print(full_file_name)

                t_info = mtr.get_tag(full_file_name)
                print(t_info)


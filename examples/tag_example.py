import sys
from tinytag import TinyTag
# from mp3tag.mp3tag import mp3tag

# 这里改为自己本机 pyID3 的存储目录
sys.path.append('/Users/shiqiang/Projects/mp3tag/src/')

for p in sys.path:
    print(p)

# import mp3tag as mpt
from mp3tag import mp3tag

# from mp3tag.mp3tag import id3tag
# import mp3tag as mpt
# import mp3tag as m3g

# music_path = '/Users/shiqiang/Downloads/old_mbp_files/OldMBP-Music/'
music_path = '/Users/shiqiang/Music/Music/Media.localized'

# mp3tag.get_version()
# mp3tag.search_folder(music_path)

file_path = '/Users/shiqiang/Downloads/old_mbp_files/OldMBP-Music/RADWIMPS (ラッドウィンプス)-針と棘.mp3'
mp3tag.get_tag(file_path)

mp3tag.get_version(file_path)

# tag = TinyTag.get(file_path)
# print("Result from tinytag : \n")
# print(tag)

# mpt = id3tag()
# # mpt.get_version()

# mp3tag.get_version()
mp3tag.search_folder(music_path)
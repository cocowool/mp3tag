import sys

# from mp3tag.mp3tag import mp3tag

# 这里改为自己本机 pyID3 的存储目录
# sys.path.append('/Users/shiqiang/Projects/mp3tag/src/mp3tag')

for p in sys.path:
    print(p)

from mp3tag.mp3tag import id3tag
# import mp3tag as mpt
# import mp3tag as m3g

music_path = '/Users/shiqiang/Downloads/old_mbp_files/OldMBP-Music/'

# mp3tag.get_version()
mpt = id3tag()
# mpt.get_version()
mpt.search_folder(music_path)

# mp3tag.get_version()
# mp3tag.search_folder(music_path)
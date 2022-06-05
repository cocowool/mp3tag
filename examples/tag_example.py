import sys

# from mp3tag.mp3tag import mp3tag

# 这里改为自己本机 pyID3 的存储目录
sys.path.append('/Users/shiqiang/Projects/mp3tag/mp3tag')

for p in sys.path:
    print(p)

import mp3tag as mpt
# import mp3tag.tag_reader
# import reader as mpr

# import pyid3
# mpt = mp3tag()
mpt.get_version()

import mp3tag
mpc = mp3tag()

# from pyID3 import tag
# import os

# print(sys.path)
# path = "/Users/rousseau/shiqiang/Music/iTunes/iTunes Media/Music"

# def findMp3(path):
#     files = os.listdir(path)
#     for f in files:
#         if( os.path.isdir(os.path.join(path,f)) ):
#             findMp3( os.path.join(path,f) )
#         else:
#             fh = open(os.path.join(path,f), "rb")
#             print(tag.parse(fh))

# # print(tag)

# findMp3(path)
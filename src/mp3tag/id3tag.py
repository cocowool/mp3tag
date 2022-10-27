# conding:utf-8

import os
import string
import base64

# from pyparsing import And
# import chardet

class id3tag():
    def __init__(self):
        pass
        # print("id3tag init.")

    # Analyze the file and which id3 version
    # Condition: 1. ID3v1 and ID3v2; 2. ID3v2 only; 3. ID3v1 only; 4. None;
    # Return { file_name: [ID3v2, ID3v1] }
    def tag_analyze(self, file_name):
        return_obj = {}
        return_obj[file_name] = []

        fh = open(file_name, "rb")
        head_bin = fh.read(10)

        fhex = open(file_name, "rb")
        hex_data = fhex.read().hex()
        # print(head_bin)

        if head_bin[0:3] == b'ID3':
            # print("ID3v2 found.")
            # print("Version: ID3v2." + str(int(hex_data[6:8])) )
            return_obj[file_name].append('ID3v2.' + str(int(hex_data[6:8])) )
            # print(int(hex_data[6:8]))
            # print(head_bin[4].decode('utf-8'))

        # Move pointer to end of file
        fh.seek(0, 2)
        if fh.tell() > 128:
            # Move pointer to 128 bytes position
            fh.seek(-128, 2)
            tag_data = fh.read()
            if tag_data[0:3] == b'TAG':
                # print("ID3v1 found.")
                # print("Version: ID3v1")
                return_obj[file_name].append('ID3v1')

        fh.close()
        fhex.close()

        return return_obj

    # Get Mp3 File Tag Information, return all by default
    def get_tag(self, file_name, char_detect_flag = False, version = 'both'):
        # print("Tag reader version is 0.0.1")
        return self.get_id3v1(file_name, char_detect_flag)

    # Get ID3v1 tag data
    # Format
    # { file_name: xxx, title: xxx, artis: xxx, album: xxx, year: xxx, comment: xxx, genre: x }
    # Exception { error : xxxx }
    def get_id3v1(self, file_name, char_detect_flag = False):
        # STRIP_CHARS = compat.b(string.whitespace) + b"\x00"
        # Strip empty characters
        STRIP_CHARS = b"\x00"

        try:
            fh = open(file_name, "rb")
            fh.seek(0, 2)

            if fh.tell() < 128:
                return { 'error' : 'No ID3v1 tag found.'}
                # print('Seems id3v1 version, does not support, exit!')
            
            fh.seek(-128,2)
            tag_data = fh.read()

            if(tag_data[0:3] != b'TAG'):
                return { 'error' : 'No ID3v1 tag found.'}

        except Exception as e:
            print(e)
            return "No file error !"

        tags = {}
        tags['file_name'] = file_name


        if char_detect_flag == True:
            char_detect = chardet.detect(tag_data[3:93])

        if char_detect_flag and char_detect['confidence'] > 0.9:

            tags['title'] = tag_data[3:33].strip(STRIP_CHARS)
            if len(tags['title']) > 0:
                tags['title'] = tags['title'].decode(char_detect['encoding'])
            else:
                tags['title'] = ''

            tags['artist'] = tag_data[33:63].strip(STRIP_CHARS)
            if len(tags['artist']) > 0:
                tags['artist'] = tags['artist'].decode(char_detect['encoding'])
            else:
                tags['artis'] = ''

            tags['album'] = tag_data[63:93].strip(STRIP_CHARS)
            if len(tags['album']) > 0:
                tags['album'] = tags['album'].decode(char_detect['encoding'])
            else:
                tags['album'] = 0

            tags['comment'] = tag_data[97:127].strip(STRIP_CHARS)
            if len(tags['comment']) > 0:
                tags['comment'] = tags['comment'].decode(char_detect['encoding'])
            else:
                tags['comment'] = ''
        else:
            tags['title'] = tag_data[3:33].strip(STRIP_CHARS)
            if len(tags['title']) > 0:
                tags['title'] = self.decodeData(tags['title'])
            else:
                tags['title'] = 0

            tags['artist'] = tag_data[33:63].strip(STRIP_CHARS)
            if len(tags['artist']) > 0:
                tags['artist'] = self.decodeData(tags['artist'])
            else:
                tags['artis'] = 0

            tags['album'] = tag_data[63:93].strip(STRIP_CHARS)
            if len(tags['album']):
                tags['album'] = self.decodeData(tags['album'])
            else:
                tags['album'] = ''

            tags['comment'] = tag_data[97:127].strip(STRIP_CHARS)
            if len(tags['comment']) > 0:
                tags['comment'] = self.decodeData(tags['comment'])
            else:
                tags['comment'] = ''

        tags['year'] = int(tag_data[93:97].strip(STRIP_CHARS))
        tags['genre'] = ord(tag_data[127:128])

        return tags

    # Remove ID3v1 Tag information
    def remove_id3v1(self):
        pass

    # Remove ID3v2 Tag information
    def remove_id3v2(self):
        pass

    # Detect the encoding and decode
    def decodeData(self, bin_seq):
        result = chardet.detect(bin_seq)
        if(result['confidence'] > 0.9):
            try:
                return bin_seq.decode(result['encoding'])
            except UnicodeDecodeError as e:
                print('Decode Failed : ' + str(e))
                return ''
        else:
            try:
                print(result)
                return bin_seq.decode('gbk')
            except UnicodeDecodeError as e:
                print('Decode Failed : ' + str(e))
                return ''

    def tag_id3v2():
        pass
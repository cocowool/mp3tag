# mp3tag

本 repo 提供一个支持读取、修改 mp3 标签信息的工具，关于 mp3 标签信息的内容，[使用Python读取Mp3的标签信息](http://www.edulinks.cn/2018/06/22/20180622-python-read-id3v1-tag/) 做了初步的介绍。

Tools for read and modify mp3 tag information, you can search wiki to know more about "Identity of MP3".

## 特性
* 支持读取某个文件夹下 mp3 文件的 idv3 信息
* 输出统一为 utf-8 编码

## Feature
* Read mp3 idv3 information under specific folder
* output attribute information in utf-8

## Requirement

* chardet 

## Usage

```python
from mp3tag import mp3tag

music_path = '/Users/shiqiang/Downloads/old_mbp_files/OldMBP-Music/'

mpt = mp3tag()
mpt.get_version()
mpt.analyze_folder(music_path)
```

Result

```sh
$ python3 examples/tag_example.py
{'title': None, 'artist': 'Pure Music', 'album': 'นลตไร๛ว๚', 'year': b'', 'comment': b'', 'genre': 0}
{'title': 'And One', 'artist': 'Linkin Park', 'album': 'Underground 1.0', 'year': b'', 'comment': b'', 'genre': 0}

```


## Reference
* [id3.org](https://id3.org/Home)
* [ATool](https://github.com/Am0xil/ATool)
* [使用Python读取Mp3的标签信息](http://www.edulinks.cn/2018/06/22/20180622-python-read-id3v1-tag/)
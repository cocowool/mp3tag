from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'MP3 tag information reader and writer.'
LONG_DESCRIPTION = 'MP3 contains many information about the music and stored in the tag. This package support read and write id3v2 tag to the mp3 file.'

setup(
    name='mp3tag',
    version=VERSION,
    author='Wang Shiqiang',
    author_email='cocowool@qq.com',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],

    keywords=['mp3','id3','id3v2'],
    classifiers=[]
)
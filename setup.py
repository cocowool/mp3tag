import setuptools
# from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'MP3 tag information reader and writer.'
LONG_DESCRIPTION = 'MP3 contains many information about the music and stored in the tag. This package support read and write id3v2 tag to the mp3 file.'

with open("README.md", "r", encoding="utf-8") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name='mp3tag',
    version=VERSION,
    author='Wang Shiqiang',
    author_email='cocowool@qq.com',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/cocowool/mp3tag",
    project_urls={
        "Bug Tracker":"https://github.com/cocowool/mp3tag/issues"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[],

    keywords=['mp3','id3','id3v2'],
    classifiers=[],
    python_requires=">=3.6"
)
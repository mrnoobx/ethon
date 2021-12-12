import re
import os
import setuptools

ver = 'v0.0.3.8'

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

name = "ethon"
author = "vasusen-code"
author_email = "maahisnu144@gmail.com"
description = "Package containing basic functions to build telegram bots."
license = "GNU AFFERO GENERAL PUBLIC LICENSE (v3)"
url = "https://github.com/vasusen-code/ethon"
classifiers = [
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Operating System :: OS Independent",
]
requirements = [
    "python-decouple",
    "telethon",
    "aiofiles",
    "aiohttp",
]



setuptools.setup(
    name=name,
    version=ver,
    author=author,
    author_email=author_email,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=url,
    license=license,
    packages=setuptools.find_packages(),
    py_modules=['ethon'],
    install_requires=requirements,
    classifiers=classifiers,
    python_requires=">=3.6",
)
#!/usr/bin/env python

from setuptools import setup, find_packages

description = 'git, libcaca and gravatar smooth integration'
with open('README.md') as f:
    long_description = f.read()

setup(
    name='gitcaca',
    version='0.1',
    packages=find_packages(),
    install_requires=['requests'],
    scripts=['gitcaca/gitcaca-fetch', 'gitcaca/gitcaca-display'],
    package_data = {'gitcaca': ['gitcaca/avatars/default.png']},
    zip_safe=False,
    author="Matthieu Caneill",
    author_email="matthieu.caneill@gmail.com",
    long_description=long_description,
    description=description,
    license="WTFPL-2",
    url="https://github.com/matthieucan/gitcaca",
    platforms=['any'],
)
#!/usr/bin/env python3
from setuptools import setup
setup(
    name = 'FileSave-cli',
    version = '0.1.0',
    packages = ['FileSave'],
    entry_points = {
        'console_scripts': [
            'FileSave = FileSave.__main__:main'
        ]
    })

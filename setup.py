#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import codecs
from setuptools import setup
# from setuptools import find_packages

# python setup.py sdist
# twine upload dist/*

def get_markdown_description():
    with codecs.open('README.md', encoding='utf-8') as fp:
        long_description = fp.read()
        return long_description
    return ''


setup(
    name='secure_delete',
    version='0.0.2',
    description='A tool for safely delete files.',
    author='wevsty',
    author_email='ty@wevs.org',
    url='https://github.com/wevsty/secure_delete',
    packages= ['secure_delete'],
    package_data={
        'secure_delete': ['README.md', 'LICENSE']
    },
    entry_points={
        'console_scripts': [
            'secdel = secure_delete.secure_delete_cmd:main',
        ]
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    long_description=get_markdown_description(),
    long_description_content_type='text/markdown'
)
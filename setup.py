# Copyright (C) 2015-2016 Skylable Ltd. <info-copyright@skylable.com>
# License: Apache 2.0, see LICENSE for more details.

import os
import re

from codecs import open
from setuptools import setup, find_packages

packages = find_packages()


def get_version():
    path = os.path.join('s3import', '__init__.py')
    pattern = re.compile(r"^__version__ = '(?P<ver>\d+\.\d+\.\d+)'$")
    match = None
    with open(path, 'r', 'utf-8') as fo:
        for line in fo:
            match = pattern.match(line)
            if match:
                break

    if not match:
        raise AttributeError('No __version__ in __init__.py')

    return match.groupdict()['ver']


def get_requirements(path):
    with open(path, 'r', 'utf-8') as fo:
        content = fo.read()
    return content.split()


def get_description_from_file(path):
    with open(path, 'r', 'utf-8') as fo:
        readme = fo.read()
    return readme


setup(
    name='s3import',
    version=get_version(),
    description='S3 data import utility',
    long_description=get_description_from_file('README.rst'),
    author='Skylable Ltd.',
    author_email='sx-users@lists.skylable.com',
    url='http://www.skylable.com/products',
    packages=packages,
    install_requires=get_requirements('requirements.txt'),
    license='Apache 2.0',
    entry_points={
        'console_scripts': [
            's3import=s3import.cli:main',
        ]
    },
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ),
)

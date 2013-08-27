#!/usr/bin/env python

# Note: Based on https://github.com/kennethreitz/requests/blob/master/setup.py
# See: http://docs.python.org/2/distutils/setupscript.html

import os
import sys

import MafIO

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'MafIO',
]

requires = []
if os.path.isfile('requirements.txt'):
    with open('requirements.txt') as fin:
        lines = fin.readlines()
    for l in lines:
        requires.append(l.strip())

setup(
    name=MafIO.__title__,
    version=MafIO.__version__,
    description=MafIO.__description__,
    long_description=open('README.rst').read(),
    author=MafIO.__author__,
    author_email = MafIO.__author_email__,
    url = MafIO.__url__,
    packages=packages,
    scripts = [''],
    package_data={'': ['LICENSE']},
    package_dir={'MafIO': 'MafIO'},
    include_package_data=True,
    install_requires=requires,
    license=open('LICENSE').read(),
    zip_safe=False,
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2 :: Only',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ),
)

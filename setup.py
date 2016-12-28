#!/usr/bin/env python
from __future__ import with_statement

import os
import re
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


NAME = 'easycolor'


def get_long_description(filename):
    readme = os.path.join(os.path.dirname(__file__), filename)
    with open(readme) as f:
        return f.read()


def read_file(path):
    with open(os.path.join(os.path.dirname(__file__), path)) as f:
        return f.read()


def _get_version_match(content):
    # Search for lines of the form: # __version__ = 'ver'
    regex = r"^__version__ = ['\"]([^'\"]*)['\"]"
    version_match = re.search(regex, content, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


def get_version(path):
    return _get_version_match(read_file(path))


setup(
    name=NAME,
    version=get_version(os.path.join(NAME, '__init__.py')),
    description='Terminal colors made easy!',
    long_description=read_file('README.rst'),
    keywords='color colour terminal text ansi',
    author='George T. Gougoudis',
    author_email='george_gougoudis@gmail.com',
    maintainer='George T. Gougoudis',
    url='https://github.com/GeorgeTG/easycolor',
    license='BSD',
    packages=[NAME],
    # see classifiers http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.3',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Terminals',
    ]
)

#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="confindr",
    version="0.4.1",
    packages=find_packages(),
    scripts=['confindr/confindr.py'],
    author="Andrew Low",
    author_email="andrew.low@inspection.gc.ca",
    url="https://github.com/lowandrew/ConFindr",
    install_requires=['biopython',
                      'pysam',
                      'pytest',
                      'numpy']
)

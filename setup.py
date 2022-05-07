# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.MD') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='HomeworkCollection',
    version='0.1.0',
    description='This repository stores the programs I use for collection jobs.',
    long_description=readme,
    author='iceberg-work',
    author_email='iceberg-work@qq.com',
    url='https://github.com/iceberg-work/HomeworkCollection',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)


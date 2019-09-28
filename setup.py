# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='nlp-lib',
    version='0.1.0',
    description='Simple nlp utility',
    long_description=readme,
    author='Kristen Foster-Marks',
    author_email='kristen.foster-marks@gmail.com',
    url='https://github.com/KFoster-Marks/nlp-lib',
    packages=find_packages(exclude=('tests', 'docs'))
)
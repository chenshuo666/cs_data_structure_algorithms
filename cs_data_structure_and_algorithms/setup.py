#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import io
from setuptools import find_packages, setup


def long_description():
    with io.open('README.md', 'r', encoding='utf-8') as f:
        readme = f.read()
    return readme


setup(name='cs_dsaa',
      version='0.1.0',
      description='Pythonic Data Structures and Algorithms',
      long_description=long_description(),
      long_description_content_type="text/markdown",
      url='https://github.com/chenshuo666/cs_data_structure_algorithms',
      author='Sebastian Williams',
      author_email="nuaa_chenshuo@163.com",
      license='MIT',
      packages=find_packages(),
      classifiers=[
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          ],
      zip_safe=False)

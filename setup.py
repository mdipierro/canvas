#!/usr/bin/python
# -*- coding:Utf-8 -*-

from setuptools import setup

setup(name='canvas',
      version='0.1',
      description='canvas is a simple interface to most common matplotlib functions',
      author='Massimo DiPierro',
      # haven't found your email addr
      # author_email='',
      long_description=open("README.md").read(),
      url='https://github.com/mdipierro/canvas',
      install_requires=['numpy', 'matplotlib'],
      py_modules=["canvas"],
      license= 'BSD',
      keywords='matplotlib',
     )

# vim:set shiftwidth=4 tabstop=4 expandtab:

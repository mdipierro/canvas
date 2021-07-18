import ast
import re

import setuptools

setuptools.setup(
    name = "canvas",
    version = 0.2,
    url = 'https://github.com/mdipierro/canvas',
    license = 'BSD',
    author = 'Massimo Di Pierro',
    author_email = 'massimo.dipierro@gmail.com',
    maintainer = 'Massimo Di Pierro',
    maintainer_email = 'massimo.dipierro@gmail.com',
    description = 'a minimallist abstraction layer on top of matplotlib',
    packages = ['canvas'],
    include_package_data = True,
    zip_safe = False,
    platforms = 'any',
    classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

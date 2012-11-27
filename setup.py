#! /usr/bin/env python
from distutils.core import setup

__version__ = '0.1'

setup(
    name="text-unidecode",
    version=__version__,
    description="The most basic Text::Unidecode port",
    long_description = open('README.rst').read(),
    license = 'Artistic License',
    author='Mikhail Korobov',
    author_email='kmike84@gmail.com',

    url = 'https://github.com/kmike/text-unidecode/',

    package_dir = {'': 'src'},
    packages = ['text_unidecode'],
    package_data = {'text_unidecode': ['data.bin']},

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Artistic License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Linguistic',
    ],
)

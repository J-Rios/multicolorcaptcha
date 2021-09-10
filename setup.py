#!/usr/bin/env python3
from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst')) as f:
    long_description = f.read()

with open(path.join(here, 'multicolorcaptcha', 'version.txt')) as f:
    version = f.read().strip()

setup(
    name='multicolorcaptcha',
    description='Python random image-captcha generator library.',
    long_description=long_description,
    url='https://github.com/J-Rios/multicolorcaptcha',

    version=version,

    author='Jose Miguel Rios Rubio',
    author_email='jrios.github@gmail.com',
    license='GPLv3',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    keywords='captcha, color',

    packages=[
        'multicolorcaptcha',
    ],

    package_data={
        'multicolorcaptcha': ['fonts/*', 'version.txt'],
    },

    entry_points={
        'console_scripts': [
            'multicolorcaptchademo = multicolorcaptcha.main:demo',
        ],
    },

    install_requires=[
        'Pillow',
    ],

    setup_requires=[
        'pytest-runner',
    ],

    tests_require=[
        'pytest',
        'pytest-mock',
    ],
)

#!/usr/bin/env python3
import os
import re

from setuptools import setup


def get_long_description():
    with open("README.md", encoding="utf8") as f:
        return f.read()


def get_variable(variable):
    with open(os.path.join("multicolorcaptcha", "__init__.py")) as f:
        return re.search(
            "{} = ['\"]([^'\"]+)['\"]".format(variable), f.read()
        ).group(1)  # type: ignore


setup(
    name="multicolorcaptcha",
    description=get_variable("__description__"),
    long_description_content_type="text/markdown",
    long_description=get_long_description(),
    url=get_variable("__url__"),
    version=get_variable("__version__"),
    author=get_variable("__author__"),
    author_email=get_variable("__author_email__"),
    license=get_variable("__license__"),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    keywords="captcha, color",
    packages=[
        "multicolorcaptcha",
    ],
    include_package_data=True,
    install_requires=[
        "Pillow",
    ],
    setup_requires=[
        "pytest-runner",
    ],
    tests_require=[
        "pytest",
        "pytest-mock",
    ],
)

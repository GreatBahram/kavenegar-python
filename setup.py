import codecs
import os
import sys

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

requires = [
        'requests',
        ]

about = {}

with open(os.path.join(here, "kavenegar", "__version__.py")) as f:
    exec(f.read(), about)

setup(
        name = about['__title__'],
        version = about['__version__'],
        description = about['__description__'],
        author = about['__author__'],
        packages=find_packages(),
        author_email = about['__author_email__'],
        url = about['__url__'],
        keywords = ["kavenegar", "sms"],
        license= about['__license__'],
        install_requires = requires,
        classifiers = [
            "Programming Language :: Python",
            "Operating System :: OS Independent",
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Topic :: Communications :: Telephony",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3 :: Only",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            ]
        )

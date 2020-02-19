# -*- coding: utf-8 -*-
import sys

from setuptools import setup, find_packages  # pylint: disable=no-name-in-module,import-error

install_requires = []


def dependencies(file):
    with open(file) as f:
        return f.read().splitlines()

setup(
    name='spinners',
    packages=find_packages(exclude=('tests', 'examples')),
    version='0.0.24',
    license='MIT',
    description='Spinners for terminals',
    long_description='More than 60 spinners for terminal, this is python port of amazing node library cli-spinners. Find the documentation here: https://github.com/manrajgrover/py-spinners.',
    author='Manraj Singh',
    author_email='manrajsinghgrover@gmail.com',
    url='https://github.com/manrajgrover/py-spinners',
    keywords=[
        'cli',
        'spinner',
        'spinners',
        'terminal',
        'term',
        'console',
        'ascii',
        'unicode',
        'loading',
        'indicator',
        'progress',
        'busy',
        'wait',
        'idle',
        'json'
    ],
    install_requires=install_requires,
    extras_require={
        ':python_version < "3.4"': [
            'enum34==1.1.6',
        ],
    },
    tests_require=dependencies('requirements-dev.txt'),
    include_package_data=True
)

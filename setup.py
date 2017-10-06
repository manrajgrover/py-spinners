# -*- coding: utf-8 -*-
from setuptools import setup, find_packages # pylint: disable=no-name-in-module,import-error

def dependencies(file):
    with open(file) as f:
        return f.read().splitlines()

setup(
    name='spinners',
    packages=find_packages(exclude=('tests', 'examples')) + ['cli-spinners'],
    version='0.0.19',
    license='MIT',
    description='Spinners for terminals',
    long_description='More than 60 spinners for terminal, this is python port of amazing node library cli-spinners. Find the documentation here: https://github.com/ManrajGrover/py-spinners.',
    author='Manraj Singh',
    author_email='manrajsinghgrover@gmail.com',
    url='https://github.com/ManrajGrover/py-spinners',
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
    install_requires=dependencies('requirements.txt'),
    tests_require=dependencies('requirements-dev.txt'),
    include_package_data=True
)

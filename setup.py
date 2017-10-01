# -*- coding: utf-8 -*-
from setuptools import setup, find_packages # pylint: disable=no-name-in-module,import-error

def readme():
    with open('README.md') as f:
        return f.read()

def dependencies(file):
    with open(file) as f:
        return f.read().splitlines()

setup(
    name='spinners',
    packages=find_packages(exclude=('tests', 'examples')) + ['cli-spinners'],
    version='0.0.17',
    license='MIT',
    description='Spinners for terminals',
    long_description=readme(),
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

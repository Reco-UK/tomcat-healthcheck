# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='agent',
    version='1.0.0',
    description=' agent',
    long_description=readme,
    author='Reece Fensome',
    author_email='reece.fensome@pcmsgroup.com',
    url='https://bitbucket.org:flooid/python-gce-agent',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=requirements
)

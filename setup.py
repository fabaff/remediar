"""Setup file for remediar."""
from setuptools import setup, find_packages
from remediar.core.version import get_version
import os

VERSION = get_version()


here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the relevant file
with open(os.path.join(here, 'README.md'), encoding='utf-8') as desc:
    long_description = desc.read()


setup(
    name='remediar',
    version=VERSION,
    description='Remediar is an issue and vulnerability tracker framework',
    long_description=long_description,

    author='Fabian Affolter',
    author_email='fabian@affolter-engineering.com',
    url='https://github.com/fabaff/remediar/',
    license='Apache 2.0',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'remediar': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        remediar = remediar.main:main
    """,
)

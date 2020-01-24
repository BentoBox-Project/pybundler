from os import environ as env
from setuptools import find_packages, setup
from setuptools.command.install import install
import sys

VERSION = '1.0.0a1'


with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()


class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""
    description = 'verify that the git tag matches our version'

    def run(self):
        tag = env.get('PYBUNDLER_TAG')
        if tag != VERSION:
            info = f"Git tag: {tag} doesn't match with this version: {VERSION}"
            sys.exit(info)


setup(
    name='pybundler',
    version=VERSION,
    description='Create or manage a python app or package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Daniel Omar Vergara Pérez',
    author_email='daniel.omar.vergara@gmail.com',
    url='https://github.com/dany2691/pybundler',
    packages=find_packages(exclude=('tests',)),
    install_requires=[
        'click',
        'colored',
        'pypkg-generator',
        'pipenv',
        'twine'
    ],
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    entry_points={
        'console_scripts': [
            'pybundler=pybundler.__main__:main'
        ]
    },
    cmdclass={'verify': VerifyVersionCommand}
)

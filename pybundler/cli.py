# -*- coding: utf-8 -*-
""" Cli commands
This file contains many commands for app managment
"""
import os
import subprocess

from pypkg_generator import package_generator


def build_source_wheel(version=3):
    """ Creates a source archive and a wheel for your package
    Parameters
    ----------
    version : int
        Defines the python version
    """
    if version == 3:
        result = subprocess.run(['python3', 'setup.py',
                                 'sdist', 'bdist_wheel'], cwd=os.getcwd())
    else:
        result = subprocess.run(['python', 'setup.py', 'sdist', 'bdist_wheel'],
                                cwd=os.getcwd())
    return result.returncode


def test_release():
    """ Uploads the package to test.pypi.org
    """
    result = subprocess.run(['twine', 'upload', '--repository-url',
                             'https://test.pypi.org/legacy/', 'dist/*'],
                            cwd=os.getcwd())
    return result.returncode


def release(remote=True):
    """ Uploads the package to pypi.org and pushes it to the git remote
    Parameters
    ----------
    remote : bool
        If remote is True, push the last commit to the git remote
    """
    result = subprocess.run(['twine', 'upload', 'dist/*'], cwd=os.getcwd())
    if remote:
        subprocess.run(['git', 'push', 'origin', 'master'], cwd=os.getcwd())
    return result.returncode


def install_pytest(pkg_dir=None, version=None):
    """ Installs pytest in a pinned version"""
    if version:
        command = ['pipenv', 'install', f'pytest=={version}', '--dev']
    else:
        command = ['pipenv', 'install', 'pytest', '--dev']

    result = subprocess.run(command, cwd=pkg_dir)
    return result.returncode


def install_python_version(pkg_dir=None, version='',
                           runner=subprocess.run):
    """Intalls a given python version into a virtual env"""
    if version:
        command = ["pipenv", "--python", version]
    else:
        command = ["pipenv", "install"]
    result = runner(command, cwd=pkg_dir)
    return result.returncode


def create_pkg(args):
    """ Creates a new python package from scratch
    Parameters
    ----------
    args : dict
        Contains the info to create the package
        according to needs of the user.
    """
    creator = package_generator.PackageGenerator(args)
    creator.call()

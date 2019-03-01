# -*- coding: utf-8 -*-
""" Cli commands
This file contains many commands for app managment
"""
import os
import subprocess

from pypkg_generator import package_generator


def install(dependency='', dev=False):
    """
    Installs a given python dependency,
    and adds them to Pipfile

    Parameters
    ----------
    dependency : str
       The python dependecy to install

    dev : bool
        If the python dependency is used during develoment
    """
    result = subprocess.run(['pipenv', 'install',
                             dependency, '--dev' if dev else ''],
                            cwd=os.getcwd())
    return result.returncode


def install_all(dev=False):
    """ Installs all packages from Pipfile
    (including dev dependencies if dev is provided)
    Parameters
    ----------
    dev : bool
        If dev is provided, install the dev dependencies
    """
    result = subprocess.run(['pipenv', 'install', '--dev' if dev else ''],
                            cwd=os.getcwd())
    return result.returncode


def uninstall(dependency=''):
    """ Uninstalls a python depdency
    Parameters
    ----------
    dependecy : str
        The python depdency to uninstall from the current virtual env
    """
    result = subprocess.run(['pipenv', 'uninstall', dependency],
                            cwd=os.getcwd())
    return result.returncode


def lock():
    """ Creates or updates the Pipfile.lock
    """
    result = subprocess.run(['pipenv', 'lock'], cwd=os.getcwd())
    return result.returncode


def shell():
    """ Spawns a shell within the virtualenv
    """
    result = subprocess.run(['pipenv', 'shell'], cwd=os.getcwd())
    return result.returncode


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


def install_pytest(pkg_dir=None):
    """ Installs pytest in a pinned version
    """
    result = subprocess.run(['pipenv', 'install', 'pytest==4.3.0',
                             '--dev'], cwd=pkg_dir)
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

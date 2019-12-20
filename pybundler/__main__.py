# -*- coding: utf-8 -*-
"""Main Function and entry point of the package

This script requires that `click` be installed within the Python
environment you are running this script in.

This file contains the following functions:

    * conduct_option              - Returns the conduct file option
    * license_option              - Returns the license file option
    * pipfile_option              - Returns the pipfile file option
    * enter_name                  - Ask for the name of the new package
    * enter_path                  - Ask for the path of the new project
    * install_pytest_confirmation - Ask if pytest should be installed
    * main                        - the main function of the script

Commands:
    build-whell: Creates a source archive and a wheel for your package
    test-release: Uploads the package to test.pypi.org
    release: Uploads the pacakge to pypi.org
    package: Creates a new python package from scratch
    version: Prints the current version of pybundler
"""
import os

import click
from colored import fg, attr

from pybundler import cli, __version__


@click.group()
def main():
    """Pybundler is a convinient tool to scaffold python for general purposes,
    like libraries.

    Type a single command and inmidiately start working with project
    with all you need.
    You can select what you need, because this tool ask you before install or
    create something.
    We recommend some practices or libraries, but is up to you what wiil
    be installed.
    """
    pass


def conduct_option():
    """Returns the conduct file option"""
    return f'{fg(2)} Do you want to include a code of conduct file? {attr(0)}'


def license_option():
    """Returns the license file option"""
    return f'{fg(2)} Do you want to include a license file? {attr(0)}'


def pipfile_option():
    """Returns the pipfile file option"""
    return f'{fg(2)} Do you want to include a Pipfile file? {attr(0)}'


def enter_name():
    """Ask for the name of the new package"""
    return f'{fg(2)} Please, enter the name of the package: {attr(0)}'


def enter_path():
    """Ask for the path of the new project"""
    default_path = '(default: current dir)'
    return f'{fg(2)} Enter the path of the project {default_path}{attr(0)}'


def install_pytest_confirmation():
    """Ask if pytest should be installed"""
    return f'{fg(2)} Do you want to install pytest? {attr(0)}'


def enter_pytest_version():
    """Ask for the desired version for pytest"""
    message = "(default: Press enter to always install the latest version)"
    return f'{fg(2)} Enter the desired pytest version {message} {attr(0)}'


def ask_for_pipenv_env():
    """Ask the user if he wants to create a virtual environment"""
    question = "Do you want to create a pipenv virtual environment?"
    return f"{fg(2)} {question} {attr(0)}"


def ask_for_python_version():
    """
    Ask the user for the python version.
    Default: The last version installed
    """
    pyenv_clarification = "(previously installed by pyenv)"
    question = f"Which python version do you need {pyenv_clarification}?"
    default = "(default: the latest python version in the system)"
    return f"{fg(2)} {question} {default} {attr(0)}"


@main.command()
def build_wheel():
    """Builds the wheel to release the package
    $ python setup.py sdist bdist_wheel
    """
    cli.build_source_wheel()


@main.command()
def test_release():
    """Uploads the package to test.pypi.org
    $ twine upload --repository-url https://test.pypi.org/legacy/ dist/*
    """
    cli.test_release()


@main.command()
def release():
    """Uploads the package to pypi.org
    $ twine upload dist/*
    """
    cli.release()


@main.command()
def package():
    """Creates a new Python package from scratch"""
    pkg_name = click.prompt(enter_name())
    path = click.prompt(enter_path(), default='')
    license_file = click.confirm(license_option())
    conduct_file = click.confirm(conduct_option())
    create_pipenv_env = click.confirm(ask_for_pipenv_env())
    pytest = click.confirm(install_pytest_confirmation())
    args = {
        'name': pkg_name,
        'path': path,
        'tests': True,
        'license': license_file,
        'code_of_conduct': conduct_file,
        'pipfile': False
    }
    cli.create_pkg(args)

    if create_pipenv_env:
        python_version = click.prompt(
            ask_for_python_version(),
            default=""
        )
        cli.install_python_version(
            pkg_dir=os.path.join(path, pkg_name),
            version=python_version
        )

        if pytest:
            pytest_version = click.prompt(
                enter_pytest_version(),
                default=''
            )
            cli.install_pytest(
                os.path.join(path, pkg_name),
                pytest_version
            )


@main.command()
def version():
    print(f'pybundler, version {__version__}')


if __name__ == '__main__':
    main()

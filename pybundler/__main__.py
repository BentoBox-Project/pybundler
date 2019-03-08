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
"""
import os

import click
from colored import fg, attr

from pybundler import cli, __version__


@click.command()
@click.option('--install-all', is_flag=True,
              help='Installs all packages from Pipfile')
@click.option('--install', '-i', default='',
              help='Install a given package or the content of the Pipfile')
@click.option('--uninstall', '-u',
              help='uninstalls a given dependecy')
@click.option('--dev', '-d', is_flag=True,
              help='If it is True, install dependency in dev section')
@click.option('--lock', is_flag=True,
              help='Creates or updates the Pipfile.lock')
@click.option('--shell', '-s', is_flag=True,
              help='Spawns a shell within the virtualenv')
@click.option('--build-wheel', '-b', is_flag=True,
              help='Creates a source archive and a wheel for your package')
@click.option('--test-release', '-t', is_flag=True,
              help='Uploads the package to test.pypi.org')
@click.option('--release', '-r', is_flag='True',
              help='Uploads the package to pypi.org and'
                   'pushes it to the git remote')
@click.option('--package', '-p', is_flag=True,
              help='Creates a new python package from scratch')
@click.option('--version', '-v', is_flag=True,
              help='Shows the current version of the package')
def main(install_all, install, uninstall, dev, lock, shell,
         build_wheel, test_release, release, package, version):
    """Executes the entire program

    Parameters \n
    ----------- \n
    install_all : bool\n
        Installs all packages from Pipfile\n
    install : str\n
        The given dependency that is going to be installed\n
    uninstall: str\n
        Uninstalls the given dependency and removes it from Pipfile\n
    dev : bool\n
        Installs the given dependency as a develoment dependency\n
    lock : bool\n
        Generates or updates Pipfile.lock\n
    shell : bool\n
         Spawns a shell within the virtualenv\n
    build_wheel : bool\n
        Creates a source archive and a wheel for your package\n
    test_release : bool\n
        Uploads the package to test.pypi.org\n
    release : bool\n
        Uploads the package to pypi.org and pushes it to the git remote\n
    package : bool\n
        Creates a new python package from scratch\n
    version : bool\n
        Shows the current version of the package
    """
    if install_all:
        cli.install_all(dev)

    if install:
        cli.install(install, dev)

    if uninstall:
        cli.uninstall(uninstall)

    if lock:
        cli.lock()

    if shell:
        cli.shell()

    if build_wheel:
        cli.build_source_wheel()

    if test_release:
        cli.test_release()

    if release:
        cli.release()

    if package:
        pkg_name = click.prompt(enter_name())
        path = click.prompt(enter_path(), default='')
        license_file = click.confirm(license_option())
        conduct_file = click.confirm(conduct_option())
        pipfile = click.confirm(pipfile_option())
        pytest = click.confirm(install_pytest_confirmation())
        args = {'name': pkg_name, 'path': path, 'tests': True,
                'license': license_file, 'code_of_conduct': conduct_file,
                'pipfile': pipfile}
        cli.create_pkg(args)

        if pytest:
            cli.install_pytest(os.path.join(path, pkg_name))

    if version:
        print(f'pybundler, version {__version__}')


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
    return f'{fg(2)} Please, enter the nanme of the package: {attr(0)}'


def enter_path():
    """Ask for the path of the new project"""
    return f'{fg(2)}Enter the path of the project (default: current dir){attr(0)}'


def install_pytest_confirmation():
    """Ask if pytest should be installed"""
    return f'{fg(2)} Do you want to install pytest? {attr(0)}'


if __name__ == '__main__':
    main()

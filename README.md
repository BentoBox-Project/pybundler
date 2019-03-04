# Pybundler
> Manages a ptyhon applicatons or packages.

Creates a basic template of python package and manages python apps or packages.
The purpose of this tool is offer a similar experience with ruby's bundler.
This package is based on [pypkg-generator](https://pypi.org/project/pypkg-generator/) and [pipenv](https://pypi.org/project/pipenv/).

## Installation

OS X & Linux:

From PYPI

```sh
$ pip3 install pybundler
```

from the source

```sh
$ git clone https://github.com/dany2691/pybundler.git
$ cd pybundler
$ python3 setup.py install
```

## Usage example

Open a terminal and type:

```sh
$ pybundler --help
```

And it'll display:

```sh
Options:
  --install-all         Installs all packages from Pipfile
  -i, --install TEXT    Install a given package or the content of the Pipfile
  -u, --uninstall TEXT  uninstalls a given dependecy
  -d, --dev             If it is True, install dependency in dev section
  --lock                Creates or updates the Pipfile.lock
  -s, --shell           Spawns a shell within the virtualenv
  -b, --build-wheel     Creates a source archive and a wheel for your package
  -t, --test-release    Uploads the package to test.pypi.org
  -r, --release         Uploads the package to pypi.org andpushes it to the
                        git remote
  -p, --package         Creates a new python package from scratch
  --help                Show this message and exit
```

The purpose of this tool is offer a similar experience with ruby's bundler. So you can create a new package from scratch.

```sh
$ pybundler --package
```
Then, a list of question will prompted in order to customize the new package:

```sh
Please, enter the nanme of the package: : greate-project
Enter the path of the project (default: current dir) []:
Do you want to include a license file?  [y/N]: y
Do you want to include a code of conduct file?  [y/N]: y
Do you want to include a Pipfile file?  [y/N]: y
Do you want to install pytest?  [y/N]: y
```

So you can install dependencies like pipenv in a virtual enviroment:

```sh
$ pybundler --install numpy==1.16.2
```

You can install dev dependencies, as shown below:

```sh
$ pybundler --install pytest --dev
```

So, like pipenv, is possible to install all dependencies from Pipfile

```sh
$ pybundler --install-all
```

The following option generates or updates Pipfile.lock:

```sh
$ pybundler --lock
```

The following option spawns a shell within the virtualenv:

```sh
$ pybundler --shell
```

In order to automate the publishing of the new package, we provide the next options for building and uploading the package to pypi and the remote git service.

This is a replacement for **python setup.py sdist bdist_wheel**

```sh
$ pybundler --build-wheel
```

The next option, uploads the package to test.pypi.org:

```sh
$ pybundler --test-release
```

And last but not least, this one, uploads the package to pypi.org and pushes it to the git remote:

```sh
$ pybundler --release
```

# Development setup

This project uses _pipenv_ for dependecy resolution. It's a kind of mix between
pip and virtualenv. Follow the next instructions to setup the development enviroment.

```sh
$ git clone https://github.com/dany2691/pybundler.git
$ cd pybundler
$ pipenv shell
$ pipenv install -e .
```

To run the test-suite, inside the pybundler directory:

```shell
$ pytest -vv test/
```

## Release History

* 0.2.0
    * CHANGE: New name of the project, `pybundler` instead of `py-bundler`
* 0.1.1
    * FIX: README.md fixed, `text/markdown` instead of `text/markadown`
* 0.1.0
    * The first proper release
    * ADD: Add cli module
* 0.0.1
    * Work in progress

## Meta

Daniel Omar Vergara Pérez – [@dan1_net](https://twitter.com/dan1_net) – daniel.omar.vergara@gmail.com

[https://github.com/dany2691](https://github.com/dany2691)

## Contributing

1. Fork it (<https://gitlab.com/hexagondata_projects/pybundler>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

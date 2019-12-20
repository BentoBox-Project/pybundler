import contextlib
import shutil
import tempfile
from unittest.mock import Mock, patch

from pybundler import cli


@contextlib.contextmanager
def get_temp_dir():
    temp_dir = tempfile.mkdtemp()
    try:
        yield temp_dir
    finally:
        shutil.rmtree(temp_dir)


@patch('pybundler.cli.subprocess.run')
def test_build_function(mock_run):
    mock_run.return_value = Mock(returncode=0)
    assert cli.build_source_wheel() == 0


@patch('pybundler.cli.subprocess.run')
def test_test_release_function(mock_run):
    mock_run.return_value = Mock(returncode=0)
    assert cli.test_release() == 0


@patch('pybundler.cli.subprocess.run')
def test_release_function(mock_run):
    mock_run.return_value = Mock(returncode=0)
    assert cli.release() == 0


def test_install_python_version():
    with get_temp_dir() as dir:
        def runner(command, cwd):
            class FakeProcessObject:
                def __init__(self):
                    self.returncode = 0

            if command[0] != 'pipenv':
                raise ValueError("Can only run pipenv args")
            if command[1] != "--python":
                raise ValueError("Can only run given flag")
            if cwd != dir:
                raise ValueError("Can only run in the given directory")

            fake_process = FakeProcessObject()
            fake_process.returncode = 1
            return fake_process

        returncode = cli.install_python_version(
            pkg_dir=dir,
            version='3.7.4',
            runner=runner
        )
        assert returncode == 1


def test_install_python_default_version():
    with get_temp_dir() as dir:
        def runner(command, cwd):
            class FakeProcessObject:
                def __init__(self):
                    self.returncode = 0

            if command[0] != 'pipenv':
                raise ValueError("Can only run pipenv args")
            if command[1] != "install":
                raise ValueError("Can only run valid pipenv installation")
            if cwd != dir:
                raise ValueError("Can only run in the given directory")

            fake_process = FakeProcessObject()
            fake_process.returncode = 1
            return fake_process

        returncode = cli.install_python_version(
            pkg_dir=dir,
            runner=runner
        )
        assert returncode == 1

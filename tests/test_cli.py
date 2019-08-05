from unittest.mock import Mock, patch

from pybundler import cli


@patch('pybundler.cli.subprocess.run')
def test_install_function(mock_run):
    mock_run.return_value = Mock(returncode=0)
    assert cli.install('dependecy') == 0


@patch('pybundler.cli.subprocess.run')
def test_install_all_function(mock_run):
    mock_run.return_value = Mock(returncode=0)
    assert cli.install_all() == 0


@patch('pybundler.cli.subprocess.run')
def test_uninstall_function(mock_run):
    mock_run.return_value = Mock(returncode=0)
    assert cli.uninstall('dependecy') == 0


@patch('pybundler.cli.subprocess.run')
def test_lock_function(mock_run):
    mock_run.return_value = Mock(returncode=0)
    assert cli.lock() == 0


@patch('pybundler.cli.subprocess.run')
def test_shell_function(mock_run):
    mock_run.return_value = Mock(returncode=0)
    assert cli.shell() == 0


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

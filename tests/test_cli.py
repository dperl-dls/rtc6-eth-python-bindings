import subprocess
import sys

from rtc6py import __version__


def test_cli_version():
    cmd = [sys.executable, "-m", "rtc6py", "--version"]
    assert subprocess.check_output(cmd).decode().strip() == __version__

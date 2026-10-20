import subprocess
import sys
import pytest


def test_no_deadlock():

    for i in range(20):

        try:
            result = subprocess.run(
                [sys.executable, "original.py"],
                capture_output=True,
                text=True,
                timeout=2,
            )

        except subprocess.TimeoutExpired:
            pytest.fail(
                f"Виявлено deadlock під час запуску {i + 1}: "
                "програма не завершилася за 2 секунди"
            )

        assert result.returncode == 0, result.stderr

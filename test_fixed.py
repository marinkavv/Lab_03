import subprocess
import sys


def test_no_deadlock():

    for i in range(20):

        try:
            result = subprocess.run(
                [sys.executable, "fixed.py"], capture_output=True, text=True, timeout=2
            )

        except subprocess.TimeoutExpired:

            assert False, f"Програма зависла під час запуску {i + 1}"

        assert result.returncode == 0, result.stderr

        assert "Кінцевий баланс Alice: 80" in result.stdout
        assert "Кінцевий баланс Bob: 220" in result.stdout

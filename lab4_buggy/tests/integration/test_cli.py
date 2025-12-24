import subprocess
import sys
from pathlib import Path


def test_cli_from_file(tmp_path):
    data_file = tmp_path / "numbers.txt"
    data_file.write_text("10 20 30", encoding="utf-8")

    result = subprocess.run(
        [sys.executable, "-m", "src.main", "--file", str(data_file)],
        cwd=Path(__file__).resolve().parents[2],
        check=True,
        capture_output=True,
        text=True,
    )

    assert "Количество: 3" in result.stdout
    assert "Среднее: 20.0000" in result.stdout

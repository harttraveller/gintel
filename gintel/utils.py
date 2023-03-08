from pathlib import Path
from gintel.env import FILES


def make_package_directory():
    if not Path(FILES).exists():
        Path(FILES).mkdir()

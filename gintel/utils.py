from pathlib import Path
from pyeio import easy
from gintel.env import FILES
from gintel.env import TOKENS


def make_package_directory():
    if not Path(FILES).exists():
        Path(FILES).mkdir()


class Tokens:
    def __init__(self) -> None:
        pass

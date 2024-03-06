import sys
from typing import NoReturn

import pytest


def main() -> NoReturn:
    """
    A wrapper function for running pytest through Poetry.
    This allows us to use 'poetry run test' to execute pytest.
    """
    sys.exit(pytest.main())

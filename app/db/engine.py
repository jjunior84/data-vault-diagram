"""Module for engine connection with database."""
import json
from typing import Any


def create_engine(path: str) -> Any:
    """Create engine connection with database.

    Args:
        path (str): Database path.

    Returns:
        _type_: Engine
    """
    with open(path) as json_file:
        return json.load(json_file)

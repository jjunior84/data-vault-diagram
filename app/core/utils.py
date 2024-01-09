"""Module utils for general helper functions."""
import json
from typing import Any, Dict

import yaml
from core.exceptions import DiagramParseError


def read_external_config(path: str, parse_as: str = None) -> Any:
    """Return data read from external configuration file parsed accordingly.

    Args:
        path (str): Path where the file will be find.
        parse_as (str, optional): Indicates to parse file to python object as.

    Returns:
        Any: Object read, any type of python obejct.
    """
    with open(path) as r_file:
        if parse_as == "json":
            return json.load(r_file)
        elif parse_as == "yaml":
            return yaml.safe_load(r_file)
        else:
            return r_file.read()


def parse_diagram_code(data: str) -> Dict[Any, Any]:
    """Parse diagram code (str) to python object, try with languages supported.

    Args:
        data (str): Diagram code in text format.

    Raises:
        DiagramParseError: Raise error if fail to parse.

    Returns:
        Dict[Any, Any]:Code parsed to python dictionary.
    """
    try:
        return yaml.safe_load(data)
    except yaml.YAMLError:
        pass

    try:
        return json.loads(data)
    except json.JSONDecodeError:
        pass

    raise DiagramParseError()


def try_blank(func: Any) -> Any:
    """Function return blank when value none.

    Args:
        func (_type_): Function to apply.
    """

    def wrapper(*args, **kwargs):  # noqa: ANN202, ANN002, ANN003
        result = func(*args, **kwargs)
        return "" if result is None else result

    return wrapper

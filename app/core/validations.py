"""Module for data vault validations."""
from typing import Dict, List

from core import exceptions
from model import DataVaultEntity


def validate_entity_type(
    dv_entity: DataVaultEntity, entity_type_list: List[str]
) -> None:
    """Validate data vault entity type match with expected list.

    Args:
        dv_entity (DataVaultEntity): data vault entity.
        entity_type_list (List[str]): list of allowed type.

    Raises:
        exceptions.DataVaultEntityTypeError: Raise data vault entity error if fails.
    """
    if dv_entity.type not in entity_type_list:
        raise exceptions.DataVaultEntityTypeError(dv_entity.type)


def validate_entity_naming_convention(
    dv_entity: DataVaultEntity, entity_naming_convention: Dict[str, List[str]]
) -> None:
    """Validate data vault entity naming convention.

    Args:
        dv_entity (DataVaultEntity): data vault entity.
        entity_naming_convention (str, List[str]): dictionary of allowed naming by type.

    Raises:
        exceptions.DataVaultNamingConventionError: Raise data vault naming convention
        error if fails.
    """
    _valid = False
    _naming_conventions = entity_naming_convention[dv_entity.type]
    for pattern in _naming_conventions:
        if dv_entity.label.startswith(pattern):
            _valid = True
            break

    if not _valid:
        raise exceptions.DataVaultNamingConventionError(
            dv_entity.label, dv_entity.type, _naming_conventions
        )


def validate_entity_connection() -> None:
    """TODO."""
    pass

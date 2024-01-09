"""Module constain custom exceptions."""
from typing import List


class DataVaultModelValidationError(Exception):
    """Class for Data Vault Model Validation Error Exception."""

    pass


class DiagramParseError(ValueError):
    """Class for Diagram Parse Error Exception."""

    def __init__(
        self, message: str = "Diagram code could not be parsed as Json or YAML format."
    ) -> None:
        self.message = message
        super().__init__(self.message)


class DataVaultEntityTypeError(DataVaultModelValidationError):
    """Class for Data Vault Entity Type Error Exception."""

    def __init__(self, type: str) -> None:
        self.message = f"{type} is not a valid data vault entity type."
        super().__init__(self.message)


class DataVaultNamingConventionError(DataVaultModelValidationError):
    """Class  Data Vault Naming Convention Error Exception."""

    def __init__(self, label: str, type: str, options: List[str]) -> None:
        self.message = (
            f"{label} is classified as {type} and should start with {options}."
        )
        super().__init__(self.message)

"""Module to register schemas used to enhance entity specification."""
from typing import Any, Dict, List, Union

from pydantic import BaseModel, Field, field_validator, model_validator


class EntityFieldSchema(BaseModel):
    """Data class representing a field of entity."""

    name: str
    type: str = None
    mode: str = None
    description: str = None
    extra: Dict[str, str] = None


class EntitySchema(BaseModel):
    """Data class representing an entity (can be a table, view, file...)."""

    name: str
    type: str
    description: str = None
    fields: List[EntityFieldSchema] = None
    extra: Dict[str, str] = None


class Connection(BaseModel):
    """Base data class represents Connection entity."""

    target: Union[str, List[str]] = Field(alias="to")
    cardinality: str = None
    extra_attr: Dict[str, Any] = None


class DataVaultEntity(BaseModel):
    """Base data class represents Data Vault entity."""

    id: str = Field(alias="name")
    type: str
    label: str = None
    description: str = None
    connections: List[Connection] = Field(default=None)
    entity_schema: EntitySchema = Field(alias="schema", default=None)
    extra_attr: Dict[str, Any] = None

    @model_validator(mode="before")
    @classmethod
    def transform_label(cls, data: Dict[str, Any]) -> Dict[str, Any]:
        """Model validation if naming convention for label was followed.

        Args:
            data (Any): model with data exteced as dictionary.

        Raises:
            DataVaultEntityTypeError: raise exception is type is not allowed.

        Returns:
            str: Return entity type value.
        """
        if isinstance(data, Dict):
            if not data.get("label"):
                data["label"] = data["name"]
            return data
        else:
            raise ValueError("Data Vault Entity data expected as dictionary instance.")

    @field_validator("connections", mode="before")
    @classmethod
    def transform_connections(
        cls, connections: List[Dict[str, Any]]
    ) -> List[Dict[str, str]]:
        """Function get connections and adapt for expected format expected by model.

        Args:
            connections (List[Dict[str, Any]]): connections dictionary.

        Returns:
            List[Dict[str, str]]: connections dictionary adjusted.
        """
        _new_connections = []
        if connections:
            for conn in connections:
                if isinstance(conn.get("to"), List):
                    for to in conn.get("to"):
                        nconn = conn.copy()
                        nconn["to"] = to
                        _new_connections.append(nconn)
                else:
                    _new_connections.append(conn)
        return _new_connections


class DataVaultModel(BaseModel):
    """Base data class represents Diagram Config entity."""

    diagram: str = Field(default="")
    entities: List[DataVaultEntity] = Field(default=[])

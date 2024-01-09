"""Module for session."""
from typing import Any, List

from pydantic import parse_obj_as


class Session:
    """Session class."""

    def __init__(self, engine: Any) -> None:
        """Construct from session class.

        Args:
            engine (Any): Engine, database connection.
        """
        self.engine = engine

    def list(self, model: Any) -> List[Any]:
        """List all model records.

        Args:
            model (Any): Model object.

        Returns:
            List[Any]: List of objects.
        """
        return self._parse_model(model)

    def add(self, model: Any) -> Any:  # noqa: D102
        raise NotImplementedError

    def get(self, model: Any, id: str) -> Any:
        """Get model record by id.

        Args:
            model (Any): Model object.
            id (str): Id from object.

        Returns:
            Any: Object.
        """
        return [p for p in self._parse_model(model) if p.id == id][0]

    def _parse_model(self, model: Any) -> Any:
        """Parse model object accordingly its type.

        Args:
            model (Any): Model

        Returns:
            Any: Parsed object model.
        """
        return parse_obj_as(List[model], self.engine[model.__table_name__])

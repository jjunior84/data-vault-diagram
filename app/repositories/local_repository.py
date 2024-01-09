"""Module implements a in-memory repository for parameters."""
from typing import Generic, List, Optional, Type, TypeVar

from db.session import Session
from pydantic import BaseModel
from repositories.base import BaseRepository

ModelType = TypeVar("ModelType", bound=BaseModel)


class LocalRepository(BaseRepository, Generic[ModelType]):
    """Local Reository class."""

    def __init__(self, model: Type[ModelType], db: Session) -> None:
        """Local Reository class contructor.

        Args:
            model (Type[ModelType]): Model.
            db (Session): Database session.
        """
        self._model = model
        self._db = db

    def add(self, obj: ModelType) -> ModelType:  # noqa: D102
        raise NotImplementedError

    def get(self, id: str) -> Optional[ModelType]:
        """Get object from repository by id.

        Args:
            id (str): Id from the object.

        Returns:
            Optional[ModelType]: Object.
        """
        try:
            return self._db.get(self._model, id)
        except StopIteration:
            print(f"Item did not exist with specified key: {id}")
            return None

    def list(self) -> Optional[List[ModelType]]:
        """List all objects from repository.

        Returns:
            Optional[List[ModelType]]: List of objects.
        """
        return self._db.list(self._model)

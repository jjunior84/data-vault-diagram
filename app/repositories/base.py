"""Module holds repository abstract class."""
from abc import ABC, abstractmethod
from typing import Any, List, Optional


class BaseRepository(ABC):
    """Abstract class for repository."""

    @abstractmethod
    def add(self, db: Any, model: Any) -> Optional[Any]:  # noqa: D102
        raise NotImplementedError

    @abstractmethod
    def get(self, db: Any, id: str) -> Optional[Any]:  # noqa: D102
        raise NotImplementedError

    @abstractmethod
    def list(self, db: Any) -> Optional[List[Any]]:  # noqa: D102
        raise NotImplementedError

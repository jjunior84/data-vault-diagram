"""Module for base model."""
from pydantic import BaseModel


class BaseDBModel(BaseModel):
    """Base DB model heir from pydantict BaseModel."""

    __table_name__: str = None

    class Config:  # noqa: D106
        arbitrary_types_allowed = True

    @classmethod
    def __init_subclass__(cls, **kwargs):  # noqa: ANN003, ANN206
        """Initialize class attribute for table name information."""
        super().__init_subclass__(**kwargs)
        if not cls.__table_name__:
            # Set table_name to the lowercase version of the class name
            cls.__table_name__ = cls.__name__.lower()

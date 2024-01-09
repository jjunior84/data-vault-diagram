"""Module to register data vault parameters model."""
from typing import List

from model.base import BaseDBModel
from pydantic import Field


class DVParameter(BaseDBModel):
    """Data class representing data vault parameters."""

    id: str = Field(alias="dv_id")
    dv_image_name: str
    dv_type: str
    dv_naming_convention: List[str]
    dv_description: str

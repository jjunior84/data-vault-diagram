"""Module define configuration settings."""
from typing import Dict, List

from core.utils import read_external_config
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Implements class for settings configurations."""

    COLOR: str = "#000000"
    ICON_DIR: str = (
        "https://raw.githubusercontent.com/PatrickCuba/the_data_must_flow/master/art/"
    )
    NODE_SHAPE: str = "image"
    NODE_SIZE: int = 40
    ARROW_IMAGES: Dict = {
        "one": "https://raw.githubusercontent.com/PatrickCuba/the_data_must_flow/master/art/BRIDGE.png",
        "many": "config/images/N.png",
    }

    DATABASE_FILE: str = "config/local_database.json"

    CODE_EDITOR_CUSTOMIZE_BTN: List = read_external_config(
        path="config/code_editor_customize.json", parse_as="json"
    )
    CODE_EDITOR_INFO_BAR_CUSTOMIZE: Dict = read_external_config(
        path="config/info_bar.json", parse_as="json"
    )
    CODE_EDITOR_CSS_CUSTOMIZE: str = read_external_config(
        "config/code_editor_style.css.scss"
    )

    DEMO_DIAGRAM_CODE: str = read_external_config("config/dv_diagram_example.yaml")

    DIAGRAM_CONFIG: str = "config/diagram_config.json"

    DIAGRAM_CONF_BUILDER: bool = False


settings = Settings()

"""Module creates Code Editor component."""
from typing import Any, Dict

from code_editor import code_editor


class CodeEditorService:
    """Code Editor Service class."""

    def __init__(
        self,
        code_customization: Dict[str, Any],
        info_bar_customization: Dict[str, Any],
        css_customization: str,
    ) -> None:
        """Code Editor Service class constructor.

        Args:
            code_customization (Dict[str, Any]): Code customization config.
            info_bar_customization (Dict[str, Any]): Infor bar config.
            css_customization (str): CSS stylesheet config.
        """
        self._code_customization = code_customization
        self._info_bar_customization = info_bar_customization
        self._css_customization = css_customization

    def load_code_editor(self, code: str, language: str = "yaml") -> Dict:
        """Function responsible for load an code editor (code_editor library instance).

        Args:
            code (str): Code to in the code editor, if none will load demo.
            language (str, optional): which language the code editor will parse.

        Returns:
            Dict: Dictionary with the content of code editor.
        """
        comp_props = {
            "css": self._css_customization,
            "globalCSS": ":root {\n  --streamlit-dark-font-family: monospace;\n}",
        }

        ace_props = {"style": {"borderRadius": "0px 0px 8px 8px"}}

        self._info_bar_customization["info"][0]["name"] = language
        response = code_editor(
            code=code,
            lang=language,
            height=500,
            allow_reset=False,
            info=self._info_bar_customization,
            options={"wrap": True},
            props=ace_props,
            component_props=comp_props,
            buttons=self._code_customization,
        )
        return response

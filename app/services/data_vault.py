"""Module for Data Vault Services."""
from typing import List

import pandas as pd
from core.utils import parse_diagram_code
from core.validations import validate_entity_naming_convention, validate_entity_type
from model import DataVaultModel, DVParameter
from repositories import LocalRepository


class DataVaultService:
    """Data Vault Service class."""

    def __init__(self, parameter_repository: LocalRepository[DVParameter]) -> None:
        """Data Vault Service constructor.

        Args:
            parameter_repository (LocalRepository[DVParameter]): Instance of parameter
            repository
        """
        self.data_vault_model: DataVaultModel = None
        self.parameter_repository = parameter_repository

    def load_data_vault_model(self, diagram_code: str) -> DataVaultModel:
        """Load data vault model from diagram code.

        Args:
            diagram_code (str): Diagram code (text).

        Returns:
            DataVaultModel: Data Vault Model.
        """
        parsed_code = parse_diagram_code(diagram_code)
        if not parsed_code:
            parsed_code = {}

        tmp_model = DataVaultModel(**parsed_code)

        entity_type_list = [param.id for param in self.parameter_repository.list()]
        entity_naming_convention = {
            param.id: param.dv_naming_convention
            for param in self.parameter_repository.list()
        }

        for entity in tmp_model.entities:
            validate_entity_type(entity, entity_type_list)
            validate_entity_naming_convention(entity, entity_naming_convention)

        self.data_vault_model = tmp_model
        return self.data_vault_model

    def load_param_dataframe(self) -> pd.DataFrame:
        """Function responsible to load parameters to a pandas Dataframe.

        Returns:
            pd.DataFrame: pandas Dataframe.
        """
        return pd.DataFrame(
            [param.model_dump() for param in self.parameter_repository.list()]
        )

    def get_entity_name_list(self) -> List[str]:
        """Return list of entity name.

        Returns:
            List[str]: List with entity name.
        """
        return [entity.label for entity in self.data_vault_model.entities]

"""Module for diagram components."""
from typing import Any, Dict, List, Optional

import pandas as pd
import streamlit as st
from core.config import settings
from model import Connection, DataVaultEntity, DataVaultModel
from repositories import LocalRepository
from streamlit.components.v1.components import CustomComponent
from streamlit_agraph import Config, ConfigBuilder, Edge, Node, agraph


class DiagramService:
    """Class create diagram component based on streamlit agraph library."""

    def __init__(
        self,
        parameter_repository: LocalRepository,
        config: Config = None,
    ) -> None:
        self.parameter_repository = parameter_repository
        self.config = config if config else Config(from_json=settings.DIAGRAM_CONFIG)

    def _generate_title(self, entity: DataVaultEntity) -> Optional[str] :
        """Generate specification to be used as title for Node based on schema,
        It will affect the mouse hover description on the diagram.

        Returns:
            Optional[str]: HTML as text formatted.
        """
        return entity.description if entity.description else entity.label

    def _get_image_path(self, type: str) -> str:
        """Return image URI based on the type of entity to be created.

        Returns:
            str: Element image URI.
        """
        return (
            f"{settings.ICON_DIR}/{self.parameter_repository.get(type).dv_image_name}"
        )

    def _parse_node(self, entity: DataVaultEntity) -> List[Node]:
        return Node(
            id=entity.id,
            title=self._generate_title(entity),
            label=entity.label,
            shape=settings.NODE_SHAPE,
            size=settings.NODE_SIZE,
            image=self._get_image_path(entity.type),
            color="#000000",
            **entity.extra_attr if entity.extra_attr else {},
        )

    def _parse_edges(self, source: str, connections: List[Connection]) -> List[Node]:
        edges = []
        if connections:
            for conn in connections:
                arrows_to = {}
                arrows_from = {}

                if conn.cardinality:
                    cardinal_to, cardinal_from = conn.cardinality.split("-to-")

                    arrows_to = self._get_arrow_info(cardinal_to)
                    arrows_from = self._get_arrow_info(cardinal_from)

                edges.append(
                    Edge(
                        source=source,
                        target=conn.target,
                        arrows={"to": arrows_to, "from": arrows_from},
                        title=conn.cardinality,
                        **conn.extra_attr if conn.extra_attr else {},
                    )
                )
        return edges

    def _get_arrow_info(self, cardinal: str) -> Dict:
        """Get arrows configuration accordingly with cardinal.

        Args:
            cardinal (str): Cardinal from connection (one, many).

        Returns:
            Dict: Dictionary with arrow configuration.
        """
        return {
            "enabled": True,
            "scaleFactor": 1,
            "type": "bar" if cardinal == "one" else "circle",
        }

    def load_diagram(
        self, data_vault_model: DataVaultModel, includes_conf_builder: bool = False
    ) -> CustomComponent:
        """Function responsible for load diagram (streamlit agraph instance).

        Args:
            data_vault_model (DataVaultModel): Model to be used to parse nodes
            and connections

            includes_conf_builder (bool, optional): Define if config builder
            will be used. Usefull to find optimal configuration. Defaults to False.

        Returns:
            CustomComponent: custom component representing streamlit agraph.
        """
        nodes = []
        edges = []

        for entity in data_vault_model.entities:
            nodes.append(self._parse_node(entity))
            edges += self._parse_edges(entity.id, entity.connections)

        if includes_conf_builder:
            self.config = ConfigBuilder(nodes, edges).build()
            self.config.save("config/diagram_config.json")

        return agraph(nodes, edges, self.config)

    def get_entity_detail_text(
        self, data_vault_model: DataVaultModel, entity_id: str
    ) -> Any:
        """Return entity detail text."""
        entity = [
            entity for entity in data_vault_model.entities if entity.label == entity_id
        ][0]
        if entity:
            col1, col2 = st.columns([1, 12])
            col1.image(self._get_image_path(entity.type), width=60)
            col2.markdown(f"#### {entity.label}")
            with st.container() as entity_detail:
                st.markdown(f"###### *Type:* {entity.type}")
                st.markdown(
                    f"###### *Description:* {entity.description if entity.description else ''}"  # noqa: E501
                )

                if entity.entity_schema:
                    st.markdown("##### Schema:")
                    st.markdown(f"###### *Object:* {entity.entity_schema.name}")
                    st.markdown(f"###### *Object Type:* {entity.entity_schema.type}")
                    st.markdown(
                        f"###### *Description:* {entity.entity_schema.description if entity.entity_schema.description else ''}"  # noqa: E501
                    )

                    if entity.entity_schema.fields:
                        st.markdown("##### Fields:")
                        df = pd.DataFrame(
                            [
                                field.model_dump()
                                for field in entity.entity_schema.fields
                            ],
                        )
                        df = df.drop(["extra"], axis=1)
                        st.dataframe(df, use_container_width=True, hide_index=True)

                connections = []
                # connection out
                if entity.connections:
                    st.markdown("##### Connections:")
                    for connection in entity.connections:
                        connections.append(
                            {
                                "source": entity.label,
                                "cardinality": connection.cardinality,
                                "target": connection.target,
                            }
                        )
                # connection in
                for ent in data_vault_model.entities:
                    if ent.connections:
                        for connection in ent.connections:
                            if connection.target == entity.id:
                                connections.append(
                                    {
                                        "source": ent.label,
                                        "cardinality": connection.cardinality,
                                        "target": connection.target,
                                    }
                                )

                df = pd.DataFrame(connections)
                st.dataframe(df, use_container_width=True, hide_index=True)

        return entity_detail

"""Module represents how to use data vaul diagram tool."""
import streamlit as st
from core.config import settings

# Setup Page
st.set_page_config(
    page_title="How to use Data Vault Diagram tool",
    page_icon="☸️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items=None,
)

with st.container():
    st.markdown("## Data Vault Diagram Tool Areas")
    st.image("docs/images/tool_areas.png")

    st.markdown("#### Code Area")
    st.markdown(
        "This is our **work area**, here it is where you will input code that \
        will be used to render the diagram."
    )
    st.markdown(
        "The code editor is initially loaded with a template but further in the \
        document, it is explained the pattern expected."
    )
    st.markdown(
        "Code editor supports two types of configuration languages (YAML and \
        JSON). It can be changed the highlight syntax support in the side bar."
    )

    st.markdown("#### Diagram Area")
    st.markdown(
        "**Presentation area:** Here it is where the diagram comes to life and draw \
        itself based on the code provided. The graph is automatically displayed and \
        each entity can be dragged for a different position to rearrange."
    )
    st.markdown(
        "Cardinality in the edges when defined in the code is represented by a bar ▎\
        when cardinality is 1 (one) and by a circle ⚫ when cardinality is N (many)"
    )  # noqa: E501
    st.markdown(
        "By click on the node it will open below of the diagram the table of detail \
        of the entity which can be changed by the select box also."
    )

with st.container():
    code_yaml, code_json = st.columns([1, 1])
    st.markdown("## Code Pattern")
    st.markdown(
        "Tool is designed to read the code editor, get code text, parse to \
        object model, run all validations and render the graph. But to ensure the \
        correct work of it, the code is expected to follow a pattern"
    )

with st.container():
    st.markdown("### Data Vault Diagram Tool Models")

    st.markdown("##### **DataVaultModel**")
    st.markdown(
        """
Base data class represents Diagram Config entity.

| Name      | Type               | Description                               |
|-----------|--------------------|-------------------------------------------|
| diagram   | str                   | The diagram associated with the model. |
| entities  | List[[DataVaultEntity](#datavaultentity)] | List of entities associated with the model. |
"""  # noqa: E501
    )

    st.divider()

    st.markdown("##### **DataVaultEntity**")
    st.markdown(
        """
Base data class represents Data Vault entity.

| Name           | Type                           | Description                                 |
|----------------|--------------------------------|---------------------------------------------|
| id             | str                            | The ID of the entity.                       |
| type           | str                            | The type of the entity. Type are confront with allowed list. |
| label          | str                            | The label of the entity. Must follow naming convention|
| description    | str, optional                  | A description of the entity.                |
| entity_schema  | [EntitySchema](#entityschema), optional         | Describe a phisical database objects.      |
| connections    | List[[Connection](#connection)], optional     | List of connections associated with entity. |
"""  # noqa: E501
    )

    st.divider()

    st.markdown("##### **EntitySchema**")
    st.markdown(
        """
Data class representing an entity (can be a table, view, file...).

| Name        | Type                           | Description                            |
|-------------|--------------------------------|----------------------------------------|
| name        | str                            | The name of the entity.                |
| type        | str                            | The type of the entity.                |
| description | str, optional                  | A description of the entity.           |
| fields      | List[[EntityFieldSchema](#entityfieldschema)], optional | List of fields associated with entity. |
"""  # noqa: E501
    )

    st.markdown("\n\n")
    st.markdown("##### **EntityFieldSchema**")
    st.markdown(
        """
Data class representing a field of an entity.

| Name         | Type               | Description                                |
|--------------|--------------------|--------------------------------------------|
| name         | str                | The name of the field.                      |
| type         | str, optional      | The type of the field.                      |
| mode         | str, optional      | The mode of the field.                      |
| description  | str, optional      | A description of the field.                |
"""  # noqa: E501
    )

    st.divider()

    st.markdown("##### **Connection**")
    st.markdown(
        """
Base data class represents Connection entity.

| Name        | Type                     | Description                            |
|-------------|--------------------------|----------------------------------------|
| target      | str or List[str], alias="to" | The target of the connection.      |
| cardinality | str, optional            | The cardinality of the connection.     |

"""  # noqa: E501
    )

    st.divider()
    st.markdown("##### Data Vault Diagram Samples")

    with st.expander("YAML Example"):
        st.markdown(
            """```yaml
    diagram: Diagram Name # [Optional]
entities: # List of Entities
    - id: str
      label: str # Validate for Naming Convention
      type: str # Validate for Type Allowed
      description: str #[Optional]
      entity_schema: #[Optional]
        name: str
        type: str
        description: str #[Optional]
        fields: #[Optional]
        - name: str
          type: str
          mode: str #[Optional]
          description: str #[Optional]
      connections: #[Optional]
        - to: str
          cardinality: str # [Optional] Validate for Cardinality Option
    """
        )

    with st.expander("JSON Example"):
        st.markdown(
            """```json
{
  "diagram": "Diagram Name",
  "entities": [
    {
      "id": "str",
      "label": "str",
      "type": "str",
      "description": "str",
      "entity_schema": {
        "name": "str",
        "type": "str",
        "description": "str",
        "fields": [
          {
            "name": "str",
            "type": "str",
            "mode": "str",
            "description": "str"
          }
        ]
      },
      "connections": [
        {
          "to": "str",
          "cardinality": "str"
        }
      ]
    }
  ]
}
    """
        )


with st.container():
    st.markdown("\n\n")
    st.markdown("### Data Vault Validation")
    st.markdown(
        "To make this tool even more useful, some data model validations \
        is applied to besure that model follow some minimum criteria of quality \
        and data modeller life easier. The list of validations the tools is applying \
        (so far) are described below, find me in github and open a issue if you want \
        include new ones or find some issue, your help will be very important."
    )

    st.markdown("##### Validate Naming Covention")
    st.markdown(
        """
        * **Model:** DatavaVaultEntity
        * **Field:** label
        * **Rule(s):** Name needs to start with the valid naming convention \
            accordingly with the type (see column Naming Convention on \
            [Data Vault Entity Options](#data-vault-entity-options))
    """
    )

    st.markdown("##### Validate Type")
    st.markdown(
        """
        * **Model:** DatavaVaultEntity
        * **Field:** type
        * **Rule(s):** Type needs to be one of the allowed type (see column Type on \
            [Data Vault Entity Options](#data-vault-entity-options))
    """
    )

    st.markdown("##### Validate Connections")
    st.markdown(
        """
        * **Model:** DatavaVaultEntity
        * **Field:** connections
        * **Rule(s):**
            * Entity of group type Satellite can not connect with another Satellite.
    """
    )

    st.markdown("##### Data Vault Entity Options ")
    df = st.session_state.data_vault_service.load_param_dataframe()
    df["dv_image"] = settings.ICON_DIR + df["dv_image_name"]

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        column_order=(
            "id",
            "dv_type",
            "dv_naming_convention",
            "dv_image",
            "dv_description",
        ),
        height=500,
        column_config={
            "id": st.column_config.Column(
                "Entity Type",
                width="small",
                help="Acronym is used to work with diagram tool.",
            ),
            "dv_type": st.column_config.Column(
                "Group Type",
                width="small",
                help="Identify the type of Data Vault entity.",
            ),
            "dv_naming_convention": st.column_config.Column(
                "Naming Convention",
                width="small",
                help="Allowed naming convention to be used as label in the diagram.",
            ),
            "dv_image": st.column_config.ImageColumn(
                "Image Icons",
                help="Image Icons representing the dta vault entity types.",
            ),
            "dv_description": st.column_config.Column(
                "Description",
                width="small",
                help="Data Vault entity type description.",
            ),
        },
    )

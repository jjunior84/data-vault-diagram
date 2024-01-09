"""Main module control program execution."""

import streamlit as st
from core.config import settings
from core.deps import get_db
from core.exceptions import DataVaultModelValidationError
from model import DVParameter
from repositories import LocalRepository
from services import CodeEditorService, DataVaultService, DiagramService
from st_pages import Page, show_pages

# Update Page Display Name
show_pages(
    [
        Page("app/main.py", "Data Vault Diagram"),
        Page("app/pages/how_to.py", "How to Use the App"),
        Page("app/pages/about.py", "About Data Vault 2.0"),
    ]
)

# Setup Page
st.set_page_config(
    page_title="Data Vault Diagram",
    page_icon="☸️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items=None,
)

# Initialize Session State
if "data_vault_model" not in st.session_state:
    ## Read only once in the session:,
    parameter_repository = LocalRepository(DVParameter, get_db())

    st.session_state.data_vault_service = DataVaultService(parameter_repository)
    st.session_state.diagram_service = DiagramService(parameter_repository)
    st.session_state.code_editor_service = CodeEditorService(
        settings.CODE_EDITOR_CUSTOMIZE_BTN,
        settings.CODE_EDITOR_INFO_BAR_CUSTOMIZE,
        settings.CODE_EDITOR_CSS_CUSTOMIZE,
    )

    st.session_state.data_vault_model = (
        st.session_state.data_vault_service.load_data_vault_model(
            settings.DEMO_DIAGRAM_CODE
        )
    )

    st.session_state.previous_result = None
    st.session_state.diagram_result = None

    st.session_state.code = settings.DEMO_DIAGRAM_CODE
    st.session_state.current_language = "yaml"


# Sidebar Options
with st.sidebar:
    language_selector = st.selectbox(
        label="Prefered Language",
        options=["yaml", "json"],
        index=0,
        key="language_selector",
    )

# Content
st.title("Data Vault Diagram Tool")
with st.container():
    code_col, graph_col = st.columns([1, 3])
    with code_col:
        code_response = st.session_state.code_editor_service.load_code_editor(
            st.session_state.code, language_selector
        )

    with graph_col:
        if code_response["type"] == "submit" and len(code_response["id"]) != 0:
            st.session_state.code = code_response["text"]
            try:
                st.session_state.data_vault_model = (
                    st.session_state.data_vault_service.load_data_vault_model(
                        code_response["text"]
                    )
                )
                st.markdown(f"### {st.session_state.data_vault_model.diagram}")
                st.session_state.diagram_result = (
                    st.session_state.diagram_service.load_diagram(
                        st.session_state.data_vault_model,
                        includes_conf_builder=settings.DIAGRAM_CONF_BUILDER,
                    )
                )
            except DataVaultModelValidationError as e:
                st.error(f"#### ❌{e.message}")
        else:
            st.markdown(f"### {st.session_state.data_vault_model.diagram}")
            st.session_state.diagram_result = (
                st.session_state.diagram_service.load_diagram(
                    st.session_state.data_vault_model,
                    includes_conf_builder=settings.DIAGRAM_CONF_BUILDER,
                )
            )

        with st.container():
            entity_list = st.session_state.data_vault_service.get_entity_name_list()
            with st.columns([1, 3])[0]:
                entity_selected = st.selectbox(
                    label="Entities",
                    options=entity_list,
                    index=entity_list.index(st.session_state.diagram_result)
                    if st.session_state.diagram_result
                    else 0,
                )
            st.session_state.previous_result = st.session_state.diagram_result
            with st.container(border=1):
                if entity_selected:
                    st.session_state.diagram_service.get_entity_detail_text(
                        st.session_state.data_vault_model, entity_selected
                    )

        if st.session_state.diagram_result != st.session_state.previous_result:
            st.rerun()

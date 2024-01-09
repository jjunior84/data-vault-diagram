"""Module represents about dtaa vault page."""
import streamlit as st
from core.config import settings

# Setup Page
st.set_page_config(
    page_title="About Data Vault 2.0",
    page_icon="☸️",
    initial_sidebar_state="expanded",
    menu_items=None,
)

#:nth-of-type(1)
with st.container():
    st.markdown(
        """
        <style>
            div[data-testid="column"] h4 span
            {
                text-align: center;
            },
            div[data-testid="column"]:nth-of-type(1)
            {
                align-items: center;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("## What is Data Vault 2.0")
    st.write(
        """Data Vault 2.0 is a methodology and architecture designed to address the \
        challenges associated with traditional data warehousing approaches. It \
        emphasizes flexibility, scalability, and agility to accommodate the dynamic \
        nature of modern businesses and their data needs."""
    )

    st.markdown("## Architecture")
    st.write(
        """Data Vault 2.0 employs a hub-and-spoke architecture that consists of three \
        main components: Hubs, Links, and Satellites."""
    )

    col_1_c, col_2_c, col_3_c = st.columns([1, 1, 1])
    col_1_i, col_2_i, col_3_i = st.columns([1, 1, 1])

    with col_1_c:
        st.markdown("#### Hubs")
        st.write(
            """Hubs represent the core business entities, such as customers, products, \
            or transactions."""
        )

    with col_2_c:
        st.markdown("#### Links")
        st.write("""Links capture the relationships between hubs.""")

    with col_3_c:
        st.markdown("#### Satellites")
        st.write(
            """Satellites store historical and contextual information related to \
            hubs."""
        )

    with col_1_i:
        st.image(settings.ICON_DIR + "RV-1HUB.png", width=150)

    with col_2_i:
        st.image(settings.ICON_DIR + "RV-2LINK.png", width=150)

    with col_3_i:
        st.image(settings.ICON_DIR + "RV-3SATELLITE.png", width=150)

    st.write(
        """In addition to Hubs, Links, and Satellites, Data Vault 2.0 also includes \
        two other important components: Point-in-Time Tables (PITs) and Bridges."""
    )

    col_11_c, col_12_c, col_13_c = st.columns([1, 1, 1])
    col_11_i, col_12_i, col_13_i = st.columns([1, 1, 1])

    with col_11_c:
        st.markdown("#### PIT")
        st.write(
            """PITs (Point-in-Time) are tables designed to simplify querying of \
            business objects and relationships state."""
        )

    with col_12_c:
        st.markdown("#### Bridges")
        st.write(
            """Bridges are tables designed to shorten distance between business \
            objects."""
        )

    with col_11_i:
        st.image(settings.ICON_DIR + "PIT.png", width=150)

    with col_12_i:
        st.image(settings.ICON_DIR + "BRIDGE.png", width=150)

    st.markdown("### Thanks")
    st.write(
        """My sincererily thanks from Patrick Cuba for \
        [The Data Vault Guru](https://www.amazon.com/dp/B08KSSKFMZ) book, and for the \
        awesome github [repository](https://github.com/PatrickCuba/the_data_must_flow) \
        from where a harvest the images I´m using on this tool."""
    )

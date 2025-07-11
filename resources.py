import streamlit as st
from understanding import show_understanding
from support import show_support
from strategies import show_strategies
from font import set_global_font
set_global_font()

def show_resources():
    # Show banner image at top, full width, no margin
    st.markdown(
        """
        <div style="text-align: center; margin: 0; padding: 0;">
            <img src="https://i.ibb.co/rRHvZjCp/qpmulqrb.png" 
                 style="width: 100%; max-height: 120px; object-fit: cover;" />
        </div>
        """, unsafe_allow_html=True
    )

    # Set white background and override previous background image
    st.markdown(
        """
        <style>
        [data-testid="stAppViewContainer"] {
            background-color: #ffffff !important;
            background-image: none !important;
            color: #000000 !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("Parent Resources")

    if "resource_page" not in st.session_state:
        st.session_state.resource_page = "main"

    if st.session_state.resource_page == "main":
        st.markdown("### Select a resource topic:")

        if st.button("Understanding Therapy"):
            st.session_state.resource_page = "understanding"

        if st.button("Supporting Your Child at Home"):
            st.session_state.resource_page = "support"

        if st.button("At-Home Coping and Calming Strategies"):
            st.session_state.resource_page = "strategies"

    elif st.session_state.resource_page == "understanding":
        show_understanding()

    elif st.session_state.resource_page == "support":
        show_support()

    elif st.session_state.resource_page == "strategies":
        show_strategies()

def back_to_resources():
    if st.button("⬅ Back to Resources"):
        st.session_state.resource_page = "main"
        st.experimental_rerun()  # updated to recommended rerun call

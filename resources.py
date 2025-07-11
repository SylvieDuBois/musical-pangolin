import streamlit as st
from understanding import show_understanding
from support import show_support
from strategies import show_strategies
from font import set_global_font
set_global_font()


def show_resources():
    st.markdown(
        """
        <style>
        [data-testid="stAppViewContainer"] {
            background: url('https://i.ibb.co/4ZwQkWdM/Untitled-design-9.png') no-repeat center center fixed;
            background-size: cover;
            background-attachment: fixed;
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
        st.rerun()

 

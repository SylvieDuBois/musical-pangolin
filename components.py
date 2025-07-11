import streamlit as st

def back_to_resources():
    if st.button("⬅ Back to Resources"):
        st.session_state.resource_page = "main"
        st.rerun()

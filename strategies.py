import streamlit as st
from components import back_to_resources
from font import set_global_font
set_global_font()


def show_strategies():
    st.header("At-Home Calming Strategies")
    st.markdown("""
    **Tools to practice with your child:**
    - Deep belly breathing to help in times of anxiety.
    - Creative outlets such as art, journaling, or music to express emotions.
    - Setting up a calming space with comforting objects.
    """)
    back_to_resources() 
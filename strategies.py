import streamlit as st
from components import back_to_resources
from font import set_global_font
set_global_font()


def show_strategies():
    st.header("At-Home Coping and Calming Strategies")
    st.markdown("""
    Practical tools to practice together:
    - **Grounding techniques:** Focus on the present moment using the 5-4-3-2-1 method.
    - **Breathing exercises:** Deep belly breathing to reduce anxiety.
    - **Creative outlets:** Drawing, journaling, music to express emotions.
    - **Setting up a calming space:** A quiet corner with comforting objects.
    """)
    back_to_resources() 
import streamlit as st
from components import back_to_resources
from font import set_global_font
set_global_font()


def show_understanding():
    st.header("Understanding Therapy")
    st.markdown("""
    **What you need to know about therapy:**
    - What therapy is: A safe space for your child to express their feelings and learn coping skills.
    - Common therapy types: Play therapy, cognitive behavioral therapy, and family therapy.
    - Explain therapy in a supportive way to make them comfortable and ensure the sessions are effective.
    """)
    back_to_resources()

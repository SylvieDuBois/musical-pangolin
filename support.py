import streamlit as st
from components import back_to_resources
from font import set_global_font
set_global_font()


def show_support():
    st.header("Supporting Your Child at Home")
    st.markdown("""
    Ways you can help your child outside therapy:
    - Recognize signs your child needs support (mood changes, withdrawal, irritability).
    - Use active listening to validate feelings.
    - Create a calm, predictable home environment.
    - Encourage healthy routines: sleep, nutrition, physical activity.
    """)
    back_to_resources()

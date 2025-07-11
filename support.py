import streamlit as st
from components import back_to_resources
from font import set_global_font
set_global_font()


def show_support():
    st.header("Supporting Your Child")
    st.markdown("""
    **Ways you can help your child outside therapy:**
    - Recognize the signs your child needs support such as mood changes, withdrawal, or irritability.
    - Take the time to listen to your child to validate their feelings.
    - Encourage physical health through sleep, nutrition, and activity.
    """)
    back_to_resources()

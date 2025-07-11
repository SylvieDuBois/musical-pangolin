import streamlit as st
from components import back_to_resources
from font import set_global_font
set_global_font()


def show_understanding():
    st.header("Understanding Therapy")
    st.markdown("""
    Therapy can be a powerful tool to support your child’s emotional and mental well-being.  
    Here’s what parents should know:
    - **What therapy is:** A safe space for your child to express feelings and learn coping skills.
    - **Common therapy types:** Play therapy, cognitive behavioral therapy (CBT), family therapy.
    - **What to expect:** Regular sessions with a trained therapist, progress over time.
    - **Talking to your child:** How to explain therapy in a supportive way.
    """)
    back_to_resources()

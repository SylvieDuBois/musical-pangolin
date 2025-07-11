import streamlit as st

def set_global_font():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Bodoni+Moda:wght@400;500;600;700;800&display=swap');

        html, body, [data-testid="stAppViewContainer"] * {
            font-family: 'Bodoni Moda', serif !important;
            font-weight: 550 !important;  /* Increase default body text weight */
        }

        h1, h2, h3, h4, h5, h6 {
            font-weight: 700 !important;  /* Strong headings */
        }

        p, span, div, label {
            font-weight: 550 !important;  /* Slightly bolder than default */
        }
        </style>
    """, unsafe_allow_html=True)

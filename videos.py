import streamlit as st
from font import set_global_font

set_global_font()

def show_videos():
    st.set_page_config(page_title="Calming Videos")

    # Top banner image
    st.markdown(
        """
        <div style="text-align: center; margin-top: 0;">
            <img src="https://i.ibb.co/p6ddJXGH/m05vvwkj.png" style="width: 100%; max-height: 120px; object-fit: cover;">
        </div>
        """,
        unsafe_allow_html=True
    )

    # Style overrides
    st.markdown("""
        <style>
        [data-testid="stAppViewContainer"] {
            background-color: #ffffff !important;
        }

        .stButton > button {
            background-color: #C8E6C9 !important;
            color: black !important;
            border: none !important;
            border-radius: 12px !important;
            padding: 0.75em 2em !important;
            font-size: 1.1em !important;
            font-weight: 600 !important;
            width: 100% !important;
            max-width: 300px;
            margin: 0 auto 1rem auto;
            display: block;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
            transition: 0.2s ease-in-out;
        }

        .stButton > button:hover {
            background-color: #AED7A0 !important;
            transform: scale(1.05);
        }

        h1, h2, h3, h4, h5, h6, p {
            color: black !important;
            text-align: center;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("**Calming Videos**")
    st.markdown("#### Pick a video to help you feel calm:")

    videos = [
        ("Beach ⛱", "https://www.youtube.com/watch?v=bn9F19Hi1Lk"),
        ("Forest 𖠰", "https://www.youtube.com/watch?v=xNN7iTA57jM"),
        ("Aquarium ଳ", "https://www.youtube.com/watch?v=gdJjc6l6iII"),
        ("Dance ♬", "https://www.youtube.com/watch?v=rPOB4MbjQmo"),
    ]

    if "selected_video" not in st.session_state:
        st.session_state.selected_video = None

    for idx, (label, url) in enumerate(videos):
        cols = st.columns([1, 3, 1])
        with cols[1]:
            if st.button(label, key=f"video_{idx}"):
                st.session_state.selected_video = url

    if st.session_state.selected_video:
        cols = st.columns([4, 1])
        with cols[0]:
            st.video(st.session_state.selected_video)
        with cols[1]:
            if st.button("Close", key="close_btn"):
                st.session_state.selected_video = None

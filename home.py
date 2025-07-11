import streamlit as st
from diary import show_diary
from games import show_games
from videos import show_videos
from imfeeling import show_activities
from report import show_report
from resources import show_resources
from therapist import show_therapist_info
from font import set_global_font
set_global_font()

st.set_page_config(page_title="My Feelings App")

# --- Show top banner only on home page ---
if "page" not in st.session_state or st.session_state.page == "home":
    st.markdown(
        """
        <div style="text-align: center; margin-top: -2rem;">
            <img src="https://i.ibb.co/fGZqhfBj/n7uyrdhk.png" style="width: 100%; max-height: 120px; object-fit: cover;">
        </div>
        """,
        unsafe_allow_html=True
    )

# --- White background and style overrides ---
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #ffffff !important;
    }

    * {
        color: #000000 !important;
    }

    [data-testid="stSelectbox"] {
        background-color: #FFE5B4;
        border-radius: 10px;
        padding: 10px;
    }

    .stButton > button {
        background-color: #FFE5B4 !important;
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
        background-color: #FFD9A0 !important;
        transform: scale(1.05);
    }

    h1, h2, h3 {
        font-family: inherit !important;
        font-weight: normal;
        text-align: center !important;
    }

    .main > div {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .button-container {
        max-width: 300px;
        width: 100%;
        margin-top: 20px;
        margin-bottom: 20px;
    }

    .radio-container {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }

    .stRadio > div > label {
        margin: 0 1rem;
        font-size: 1.1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# --- Return to Home Button ---
def return_home(from_page=None):
    col1, col2, col3 = st.columns([10, 1, 1])
    with col3:
        btn_key = f"return_home_{from_page}" if from_page else "return_home_default"
        if st.button("X", help="Return to Home", key=btn_key):
            st.session_state.page = "home"
            if from_page in ("report", "resources"):
                st.session_state.selected_role_tab = "Parent"
            else:
                st.session_state.selected_role_tab = "Child"


# --- Init Session State ---
if "page" not in st.session_state:
    st.session_state.page = "home"
if "selected_role_tab" not in st.session_state:
    st.session_state.selected_role_tab = "Child"


# --- Home View ---
if st.session_state.page == "home":
    st.title("Welcome to My Feelings App")

    st.markdown('<div class="radio-container">', unsafe_allow_html=True)
    selected_role = st.radio(
        "Select Account Type",
        options=["Child", "Parent"],
        index=0 if st.session_state.selected_role_tab == "Child" else 1,
        horizontal=True,
        key="selected_role_tab"
    )

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="button-container">', unsafe_allow_html=True)

    if selected_role == "Child":
        if st.button("Mood Diary"):
            st.session_state.page = "mood"
        if st.button("Games & Activities"):
            st.session_state.page = "games"
        if st.button("Calming Videos"):
            st.session_state.page = "videos"
        if st.button("I'm Feeling..."):
            st.session_state.page = "activities"
        # if st.button("Chat"):
        #     st.session_state.page = "chat"
    else:  # Parent buttons
        if st.button("Weekly Mood Report"):
            st.session_state.page = "report"
        if st.button("Resources"):
            st.session_state.page = "resources"
        if st.button("Therapist Info"):
            st.session_state.page = "therapist"

    st.markdown('</div>', unsafe_allow_html=True)


# --- Pages without white box ---
elif st.session_state.page == "mood":
    return_home()
    show_diary()

elif st.session_state.page == "report":
    return_home(from_page="report")
    show_report()


# --- Pages with white box layout ---
elif st.session_state.page == "therapist":
    return_home(from_page="therapist")
    show_therapist_info()

else:
    return_home(from_page=st.session_state.page)
    with st.container():
        st.markdown('<div class="white-box">', unsafe_allow_html=True)

        if st.session_state.page == "games":
            show_games()
        elif st.session_state.page == "videos":
            show_videos()
        elif st.session_state.page == "activities":
            show_activities()
        elif st.session_state.page == "resources":
            show_resources()
        # elif st.session_state.page == "chat":
        #     show_chat()

        st.markdown('</div>', unsafe_allow_html=True)

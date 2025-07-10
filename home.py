import streamlit as st
from diary import show_diary
from games import show_games
from videos import show_videos
from imfeeling import show_activities
from report import show_report
from resources import show_resources   # <- Import your resources page here

st.set_page_config(page_title="My Feelings App")

# --- Your full CSS styles + radio centering styles ---
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url('https://plus.unsplash.com/premium_photo-1668192066413-43a64d7b08d6?q=80&w=1935&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    * {
        color: #000000 !important;
    }

    [data-testid="stSelectbox"] {
        background-color: #FFE5B4;
        border-radius: 10px;
        padding: 10px;
    }

    /* Skinny buttons styling like videos page */
    .stButton > button {
        background-color: #FFE5B4 !important;  /* pastel orange */
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
        text-align: center !important;  /* Added this */
    }

    /* Center all content horizontally */
    .main > div {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    /* Buttons container with fixed width */
    .button-container {
        max-width: 300px;
        width: 100%;
        margin-top: 20px;
        margin-bottom: 20px;
    }

    /* Center radio buttons horizontally */
    .radio-container {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    /* Optional: spacing and size for radio labels */
    .stRadio > div > label {
        margin: 0 1rem;
        font-size: 1.1rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Return to Home Button for subpages
def return_home(from_page=None):
    col1, col2, col3 = st.columns([10, 1, 1])
    with col3:
        if st.button("X", help="Return to Home"):
            st.session_state.page = "home"
            # When returning from report or resources, switch tab to Parent
            if from_page in ("report", "resources"):
                st.session_state.selected_role_tab = "Parent"
            else:
                st.session_state.selected_role_tab = "Child"  # default

# Initialize session state
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
    else:
        if st.button("Weekly Mood Report"):
            st.session_state.page = "report"
        if st.button("Resources"):      # Added resources button here
            st.session_state.page = "resources"
    st.markdown('</div>', unsafe_allow_html=True)

# --- Subpages ---
elif st.session_state.page == "mood":
    return_home()
    show_diary()

elif st.session_state.page == "games":
    return_home()
    show_games()

elif st.session_state.page == "videos":
    return_home()
    show_videos()

elif st.session_state.page == "activities":
    return_home()
    show_activities()

elif st.session_state.page == "report":
    return_home(from_page="report")
    show_report()

elif st.session_state.page == "resources":      # New routing for resources
    return_home(from_page="resources")
    show_resources()


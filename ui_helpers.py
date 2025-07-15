import streamlit as st
import time

# Initialize session state variables
def init_globals():
    if "calm_mode" not in st.session_state:
        st.session_state.calm_mode = False
    if "start_time" not in st.session_state:
        st.session_state.start_time = time.time()
    if "last_reminder" not in st.session_state:
        st.session_state.last_reminder = time.time()

# Toggle Calm Mode on/off
def toggle_calm_mode():
    st.session_state.calm_mode = not st.session_state.calm_mode

# Render the Calm Mode (Night Mode) button
def render_calm_mode_toggle():
    label = "Night Mode" if not st.session_state.calm_mode else "Day Mode"
    if st.button(label):
        toggle_calm_mode()

# Apply Calm Mode styling (safe for all pages)
def apply_calm_mode_style():
    if st.session_state.calm_mode:
        st.markdown(
            """
            <style>
            [data-testid="stAppViewContainer"] {
                filter: brightness(80%) sepia(10%);
                transition: all 0.5s ease;
            }
            body {
                background-color: #f4f4f4 !important;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

# Show screen time reminder every 15 minutes
def check_screen_time_reminder(interval_minutes=15):
    elapsed = time.time() - st.session_state.start_time
    last_shown = time.time() - st.session_state.last_reminder
    if elapsed > interval_minutes * 60 and last_shown > interval_minutes * 60:
        st.session_state.last_reminder = time.time()
        st.warning(f"You’ve been using the app for about {int(elapsed // 60)} minutes. Want to take a break?")
        if st.button("Take a Break"):
            st.switch_page("breathing_page.py")  # Make sure this path matches your actual page filename

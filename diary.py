# diary.py
import streamlit as st
from datetime import date, timedelta



def show_diary():
    st.set_page_config(page_title="Mood Diary")

    st.markdown(
        """
        <style>
        /* Background image */
        [data-testid="stAppViewContainer"] {
            background-image: url('https://wallpapers.com/images/high/captivating-notebook-background-z1kbd2ft2q18mlzv.webp');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }

        /* Make all text black */
        body, div, p, span, label, h1, h2, h3, h4, h5, h6 {
            color: black !important;
            font-family: Arial, sans-serif;
        }

        /* Keep dropdown label and selected text white with monospace font */
        div[role="combobox"] label,
        div[role="combobox"] span {
            color: white !important;
            font-family: 'Courier New', monospace !important;
            font-weight: bold !important;
        }

        /* Save Mood button text white with monospace font */
        button[kind="primary"] > div {
            color: white !important;
            font-family: 'Courier New', monospace !important;
            font-weight: bold !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # 🎨 Emotion color map
    EMOTION_COLORS = {
        "Happy": "#FFD700",       # Yellow
        "Sad": "#87CEEB",         # Blue
        "Angry": "#FF6B6B",       # Red
        "Anxious": "#B39DDB",     # Purple
        "Bored": "#D3D3D3",       # Gray
        "Frustrated": "#FFB347",  # Orange
        "Calm": "#A8D5BA",        # Light Green
    }

    # Initialize mood log in session state
    if "mood_log" not in st.session_state:
        st.session_state.mood_log = {}

    st.title("**Mood Diary**")

    # --- 🌤 Mood Logging Input ---
    st.header("Log Your Mood Today")

    col1, col2 = st.columns(2)

    with col1:
        today = date.today()
        mood = st.selectbox("How are you feeling today?", list(EMOTION_COLORS.keys()))
        journal = st.text_area("Write about your day or what made you feel that way")

        if st.button("Save Mood"):
            st.session_state.mood_log[str(today)] = {
                "emotion": mood,
                "journal": journal
            }
            st.success("Mood saved!")

    # --- 📅 Mood Calendar View ---
    with col2:
        st.header("This Week’s Mood Map")

        week_dates = [date.today() - timedelta(days=i) for i in range(6, -1, -1)]
        for d in week_dates:
            date_str = str(d)
            if date_str in st.session_state.mood_log:
                entry = st.session_state.mood_log[date_str]
                color = EMOTION_COLORS.get(entry["emotion"], "#FFFFFF")
                st.markdown(f"""
                    <div style='background-color:{color}; padding:10px; border-radius:8px; margin-bottom:8px;'>
                        <strong>{d.strftime('%A')}</strong>: {entry['emotion']}
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                    <div style='background-color:#f0f0f0; padding:10px; border-radius:8px; margin-bottom:8px;'>
                        <strong>{d.strftime('%A')}</strong>: Not logged
                    </div>
                """, unsafe_allow_html=True)


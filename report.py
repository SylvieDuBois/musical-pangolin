import streamlit as st
from datetime import date, timedelta

def show_report():
    st.set_page_config(page_title="Parent Mood Viewer")

    # Sample stored mood log (replace with real data)
    if "mood_log" not in st.session_state:
        st.session_state.mood_log = {
            str(date.today() - timedelta(days=1)): {
                "emotion": "Happy",
                "journal": "Had a great day playing outside!"
            },
            str(date.today() - timedelta(days=2)): {
                "emotion": "Sad",
                "journal": "Missed my friend today."
            }
        }

    # Pastel color mapping for emotions
    EMOTION_COLORS = {
        "Happy": "#FFF9C4",
        "Sad": "#BBDEFB",
        "Angry": "#FFCDD2",
        "Anxious": "#D1C4E9",
        "Bored": "#E0E0E0",
        "Frustrated": "#FFE0B2",
        "Calm": "#C8E6C9",
    }

    st.markdown("""
        <style>
        /* Background image */
        [data-testid="stAppViewContainer"] {
            background-image: url('https://wallpapers.com/images/high/captivating-notebook-background-z1kbd2ft2q18mlzv.webp');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }

        body, div, p, span, label, h1, h2, h3, h4, h5, h6 {
            color: black !important;
        }

        .stSelectbox > div > div > div > select {
            background-color: #FDEBD0;
            color: black;
            font-weight: 600;
            padding: 8px;
            border-radius: 8px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("Parent View — Weekly Mood Log")

    week_dates = [date.today() - timedelta(days=i) for i in range(6, -1, -1)]
    week_str = [d.strftime("%A, %b %d") for d in week_dates]

    selected_day = st.selectbox("Select a day to view mood and notes:", week_str)
    selected_date = week_dates[week_str.index(selected_day)]
    selected_key = str(selected_date)

    if selected_key in st.session_state.mood_log:
        entry = st.session_state.mood_log[selected_key]
        bg_color = EMOTION_COLORS.get(entry["emotion"], "#FFFFFF")

        st.markdown(f"""
        <div style='
            background-color: {bg_color};
            padding: 20px;
            border-radius: 12px;
            margin-top: 15px;
            box-shadow: 3px 3px 8px rgba(0,0,0,0.1);
            color: black;
            font-family: Arial, sans-serif;
        '>
            <h3>Mood on {selected_day}: <span style="font-weight:bold;">{entry['emotion']}</span></h3>
            <p><strong>Notes:</strong> {entry['journal']}</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div style='
            background-color: #F0F0F0;
            padding: 20px;
            border-radius: 12px;
            margin-top: 15px;
            color: black;
            font-family: Arial, sans-serif;
        '>
            No mood logged for {selected_day}.
        </div>
        """, unsafe_allow_html=True)

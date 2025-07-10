import streamlit as st
from streamlit_drawable_canvas import st_canvas
import random

st.set_page_config(page_title="Games & Activities")

def show_games():  # ✅ Added missing colon
    # Custom styling
    st.markdown("""
        <style>
            [data-testid="stAppViewContainer"] {
                background: #FFF9F5 url('https://images.unsplash.com/photo-1544039578-7619e5bc1fe7?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D') no-repeat center center fixed;
                background-size: cover;
            }

            /* General text color */
            body, h1, h2, h3, h4, h5, h6, p, span, label, div, section, article {
                color: #000000 !important;
            }

            /* Centered select box */
            .dropdown-container {
                display: flex;
                justify-content: center;
                padding: 1rem;
            }

        </style>
    """, unsafe_allow_html=True)

    st.title("**Games & Activities**")
    st.markdown("#### Choose a game:")

    # Centered dropdown in yellow box
    st.markdown('<div class="dropdown-container"><div class="yellow-box">', unsafe_allow_html=True)
    game = st.selectbox("Select a game", [
        "54321 Grounding", "Fidget Game", "Emotions Game", "Drawing"
    ])
    st.markdown('</div></div>', unsafe_allow_html=True)

    # --- Game logic ---
    if game == "54321 Grounding":
        st.subheader("5-4-3-2-1 Grounding Game 👁")
        st.markdown("**Use your senses.**")

        see = st.text_area("5 Things You Can See", value="1.\n2.\n3.\n4.\n5.")
        hear = st.text_area("4 Things You Can Hear", value="1.\n2.\n3.\n4.")
        touch = st.text_area("3 Things You Can Touch", value="1.\n2.\n3.")
        smell = st.text_area("2 Things You Can Smell", value="1.\n2.")
        taste = st.text_area("1 Thing You Can Taste", value="1.")

        if st.button("Done", key="done_54321"):
            st.success("Good Job!")

    elif game == "Fidget Game":
        st.subheader("Fidget Game ᨒ")
        st.markdown("**Play with virtual rocks:**")
        st.markdown("[Click here to play the Fidget Game](https://neal.fun/rocks/)", unsafe_allow_html=True)

    elif game == "Emotions Game":
        st.subheader("Match the Situation to the Feeling")

        correct_matches = {
            "You just got a birthday present": "Happy",
            "Your friend didn’t talk to you today": "Sad",
            "Someone cut in line in front of you": "Angry",
            "You’re lying on a hammock listening to the breeze": "Calm",
            "You’re going to a theme park tomorrow": "Excited"
        }

        situations = list(correct_matches.keys())
        emotions = list(set(correct_matches.values()))
        random.seed(42)
        random.shuffle(emotions)

        user_matches = {}

        for situation in situations:
            user_matches[situation] = st.selectbox(
                f"How would you feel if: **{situation}**",
                emotions,
                key=f"match_{situation}"
            )

        if st.button("Submit Matches", key="submit_situation_match"):
            correct_count = sum(
                1 for sit, choice in user_matches.items() if correct_matches[sit] == choice
            )
            if correct_count == len(situations):
                st.success("Great job! You matched all correctly.")
            else:
                st.warning(f"You matched {correct_count} out of {len(situations)} correctly. Keep practicing!")

    elif game == "Drawing":
        st.subheader("Drawing Canvas ✎𓂃")
        st.markdown("**Draw something that makes you feel calm or happy!**")

        canvas_result = st_canvas(
            fill_color="rgba(255, 165, 0, 0.3)",  # Transparent orange
            stroke_width=3,
            stroke_color="#000000",
            background_color="#fff",
            height=400,
            width=700,
            drawing_mode="freedraw",
            key="drawing_canvas_dropdown_fix",
        )

        if canvas_result.image_data is not None:
            st.caption("Nice drawing!")
        else:
            st.info("Start drawing above!")

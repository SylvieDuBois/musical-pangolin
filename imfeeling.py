import streamlit as st
from streamlit_drawable_canvas import st_canvas
import random
from font import set_global_font
set_global_font()

def show_activities():
    st.set_page_config(page_title="I'm Feeling...")

    # Show top banner image only on this page
    st.markdown(
        """
        <div style="text-align: center; margin-top: -1rem;">
            <img src="https://i.ibb.co/JwDxVwBG/fay0kl6n.png" style="width: 100%; max-height: 120px; object-fit: cover;">
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("""
        <style>
        ...
            }

            * { color: #000000!important; }

            .stButton > button {
                background-color: #FFFFFF;
                color: black;
                border: none;
                padding: 0.6em 1.6em;
                border-radius: 12px;
                font-size: 1.1em;
                font-weight: 500;
                transition: 0.2s ease-in-out;
            }

            .stButton > button:hover {
                background-color: #fad2e1;
                transform: scale(1.02);
            }

            .dropdown-container {
                display: flex;
                justify-content: center;
                padding: 1rem;
            }
        </style>
    """, unsafe_allow_html=True)

    st.title("**𖡎 I'm feeling...**")

    # Dropdown menu in centered yellow box
    st.markdown('<div class="dropdown-container"><div class="yellow-box">', unsafe_allow_html=True)
    feeling = st.selectbox("How are you feeling?", [
        "Sad", "Angry", "Anxious", "Bored", "Happy", "Frustrated"
    ])
    st.markdown('</div></div>', unsafe_allow_html=True)

    # --- SAD ---
    if feeling == "Sad":
        st.subheader("You're feeling sad.")
        st.markdown("Try drawing your feelings, and enjoy the aquarium.")
        st.video("https://www.youtube.com/watch?v=gdJjc6l6iII")

        st.markdown("Draw how you feel:")
        canvas_result = st_canvas(
            fill_color="rgba(255, 165, 0, 0.3)",
            stroke_width=3,
            stroke_color="#000000",
            background_color="#ffffff",
            height=400,
            width=700,
            drawing_mode="freedraw",
            key="canvas_sad"
        )
        if canvas_result.image_data is not None:
            st.caption("Thank you for sharing!")

    # --- ANGRY ---
    elif feeling == "Angry":
        st.subheader("You're feeling angry.")
        st.markdown("Try blowing off some steam with the fidget game and then relax with the forest.")
        st.markdown("[Play the Fidget Game](https://neal.fun/rocks/)", unsafe_allow_html=True)
        st.video("https://www.youtube.com/watch?v=xNN7iTA57jM")

    # --- ANXIOUS ---
    elif feeling == "Anxious":
        st.subheader("You're feeling anxious.")
        st.markdown("Let's try the 5-4-3-2-1 game and calm down with nature.")
        st.video("https://www.youtube.com/watch?v=xNN7iTA57jM")

        see = st.text_area("5 Things You Can See", value="1.\n2.\n3.\n4.\n5.")
        hear = st.text_area("4 Things You Can Hear", value="1.\n2.\n3.\n4.")
        touch = st.text_area("3 Things You Can Touch", value="1.\n2.\n3.")
        smell = st.text_area("2 Things You Can Smell", value="1.\n2.")
        taste = st.text_area("1 Thing You Can Taste", value="1.")

        if st.button("Done Grounding", key="done_54321_anxious"):
            st.success("Well done!")

    # --- BORED ---
    elif feeling == "Bored":
        st.subheader("You're feeling bored.")
        st.markdown("Try the fidget game or make something on the drawing board!")
        st.markdown("[Play the Fidget Game](https://neal.fun/rocks/)", unsafe_allow_html=True)

        canvas_result = st_canvas(
            fill_color="rgba(255, 165, 0, 0.3)",
            stroke_width=3,
            stroke_color="#000000",
            background_color="#ffffff",
            height=400,
            width=700,
            drawing_mode="freedraw",
            key="canvas_bored"
        )
        if canvas_result.image_data is not None:
            st.caption("Cool drawing!")

    # --- HAPPY ---
    elif feeling == "Happy":
        st.subheader("You're feeling happy!")
        st.video("https://www.youtube.com/watch?v=rPOB4MbjQmo")
        st.text_input("What made you happy today?")
        st.markdown("Draw something joyful!")

        canvas_result = st_canvas(
            fill_color="rgba(255, 165, 0, 0.3)",
            stroke_width=3,
            stroke_color="#000000",
            background_color="#ffffff",
            height=400,
            width=700,
            drawing_mode="freedraw",
            key="canvas_happy"
        )
        if canvas_result.image_data is not None:
            st.caption("What a happy drawing!")

    # --- FRUSTRATED ---
    elif feeling == "Frustrated":
        st.subheader("You're feeling frustrated.")
        st.video("https://www.youtube.com/watch?v=bn9F19Hi1Lk")
        st.markdown("Try this emotion matching game:")

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
                st.success("Great job!")
            else:
                st.warning(f"You matched {correct_count} out of {len(situations)} correctly. Keep practicing!")

import streamlit as st

def show_resources():
    st.markdown(
        """
        <style>
        [data-testid="stAppViewContainer"] {
            background: url('https://plus.unsplash.com/premium_photo-1743513371075-7a13530234f8?q=80&w=1935&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D') no-repeat center center fixed;
            background-size: cover;
            background-attachment: fixed;
            filter: brightness(0.85);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("Parent Resources")

    if "resource_page" not in st.session_state:
        st.session_state.resource_page = "main"

    if st.session_state.resource_page == "main":
        st.markdown("### Select a resource topic:")

        if st.button("Understanding Therapy"):
            st.session_state.resource_page = "understanding"
            st.experimental_rerun()

        if st.button("Supporting Your Child at Home"):
            st.session_state.resource_page = "support"
            st.experimental_rerun()

        if st.button("At-Home Coping and Calming Strategies"):
            st.session_state.resource_page = "strategies"
            st.experimental_rerun()

    elif st.session_state.resource_page == "understanding":
        show_understanding()

    elif st.session_state.resource_page == "support":
        show_support()

    elif st.session_state.resource_page == "strategies":
        show_strategies()

def back_to_resources():
    if st.button("⬅ Back to Resources"):
        st.session_state.resource_page = "main"
  

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
   

def show_support():
    st.header("Supporting Your Child at Home")
    st.markdown("""
    Ways you can help your child outside therapy:
    - Recognize signs your child needs support (mood changes, withdrawal, irritability).
    - Use active listening to validate feelings.
    - Create a calm, predictable home environment.
    - Encourage healthy routines: sleep, nutrition, physical activity.
    """)
 

def show_strategies():
    st.header("At-Home Coping and Calming Strategies")
    st.markdown("""
    Practical tools to practice together:
    - **Grounding techniques:** Focus on the present moment using the 5-4-3-2-1 method.
    - **Breathing exercises:** Deep belly breathing to reduce anxiety.
    - **Creative outlets:** Drawing, journaling, music to express emotions.
    - **Setting up a calming space:** A quiet corner with comforting objects.
    """)
 

import streamlit as st

def show_therapist_info():
    st.title("Therapist Contact Information")

    # Initialize session state variables if not present
    if "therapist_name" not in st.session_state:
        st.session_state.therapist_name = ""
    if "therapist_phone" not in st.session_state:
        st.session_state.therapist_phone = ""
    if "therapist_email" not in st.session_state:
        st.session_state.therapist_email = ""
    if "therapist_office" not in st.session_state:
        st.session_state.therapist_office = ""

    with st.form("therapist_form"):
        name = st.text_input("Therapist Name", value=st.session_state.therapist_name)
        phone = st.text_input("Phone Number", value=st.session_state.therapist_phone)
        email = st.text_input("Email Address", value=st.session_state.therapist_email)
        office = st.text_area("Office Address", value=st.session_state.therapist_office)

        submitted = st.form_submit_button("Save")

        if submitted:
            st.session_state.therapist_name = name
            st.session_state.therapist_phone = phone
            st.session_state.therapist_email = email
            st.session_state.therapist_office = office
            st.success("Therapist info saved!")

    # Display saved info
    if st.session_state.therapist_name or st.session_state.therapist_phone or st.session_state.therapist_email or st.session_state.therapist_office:
        st.markdown("---")
        st.subheader("Saved Therapist Contact Info")
        st.write(f"**Name:** {st.session_state.therapist_name}")
        st.write(f"**Phone:** {st.session_state.therapist_phone}")
        st.write(f"**Email:** {st.session_state.therapist_email}")
        st.write(f"**Office:** {st.session_state.therapist_office}")

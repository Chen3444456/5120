import streamlit as st


def show_interface():
    st.write("2.1 User Story- Sunscreen reminders")
    if st.button('Return', key='return_from_sunscreen_reminders'):
        st.session_state.current_page = 'home'
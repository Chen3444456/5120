import streamlit as st


def show_interface():
    st.write("US1.3 Sunscreen reminders")
    if st.button('Return', key='return_from_sunscreen_set'):
        st.session_state.current_page = 'home'
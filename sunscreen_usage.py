import streamlit as st


def show_interface():
    st.write("US1.4 Sunscreen Usage")
    if st.button('Return', key='return_from_sunscreen_usage'):
        st.session_state.current_page = 'home'

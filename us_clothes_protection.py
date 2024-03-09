import streamlit as st


def show_interface():
    st.write("US1.2 US Clothes Protection")
    if st.button('Return', key='return_from_us_clothes_protection'):
        st.session_state.current_page = 'home'

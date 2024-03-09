import streamlit as st


def show_interface():
    st.write("US1.3 Data about UV impacts")
    if st.button('Return', key='return_from_uv_data_impacts'):
        st.session_state.current_page = 'home'

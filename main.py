import streamlit as st


import view_uv_level_locations,us_clothes_protection, uv_data_impacts, sunscreen_usage, sunscreen_reminders, sunscreen_set

def set_page_status(page_name):
    st.session_state.current_page = page_name

def show_main_page():
    st.header('Welcome to the sun protection page')
    if st.button('UV Level Locations', key='uv_level_locations_btn'):
        set_page_status('view_uv_level_locations')
    elif st.button('US Clothes Protection', key='us_clothes_protection_btn'):
        set_page_status('us_clothes_protection')
    elif st.button('Data about UV impacts',key= 'uv_data_impacts'):
        set_page_status('uv_data_impacts')
    elif st.button('Sunscreen Usage', key='sunscreen_usage'):
        set_page_status('sunscreen_usage')
    elif st.button('Sunscreen reminders',key='sunscreen_reminders'):
        set_page_status('sunscreen_reminders')
    elif st.button('sunscreen remder set',key = 'sunscreen_set'):
        set_page_status('sunscreen_set')

def main():
    if 'current_page' not in st.session_state:
        st.session_state['current_page'] = 'home'

    if st.session_state.current_page == 'home':
        show_main_page()
    elif st.session_state.current_page == 'view_uv_level_locations':
        view_uv_level_locations.view_uv_level_main()
    elif st.session_state.current_page == 'us_clothes_protection':
        us_clothes_protection.show_interface()
    elif st.session_state.current_page == 'uv_data_impacts':
        uv_data_impacts.show_interface()
    elif st.session_state.current_page == 'sunscreen_usage':
        sunscreen_usage.show_interface()
    elif st.session_state.current_page == 'sunscreen_reminders':
        sunscreen_reminders.show_interface()
    elif st.session_state.current_page == 'sunscreen_set':
        sunscreen_set.show_interface()

if __name__ == "__main__":
    main()

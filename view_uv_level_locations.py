# view_uv_level_locations.py
import streamlit as st
import mysql.connector
from mysql.connector import Error


# def view_uv_level_main():
#     st.title("View UV Index")
#
#     if st.button('Return', key='return_from_uv_level_locations'):
#         st.session_state.current_page = 'home'
#     else:
#         postcode = st.text_input("please input your postcode:")
#         suburb = st.text_input("please input your suburb")
#
#         if st.button("Get UV level"):
#             location_result =get_location(postcode,suburb)
#             if location_result:
#                 #get uv level
#                 uv_level = get_uv_level(location_result)
#                 st.write(f"The UV index for {suburb} ({postcode}) is: {uv_level}")
#             else:
#                 st.error("No location found for the given postcode and suburb.")



def view_uv_level_main():
    st.title("View UV Index")

    # Check if the return button is pressed, if so, change the page state.
    if 'return_pressed' not in st.session_state:
        st.session_state.return_pressed = False

    if st.button('Return', key='return_from_uv_level_locations'):
        st.session_state.return_pressed = True
        st.session_state.current_page = 'home'

    # Only show the postcode and suburb input if the return button has not been pressed.
    if not st.session_state.return_pressed:
        postcode = st.text_input("Please input your postcode:")
        suburb = st.text_input("Please input your suburb")

        if st.button("Get UV level"):
            location_result = get_location(postcode, suburb)
            if location_result:
                # Get UV level
                uv_level = get_uv_level(location_result)
                st.write(f"The UV index for {suburb} ({postcode}) is: {uv_level}")
            else:
                st.error("No location found for the given postcode and suburb.")


def get_location(postcode, suburb):
    '''Query Latitude and Longitude based on the postcode and suburb information in the database table'''
    # create db connection
    connection = check_database_connection()
    if connection is not None:
        try:
            # Create a cursor object
            cursor = connection.cursor()
            # execute the query
            query = "select Latitude, Longitude from SunSmart, location where postcode = %s and suburb =%s"
            cursor.execute(query, (postcode, suburb))
            result = cursor.fetchone()
            return result
        except Error as errorMessage:
            st.error(f"error message:" + errorMessage)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    return None

#result = get_location('800', 'Darwin')
# Latitude: -12.800, Longitude: 130.960
def get_uv_level(result):
    #将result转换
    lat = result[0]
    lon = result[1]
    print(lat,lon)
    #通过api获取相应的uv level





# Check whether the database connection is successful
def check_database_connection():
    """Check whether the database connection is successful"""
    try:
        connection = mysql.connector.connect(
            host='Database address',
            user='user',
            pwd='password',
            database='database name'
        )
        if connection.is_connected():
            conn_info = connection.get_server_info()
            print("The connection to mysql is successful, mysql information:", conn_info)
            return connection
    except Error as errorMessage:
        print("Connection failed! ! ! ! error message:", errorMessage)
        return False

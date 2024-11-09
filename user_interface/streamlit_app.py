import streamlit as st
import sys
import os
import requests


current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from app.config import Config


def main():
    st.title("Restaurant Name Generator")

    cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Italian", "Mexican", "Arabic", "American"))

    if cuisine:

        response = restaurant_data(cuisine)
        st.header(response['restaurant_name'])
        menu_items = response['menu_items'].split(",")
        print(response)

        st.write("**Menu Items**")
        for item in menu_items:
            st.write("-", item)
            print(item)


def restaurant_data(cuisine_type):
    url = f'{Config.API_URL}/generate'
    params = {'cuisine': cuisine_type}

    try:
        response = requests.get(url, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

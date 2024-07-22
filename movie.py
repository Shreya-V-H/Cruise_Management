import streamlit as st
import requests

# Streamlit App
st.title('Cruise Ship Management - Movie Booking')

# Fetch data from Flask API
response = requests.get('http://localhost:5000/api/movies')
if response.status_code == 200:
    movies = response.json()
    # Display movie information
    for movie in movies:
        st.subheader(movie['title'])
        st.write(f"**Description:** {movie['description']}")
        st.write(f"**Rating:** {movie['rating']}")
        st.write(f"**Timing:** {movie['timing']}")
        st.button(f"Book {movie['title']}")  # This can be linked to further booking functionality
else:
    st.error("Failed to fetch movies from the server.")

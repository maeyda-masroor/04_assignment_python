import streamlit as st
import requests

# Streamlit UI
st.title("🌦️ Weather App")
st.write("Enter a city name to get current weather data")

# User input
city = st.text_input("City Name")

# Replace with your own OpenWeatherMap API key
api_key = "544f179e3d863287ea23403438247324"

if st.button("Get Weather"):
    if city:
        # Call the API
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            temp = data['main']['temp']
            description = data['weather'][0]['description']
            humidity = data['main']['humidity']
            wind = data['wind']['speed']

            # Display results
            st.subheader(f"Weather in {city.title()}")
            st.write(f"Temperature: {temp}°C")
            st.write(f" Condition: {description}")
            st.write(f" Humidity: {humidity}%")
            st.write(f"Wind Speed: {wind} m/s")
        else:
            st.error("City not found or error retrieving data.")
    else:
        st.warning("Please enter a city name.")

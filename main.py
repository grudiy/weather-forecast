import streamlit as st
import plotly.express as px
from backend import get_data


# Add title, text, slider, selectbox
st.title("Weather Forecast App")
place = st.text_input("Place:")
days = st.slider("Forecast for Days: ", min_value=5, max_value=1,
                 help="Select the number of days you want to get forecast")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

if not place:
    st.subheader("Choose the place")

else:
    try:
        # Get data
        filtered_data = get_data(place, days)
        st.subheader(f"{option} for the next {days} days in {place.title()}")

        if option == "Temperature":
            # Create temperature plot
            temperatures = [dict["main"]["temp"] for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature"})
            st.plotly_chart(figure)

        if option == "Sky":
            # Draw img of the sky state
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=88)

    except KeyError:
        st.subheader("You entered not existing place")
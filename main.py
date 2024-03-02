import streamlit as st
import plotly.express as px

st.title("Weather Forecast App")
place = st.text_input("Place:")
days = st.slider("Forecast for Days: ", min_value=1, max_value=5,
                 help="Select the number of days you want to get forecast")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")


def get_data(days_period):
    dates = ["2023-10-25", "2023-10-26", "2023-10-30"]
    temperatures = ["10", "11", "-5"]
    return dates, temperatures


d, t = get_data(days)
figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature"})
st.plotly_chart(figure)

import streamlit as st

st.title("Weather Forecast App")
place = st.text_input("Place:")
days = st.slider("Forecast for Days: ", min_value=1, max_value=5,
                 help="Select the number of days you want to get forecast")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

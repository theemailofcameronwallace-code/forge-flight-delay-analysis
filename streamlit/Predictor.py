import pandas as pd
import numpy as np
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


predictor = pd.read_csv("Delay_predictor.csv")

predictor["Delayed"] = (predictor["ARRIVAL_DELAY"] > 5).astype(int)

df_encoded = pd.get_dummies(predictor, columns=['AIRLINE'])

x = df_encoded.drop(columns=["ARRIVAL_DELAY", "Delayed"])

y = df_encoded['Delayed']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state=42)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)


st.title("Flight Delay Predictor")
st.write("Can we predict future delays?")

month = st.selectbox(
    "Select Month",
    [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]
)

month_map = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}
month_num = month_map[month]

day_of_week = st.selectbox(
    "Select Day of Week",
    [
        "Sunday", "Monday", "Tuesday",
        "Wednesday", "Thursday",
        "Friday", "Saturday"
    ]
)

day_map = {
    "Sunday": 1,
    "Monday": 2,
    "Tuesday": 3,
    "Wednesday": 4,
    "Thursday": 5,
    "Friday": 6,
    "Saturday": 7
}

day_num = day_map[day_of_week]

departure_delay = st.number_input("Departure Delay", value=0)
taxi_out = st.number_input("Taxi Out Time", value=10)
distance = st.number_input("Distance", value=500)

airline_options = predictor["AIRLINE"].unique()

selected_airline = st.selectbox(
    "Select Airline", airline_options)

input_data = pd.DataFrame({
    "MONTH": [month_num],
    "DAY_OF_WEEK": [day_num],
    "DEPARTURE_DELAY": [departure_delay],
    "TAXI_OUT": [taxi_out],
    "DISTANCE": [distance]
})

input_data[f"AIRLINE_{selected_airline}"] = 1
input_data = input_data.reindex(columns=x.columns, fill_value=0)


if st.button("Predict Delay"):
    prediction = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0][1]

    if prediction ==1:
        st.error(f"Flight likely delayed({prob:.1%}probability)")
    else:
        st.success(f"Flight likely on time ({1-prob:.1%} confidence)")
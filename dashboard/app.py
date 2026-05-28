import streamlit as st
import pandas as pd

st.title("Flight Delay Predictor Dashboard")

uploaded_file = st.file_uploader("Upload Flight CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df.columns = df.columns.str.lower()

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    airline = st.selectbox("Select Airline", df["airline"].dropna().unique())

    if "month" in df.columns:
        month = st.selectbox("Select Month", sorted(df["month"].dropna().unique()))
    else:
        month = None

    filtered = df[df["airline"] == airline]

    avg_delay = filtered["arrival_delay"].mean()

    st.metric("Predicted Average Arrival Delay", f"{avg_delay:.2f} minutes")

    st.subheader("Average Delays by Airline")

    airline_delays = (
        df.groupby("airline")["arrival_delay"]
        .mean()
        .sort_values(ascending=False)
    )

    st.bar_chart(airline_delays)
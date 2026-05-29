import streamlit as st
import pandas as pd
import plotly.express as px


def show_delay_analysis():
    st.header("Delay Analysis")
    st.write(
        "This section analyzes which airlines had the worst average delays and which airlines created the largest total delay impact."
    )

    df = pd.read_csv("Delay_predictor.csv")
    df.columns = df.columns.str.lower()

    st.subheader("1. Airlines with Highest Average Arrival Delays")

    airline_delay = (
        df.groupby("airline", as_index=False)
        .agg(
            avg_arrival_delay=("arrival_delay", "mean"),
            avg_departure_delay=("departure_delay", "mean"),
            total_flights=("airline", "count"),
        )
        .sort_values("avg_arrival_delay", ascending=False)
    )

    fig1 = px.bar(
        airline_delay,
        x="airline",
        y="avg_arrival_delay",
        hover_data=["avg_departure_delay", "total_flights"],
        title="Average Arrival Delay by Airline",
        labels={
            "airline": "Airline",
            "avg_arrival_delay": "Average Arrival Delay (minutes)",
        },
    )

    st.plotly_chart(fig1, use_container_width=True)

    st.write(
        "This chart shows which airlines had the highest average arrival delays. "
        "It helps distinguish airlines with consistently higher delays from airlines that simply operate many flights."
    )

    st.subheader("2. Delay Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Average Arrival Delay",
            f"{df['arrival_delay'].mean():.2f} min"
        )

    with col2:
        st.metric(
            "Average Departure Delay",
            f"{df['departure_delay'].mean():.2f} min"
        )

    with col3:
        st.metric(
            "Longest Arrival Delay",
            f"{df['arrival_delay'].max():.0f} min"
        )

    st.write(
        "These summary metrics provide a quick snapshot of overall delay conditions in the dataset."
    )

    st.subheader("3. Airlines with Most Total Delay Minutes")

    total_delay_by_airline = (
        df.groupby("airline", as_index=False)
        .agg(
            total_arrival_delay=("arrival_delay", "sum"),
            total_flights=("airline", "count"),
        )
        .sort_values("total_arrival_delay", ascending=False)
    )

    fig2 = px.bar(
        total_delay_by_airline,
        x="airline",
        y="total_arrival_delay",
        hover_data=["total_flights"],
        title="Total Arrival Delay Minutes by Airline",
        labels={
            "airline": "Airline",
            "total_arrival_delay": "Total Arrival Delay Minutes",
        },
    )

    st.plotly_chart(fig2, use_container_width=True)

    st.write(
        "This chart shows total delay impact by airline. "
        "Airlines with more flights may accumulate more total delay minutes even if their average delay is not the highest."
    )
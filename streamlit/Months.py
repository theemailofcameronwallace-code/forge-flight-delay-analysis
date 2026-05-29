import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px


month_df = pd.read_csv("Busiest_months.csv")
days_df = pd.read_csv("Busiest_days.csv")
airlines_df = pd.read_csv("Busiest_airlines.csv")

def show_months():
    st.title("Flight Frequency per month")
    st.write("What Months have the most frequent flights?")
    
    fig1 = px.line(
        month_df,
        x="Month",
        y="TotalFlights",
        labels={
            "Month": "Month",
            "TotalFlights": "Number of Flights"
        },
        title="Flights by Month"
    )

    fig1.update_layout(xaxis_tickangle=45)

    st.plotly_chart(fig1, use_container_width=True)




    st.write("What Days of the week have the most frequent flights?")
    fig2 = px.bar(
        days_df,
        x="day of week",
        y="TotalFlights",
        text="TotalFlights",
        labels={
            "TotalFlights": "Number of Flights"
        },
        color = "day of week",
        color_discrete_map={
            "Monday": "blue",
            "Wednesday": "blue",
            "Thursday": "blue",
            "Tuesday": "lightblue",
            "Sunday": "lightblue",
            "Saturday": "lightblue",
            "Friday": "lightblue"
        },
        title="Flights by Day of the Week"  
    )

    fig2.update_layout(xaxis_tickangle=45)

    st.plotly_chart(fig2, use_container_width=True)


    st.write('Which Airlines have the most flights?')

    fig3 = px.bar(
        airlines_df,
        x="Airline",
        y="TotalFlights",
        text="TotalFlights",
        labels={
            "TotalFlights": "Number of Flights"
        },
        color = "ID",
        title="Busiest Airlines"  
    )

    fig3.update_layout(xaxis_tickangle=45)

    st.plotly_chart(fig3, use_container_width=True)

import streamlit as st

from Predictor import show_predictor
from Months import show_months
from DelayAnalysis import show_delay_analysis

st.title("Flight Delay Dashboard")
tab1, tab2, tab3 = st.tabs(
    ["Times of Frequent Flights", "Delay Analysis", "Predictor"]
)

with tab1:
    show_months()

with tab2:
    show_delay_analysis()

with tab3:
    show_predictor()
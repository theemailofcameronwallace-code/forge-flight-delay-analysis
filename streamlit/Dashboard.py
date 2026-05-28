import streamlit as st

from Predictor import show_predictor
from Months import show_months

st.title("Flight Delay Dashboard")
tab1, tab2 = st.tabs(["Times of Frequent Flights", "Predictor"])

with tab1:
    show_months()

with tab2:
    show_predictor()
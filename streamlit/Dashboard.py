import streamlit as st

from Predictor import show_predictor

st.title("Flight Delay Dashboard")
tab1 = st.tabs(["Predictor"])

with tab1[0]:
    show_predictor()
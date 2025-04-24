# ui/display.py

import streamlit as st
import pandas as pd

def display_data(df: pd.DataFrame):
    st.dataframe(df)
    st.subheader("📍 Map and Charts (Coming Soon...)")
    st.info("This is where your map and IPS visualizations will go.")

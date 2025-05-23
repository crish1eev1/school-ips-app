# app/logic/etl_trigger.py

import streamlit as st
import subprocess

def prompt_for_data():
    st.warning("No IPS data found in the database.")
    dept = st.text_input("Enter a department code to ingest (e.g., 75):")
    if st.button("Ingest data"):
        if dept:
            subprocess.run(["poetry", "run", "python", "etl/create_and_ingest.py", dept], check=True)
            st.success("✅ Data ingested!")
            st.cache_data.clear()  # Force Streamlit to clear all cached data
            st.rerun()
        else:
            st.error("Please provide a department code.")

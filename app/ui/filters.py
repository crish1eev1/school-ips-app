# app/ui/filters.py

import streamlit as st

def sidebar_filters():
    st.sidebar.header("📍 Filters")
    selected_type = st.sidebar.radio("School Type", ["All", "Public", "Private"])
    selected_dept = st.sidebar.text_input("Département code (e.g., 75)", max_chars=3)
    return selected_type, selected_dept

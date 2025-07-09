# app/main.py

import streamlit as st
from ui.filters import sidebar_filters
from ui.controls import handle_clear_db_button
from ui.display import display_data
from logic.database import table_exists, is_table_empty
from logic.data_loader import load_data
from logic.etl_trigger import prompt_for_data

st.set_page_config(page_title="School IPS Explorer", layout="wide")

st.title("📊 French Schools IPS")
st.markdown("Explore IPS data (Indice de Position Sociale) across schools for a specific city.")

# Get filter values
selected_type, selected_school_level = sidebar_filters()

# Handle clear DB button
handle_clear_db_button()

# Main logic
if not table_exists() or is_table_empty():
    prompt_for_data()
else:
    df = load_data(selected_type, selected_school_level)
    display_data(df)

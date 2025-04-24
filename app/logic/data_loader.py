# logic/data_loader.py

import streamlit as st
import pandas as pd
import sqlalchemy
from sqlalchemy import text
from config.settings import get_db_url

@st.cache_data
def load_data(selected_type):
    engine = sqlalchemy.create_engine(get_db_url())
    query = """
        SELECT 
            *
        FROM ips_ecoles
    """
    df = pd.read_sql_query(query, engine)

    if selected_type != "All":
        df = df[df["Type"] == selected_type]
    return df

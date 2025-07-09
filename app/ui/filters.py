# app/ui/filters.py

import streamlit as st
import sqlalchemy
from sqlalchemy import text
from config.settings import get_db_url

def sidebar_filters():
    st.sidebar.header("📍 Filters")
    
    engine = sqlalchemy.create_engine(get_db_url())
    types = []  # Default empty list

    # Check if table exists
    with engine.connect() as conn:
        table_check = conn.execute(text("""
            SELECT EXISTS (
                SELECT FROM information_schema.tables 
                WHERE table_name = 'ips_ecoles'
            )
        """))
        if table_check.scalar():
            result = conn.execute(text("SELECT DISTINCT secteur FROM ips_ecoles WHERE secteur IS NOT NULL"))
            types = sorted([row[0] for row in result.fetchall()])

    type_options = ["All"] + types
    selected_type = st.sidebar.radio("School Type", type_options)
    return selected_type


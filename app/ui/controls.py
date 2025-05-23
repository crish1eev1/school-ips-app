# app/ui/controls.py

import streamlit as st
import sqlalchemy
from sqlalchemy import text
from config.settings import get_db_url

def clear_database():
    engine = sqlalchemy.create_engine(get_db_url())
    with engine.connect().execution_options(isolation_level="AUTOCOMMIT") as conn:
        conn.execute(text("DROP TABLE IF EXISTS ips_ecoles"))
    st.success("✅ All data has been cleared from the database.")

def handle_clear_db_button():
    if "clear_db_confirmed" not in st.session_state:
        st.session_state.clear_db_confirmed = False

    if st.sidebar.button("🗑️ Clear IPS data from DB"):
        st.session_state.clear_db_confirmed = True

    if st.session_state.clear_db_confirmed:
        st.sidebar.warning("⚠️ This will permanently delete all IPS data.")
        col1, col2 = st.sidebar.columns(2)
        if col1.button("✅ Confirm"):
            clear_database()
            st.session_state.clear_db_confirmed = False
            st.rerun()
        if col2.button("❌ Cancel"):
            st.session_state.clear_db_confirmed = False

# app/main.py

import streamlit as st
import pandas as pd
import sqlalchemy
import subprocess
from sqlalchemy import text
from config.settings import get_db_url

st.set_page_config(page_title="School IPS Explorer", layout="wide")

st.title("📊 French Schools: Public vs Private Social Disparities")
st.markdown("Explore IPS data (Indice de Position Sociale) across public and private schools in France.")

# Sidebar UI
st.sidebar.header("📍 Filters")
selected_type = st.sidebar.radio("School Type", ["All", "Public", "Private"])
selected_dept = st.sidebar.text_input("Département code (e.g., 75)", max_chars=3)

# Session state for deletion confirmation
if "clear_db_confirmed" not in st.session_state:
    st.session_state.clear_db_confirmed = False

# Drop table with proper isolation level
def clear_database():
    engine = sqlalchemy.create_engine(get_db_url())
    with engine.connect().execution_options(isolation_level="AUTOCOMMIT") as conn:
        conn.execute(text("DROP TABLE IF EXISTS ips_ecoles"))
    st.success("✅ All data has been cleared from the database.")

# UI controls for clearing DB
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

# Data loading
@st.cache_data
def load_data():
    engine = sqlalchemy.create_engine(get_db_url())
    query = """
        SELECT 
            nom_etablissement AS "School Name",
            secteur AS "Type",
            academie AS "Region",
            ips AS "IPS"
        FROM ips_ecoles
        -- WHERE rentree_scolaire = '2022-2023'
    """
    df = pd.read_sql_query(query, engine)

    if selected_type != "All":
        df = df[df["Type"] == selected_type]
    return df

# Check if table exists
def table_exists():
    engine = sqlalchemy.create_engine(get_db_url())
    with engine.connect() as conn:
        result = conn.execute(text("""
            SELECT EXISTS (
                SELECT FROM information_schema.tables 
                WHERE table_name = 'ips_ecoles'
            )
        """))
        return result.scalar()

# Check if table is empty
def is_table_empty():
    engine = sqlalchemy.create_engine(get_db_url())
    with engine.connect() as conn:
        result = conn.execute(text("SELECT COUNT(*) FROM ips_ecoles"))
        return result.scalar() == 0

# Manual ETL trigger when no data
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

# App logic
if not table_exists() or is_table_empty():
    prompt_for_data()
else:
    df = load_data()
    st.dataframe(df)
    st.subheader("📍 Map and Charts (Coming Soon...)")
    st.info("This is where your map and IPS visualizations will go.")

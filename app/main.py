# app/main.py

import streamlit as st
import pandas as pd
import sqlalchemy
from sqlalchemy import text 
import subprocess

from config.settings import get_db_url

st.set_page_config(page_title="School IPS Explorer", layout="wide")

st.title("📊 French Schools: Public vs Private Social Disparities")
st.markdown("Explore IPS data (Indice de Position Sociale) across public and private schools in France.")

# Sidebar for filters
st.sidebar.header("📍 Filters")
selected_region = st.sidebar.selectbox("Choose a region", ["All", "Île-de-France", "Provence-Alpes-Côte d’Azur", "Nouvelle-Aquitaine"])
selected_type = st.sidebar.radio("School Type", ["All", "Public", "Private"])

# Data
st.subheader("📄 Dataset Preview (To Be Replaced)")
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
        WHERE rentree_scolaire = '2022-2023'
    """
    df = pd.read_sql_query(query, engine)
    
    # Apply filters
    if selected_region != "All":
        df = df[df["Region"] == selected_region]
    if selected_type != "All":
        df = df[df["Type"] == selected_type]
    
    return df


def check_and_populate_data():
    engine = sqlalchemy.create_engine(get_db_url())
    with engine.connect() as conn:
        # Encapsule la requête avec text()
        result = conn.execute(text("SELECT COUNT(*) FROM information_schema.tables WHERE table_name = 'ips_ecoles'"))
        table_exists = result.scalar() > 0

        if table_exists:
            result = conn.execute(text("SELECT COUNT(*) FROM ips_ecoles"))
            row_count = result.scalar()
        else:
            row_count = 0

        if row_count == 0:
            st.warning("No data found in `ips_ecoles`. Running ETL to populate data...")
            subprocess.run(["poetry", "run", "python", "etl/create_and_ingest.py"], check=True)

check_and_populate_data()
df = load_data()
st.dataframe(df)

# Placeholder for map / charts
st.subheader("📍 Map and Charts (Coming Soon...)")
st.info("This is where your map and IPS visualizations will go.")

import streamlit as st
import pandas as pd

st.set_page_config(page_title="School IPS Explorer", layout="wide")

st.title("📊 French Schools: Public vs Private Social Disparities")
st.markdown("Explore IPS data (Indice de Position Sociale) across public and private schools in France.")

# Sidebar for filters
st.sidebar.header("📍 Filters")
selected_region = st.sidebar.selectbox("Choose a region", ["All", "Île-de-France", "Provence-Alpes-Côte d’Azur", "Nouvelle-Aquitaine"])
selected_type = st.sidebar.radio("School Type", ["All", "Public", "Private"])

# Placeholder for data
st.subheader("📄 Dataset Preview (To Be Replaced)")
df = pd.DataFrame({
    "School Name": ["Lycée A", "Collège B", "École C"],
    "Type": ["Public", "Private", "Public"],
    "Region": ["Île-de-France", "Île-de-France", "Nouvelle-Aquitaine"],
    "IPS": [105, 130, 92],
})
st.dataframe(df)

# Placeholder for map / charts
st.subheader("📍 Map and Charts (Coming Soon...)")
st.info("This is where your map and IPS visualizations will go.")

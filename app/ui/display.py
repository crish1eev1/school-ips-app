# app/ui/display.py

import streamlit as st
import pandas as pd
import altair as alt

def display_data(df: pd.DataFrame):
    st.dataframe(df)

    st.subheader("📍 IPS Evolution Over Time")

    # Step 1: User selects a city
    city_options = sorted(df["nom_commune"].dropna().unique())
    selected_city = st.selectbox("Select a city (commune):", options=city_options)

    if selected_city:
        df_city = df[df["nom_commune"] == selected_city]

        # Step 2: User selects schools within that city
        school_options = sorted(df_city["nom_etablissement"].dropna().unique())
        selected_schools = st.multiselect(
            "Now select one or more schools to view their IPS evolution:",
            options=school_options,
            default=school_options  # Show all by default
        )

        if selected_schools:
            filtered_df = df_city[df_city["nom_etablissement"].isin(selected_schools)]
            plot_ips_evolution(filtered_df)
        else:
            st.info("Select at least one school.")
    else:
        st.info("Please select a city to begin.")


def plot_ips_evolution(df: pd.DataFrame):
    df = df.copy()
    df["rentree_scolaire"] = df["rentree_scolaire"].astype(str)
    df["ips"] = pd.to_numeric(df["ips"], errors="coerce")

    # Drop NaN IPS values to avoid issues in min/max
    df = df.dropna(subset=["ips"])

    if df.empty:
        st.info("No IPS data available to display.")
        return

    # Calculate min/max with padding
    ips_min = df["ips"].min()
    ips_max = df["ips"].max()
    padding = (ips_max - ips_min) * 0.05
    y_domain = [ips_min - padding, ips_max + padding]

    chart = alt.Chart(df).mark_line(point=True).encode(
        x=alt.X("rentree_scolaire:N", title="School Year"),
        y=alt.Y("ips:Q", title="IPS", scale=alt.Scale(domain=y_domain)),
        color=alt.Color("nom_etablissement:N", title="School"),
        tooltip=["nom_etablissement", "rentree_scolaire", "ips", "secteur"]
    ).properties(
        width=800,
        height=400,
        title=f"IPS Evolution for Schools in {df['nom_commune'].iloc[0]}"
    ).interactive()

    st.altair_chart(chart, use_container_width=True)
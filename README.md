# 🏫 School IPS App

📊 **Interactive app to explore social disparities between public and private schools in France**, using the Social Position Index (IPS).

Built with [Streamlit](https://streamlit.io), [Poetry](https://python-poetry.org), and [Docker](https://www.docker.com/).

---

## 🚀 Quickstart


### 🐳 Docker (with Docker Compose v2)

> Make sure you have the **Docker Compose Plugin v2** installed (`docker compose version` should show `v2.x.x`).

```bash
# Add yourself to the docker group if needed (then log out and back in)
sudo usermod -aG docker $USER

# Start the app
cd school-ips-app
docker compose down -v  # if needed
docker compose up --build
```

Then open 👈 http://localhost:8501

> If you get an error about port 5432 already being in use, kill the process:
>
> ```bash
> sudo lsof -i :5432
> sudo kill <PID>
> ```

---

### DBT

Open a shell inside the container and work interactively with dbt

```
docker exec -it school-ips-dbt bash 

dbt debug
dbt run
dbt test
```

Or, if done without ingestion on the app, run ingestion first:

```
# Ingest a single department (example: 75 = Paris)
docker compose run --rm app sh -lc "poetry run python etl/create_and_ingest.py 75"

# Run dbt
docker compose run --rm dbt run
---

## 🧱 Tech Stack

- 🐍 Python 3.10+
- 📊 Streamlit
- 🛆 Poetry
- 🐳 Docker + Docker Compose Plugin v2
- 🌍 Folium, GeoPandas, Plotly

---

## 📜 License

MIT

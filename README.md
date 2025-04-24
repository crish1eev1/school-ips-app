# 🏫 School IPS App

📊 **Interactive app to explore social disparities between public and private schools in France**, using the Social Position Index (IPS).

Built with [Streamlit](https://streamlit.io), [Poetry](https://python-poetry.org), and [Docker](https://www.docker.com/).

---

## 🚀 Quickstart

### 🔧 Local (with Poetry)

```bash
# Clone the repo
git clone git@github.com:crish1eev1/school-ips-app.git
cd school-ips-app

# Create virtual environment and install dependencies
poetry install

# Run the app
poetry run streamlit run app/main.py
```

Then open 👈 http://localhost:8501

---

### 🐳 Docker (with Docker Compose v2)

> Make sure you have the **Docker Compose Plugin v2** installed (`docker compose version` should show `v2.x.x`).

```bash
# Add yourself to the docker group if needed (then log out and back in)
sudo usermod -aG docker $USER

# Start the app
cd school-ips-app
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

### 📁 Project Structure

```
school-ips-app/
├── app/
│   └── main.py           # Main Streamlit app
├── config/               # DB config (get_db_url)
├── data_ingestion/       # Raw data fetching logic
├── transform/            # Data normalization logic
├── etl/                  # Create/ingest scripts
├── load/                 # DB insert logic
├── pyproject.toml        # Poetry dependencies
├── poetry.lock
├── Dockerfile
├── docker-compose.yml
└── README.md
```

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

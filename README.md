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

Then open 👉 http://localhost:8501

---

### 🐳 Docker

```bash
# Build the image
docker build -t school-ips-app .

# Run the container
docker run -it --rm -p 8501:8501 school-ips-app
```

Then open 👉 http://localhost:8501

---

### 📁 Project Structure

```
school-ips-app/
├── app/
│   └── main.py           # Main Streamlit app
├── pyproject.toml        # Poetry dependencies
├── poetry.lock
├── Dockerfile
└── README.md
```

---

## 🧱 Tech Stack

- 🐍 Python 3.10+
- 📊 Streamlit
- 📦 Poetry
- 🐳 Docker
- 🌍 Folium, GeoPandas, Plotly

---

## 📜 License

MIT

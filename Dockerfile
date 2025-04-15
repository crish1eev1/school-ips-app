# Dockerfile
FROM python:3.10-slim

# Set environment variables
ENV POETRY_VERSION=1.8.2 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install Poetry
RUN pip install "poetry==$POETRY_VERSION"

# Create app directory
WORKDIR /app

# Copy dependency files first
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry install --no-root

# Copy rest of the code
COPY . .

# Expose port
EXPOSE 8501

# Run the app
CMD ["sh", "-c", "poetry run streamlit run app/main.py --server.port=8501 --server.address=0.0.0.0"]

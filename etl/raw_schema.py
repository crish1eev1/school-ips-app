# etl/raw_schema.py

from sqlalchemy import Table, Column, String, DateTime, MetaData, text
from sqlalchemy.dialects.postgresql import JSONB

def ensure_raw_schema(engine):
    with engine.begin() as conn:
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS raw"))

def define_raw_table(metadata: MetaData, name: str) -> Table:
    # One table per dataset, storing the full API record in JSONB
    return Table(
        name, metadata,
        Column("id", String, primary_key=True),        # stable PK per record
        Column("dataset", String, nullable=False),     # "école" | "collège" | "lycée"
        Column("dept_code", String),                   # which dept we fetched
        Column("payload", JSONB, nullable=False),      # full API record
        Column("ingested_at", DateTime(timezone=True), server_default=text("now()")),
        schema="raw"
    )

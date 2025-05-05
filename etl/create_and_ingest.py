# etl/create_and_ingest.py
import sys
from sqlalchemy import create_engine, MetaData, Table, Column, String, Float, Integer, text
from data_ingestion.fetch_ips_data import fetch_all_records
from transform.normalize_ips import normalize_records
from config.settings import get_db_url
from sqlalchemy.dialects.postgresql import insert

def insert_records_to_db(engine, table, records):
    metadata = MetaData()
    metadata.create_all(engine, tables=[table])

    with engine.begin() as conn:
        for row in records:
            stmt = insert(table).values(**row).on_conflict_do_nothing(index_elements=['uai'])
            conn.execute(stmt)

def main():
    dept_code = sys.argv[1] if len(sys.argv) > 1 else None
    print("Creating DB connection...")
    engine = create_engine(get_db_url())

    metadata = MetaData()
    ips_table = Table('ips_ecoles', metadata,
        Column('uai', String, primary_key=True),
        Column('nom_etablissement', String),
        Column('ips', Float),
        Column('secteur', String),
        Column('academie', String),
        Column('departement', String),
        Column('code_du_departement', String),
        Column('code_insee', String),
        Column('nom_commune', String),
        Column('rentree_scolaire', String),
    )

    # ✅ Always ensure the table exists
    metadata.create_all(engine, tables=[ips_table])

    # ✅ Now it's safe to truncate it
    print("Clearing old data...")
    with engine.begin() as conn:
        conn.execute(text("TRUNCATE TABLE ips_ecoles"))

    print("Fetching raw data...")
    raw = fetch_all_records(dept_code=dept_code)

    print("Normalizing data...")
    normalized = normalize_records(raw, dept_code=dept_code)

    print("Inserting data...")
    insert_records_to_db(engine, ips_table, normalized)
    print("✅ Done!")



if __name__ == "__main__":
    main()
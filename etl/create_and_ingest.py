# etl/create_and_ingest.py

from data_ingestion.fetch_ips_data import fetch_all_2022_2023_records
from transform.normalize_ips import normalize_records
from sqlalchemy import create_engine, MetaData, Table, Column, String, Float, Integer, text
from sqlalchemy.dialects.postgresql import insert
from config.settings import get_db_url


def create_table_if_not_exists(engine):
    metadata = MetaData()

    ips_table = Table('ips_ecoles', metadata,
        Column('uai', String, primary_key=True),
        Column('nom_etablissement', String),
        Column('ips', Float),
        Column('ips_min', Float),
        Column('ips_max', Float),
        Column('ips_moy', Float),
        Column('nb_eleves', Integer),
        Column('secteur', String),
        Column('academie', String),
        Column('departement', String),
        Column('code_du_departement', String),
        Column('code_insee', String),
        Column('nom_commune', String),
        Column('geo_point', String),
        Column('rentree_scolaire', String),
    )

    metadata.create_all(engine)
    return ips_table


def insert_records_to_db(engine, table, records):
    with engine.begin() as conn:
        for row in records:
            stmt = insert(table).values(**row)
            stmt = stmt.on_conflict_do_nothing(index_elements=['uai'])
            conn.execute(stmt)


def main():
    print("Creating DB connection...")
    engine = create_engine(get_db_url())

    print("Ensuring table exists...")
    table = create_table_if_not_exists(engine)

    print("Fetching raw data...")
    raw = fetch_all_2022_2023_records()
    print(f"Fetched {len(raw)} records.")

    print("Normalizing data...")
    normalized = normalize_records(raw)

    print("Inserting data...")
    insert_records_to_db(engine, table, normalized)
    print("✅ Done!")


if __name__ == "__main__":
    main()

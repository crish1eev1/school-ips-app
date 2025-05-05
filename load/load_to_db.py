# load/load_to_db.py

from sqlalchemy import MetaData, Table, Column, String, Float, Integer
from sqlalchemy.dialects.postgresql import insert

def define_ips_table(metadata):
    return Table('ips_ecoles', metadata,
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

def insert_records_to_db(engine, table, records):
    with engine.connect() as conn:
        for row in records:
            stmt = insert(table).values(**row)
            stmt = stmt.on_conflict_do_nothing(index_elements=['uai'])
            conn.execute(stmt)

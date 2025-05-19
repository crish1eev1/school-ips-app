# load/load_to_db.py

from sqlalchemy import MetaData, Table, Column, String, Float, Integer
from sqlalchemy.dialects.postgresql import insert

def define_ips_table(metadata):
    return Table('ips_ecoles', metadata,
        Column('uai', String, primary_key=True),
        Column('nom_etablissement', String),
        Column('ips', Float),
        Column('ips_departemental_public', Float),
        Column('ips_academique', Float),
        Column('ips_departemental_prive', Float),
        Column('region', String),
        Column('rentree_scolaire', String),
        Column('code_insee', String),
        Column('nom_commune', String),
        Column('ips_academique_public', Float),
        Column('ips_national_prive', Float),
        Column('code_academie', String),
        Column('academie', String),
        Column('departement', String),
        Column('secteur', String),
        Column('code_du_departement', String),
        Column('ips_national_public', Float),
        Column('ips_national', Float),
        Column('code_region', String),
        Column('ips_departemental', Float),
        Column('ips_academique_prive', Float),
        Column('num_ligne', Float),
    )


def insert_records_to_db(engine, table, records):
    with engine.connect() as conn:
        for row in records:
            stmt = insert(table).values(**row)
            stmt = stmt.on_conflict_do_nothing(index_elements=['uai'])
            conn.execute(stmt)

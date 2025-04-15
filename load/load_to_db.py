# load/load_to_db.py

from sqlalchemy import create_engine, MetaData, Table, Column, String, Float, Integer
from sqlalchemy.dialects.postgresql import insert
from config.settings import get_db_url

def insert_records_to_db(records):
    engine = create_engine(get_db_url())
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

    with engine.connect() as conn:
        for row in records:
            stmt = insert(ips_table).values(**row)
            stmt = stmt.on_conflict_do_nothing(index_elements=['uai'])
            conn.execute(stmt)

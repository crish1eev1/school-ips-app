# etl/schema.py

from sqlalchemy import Table, Column, String, Float, MetaData, UniqueConstraint

def define_ips_table(metadata: MetaData) -> Table:
    return Table('ips_ecoles', metadata,
        Column('uai', String),
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
        UniqueConstraint('uai', 'rentree_scolaire', name='uai_year_unique')
    )

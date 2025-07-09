# etl/schema.py

from sqlalchemy import Table, Column, String, Float, MetaData, UniqueConstraint

def define_ips_table(metadata: MetaData) -> Table:
    return Table('ips_ecoles', metadata,
        Column('uai', String),                      # 0010005A
        Column('nom_etablissement', String),        # ECOLE ROGER POULNARD
        Column('type', String),                     # école
        Column('ips', Float),                       # 112.3
        Column('ips_departemental_public', Float),  # 105.9
        Column('ips_academique', Float),            # 109.6
        Column('ips_departemental_prive', Float),   # 123.9
        Column('region', String),                   # PAYS DE LA LOIRE
        Column('rentree_scolaire', String),         # 2023-2024
        Column('code_insee', String),               # 85194
        Column('nom_commune', String),              # LES SABLES D OLONNE
        Column('ips_academique_public', Float),     # 104.4
        Column('ips_national_prive', Float),        # 113.1
        Column('code_academie', String),            # 17
        Column('academie', String),                 # NANTES
        Column('departement', String),              # VENDEE
        Column('secteur', String),                  # public
        Column('code_du_departement', String),      # 85
        Column('ips_national_public', Float),       # 102.9
        Column('ips_national', Float),              # 105.5
        Column('code_region', String),              # 17
        Column('ips_departemental', Float),         # ips_departemental
        Column('ips_academique_prive', Float),      # ips_departemental_prive
        Column('num_ligne', Float),                 # 60002
        
        Column("ecart_type_de_l_ips", Float),
        Column("ips_etab", Float),
        Column("ips_voie_pro", Float),
        Column("ips_post_bac", Float),
        Column("type_de_lycee", String),
        Column("ecart_type_etablissement", Float),
        Column("ecart_type_voie_pro", Float),
        Column("ips_national_lp", Float),
        Column("ips_academique_lp", Float),
        Column("ips_departemental_lp", Float),
        
        UniqueConstraint('uai', 'rentree_scolaire', name='uai_year_unique')
    )

# load/load_to_db.py

from sqlalchemy import MetaData
from sqlalchemy.dialects.postgresql import insert
from etl.schema import define_ips_table

def insert_records_to_db(engine, records):
    metadata = MetaData()
    ips_table = define_ips_table(metadata)

    with engine.connect() as conn:
        for row in records:
            stmt = insert(ips_table).values(**row)
            stmt = stmt.on_conflict_do_nothing(index_elements=['uai', 'rentree_scolaire'])
            conn.execute(stmt)
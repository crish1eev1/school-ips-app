# etl/create_and_ingest.py 

import sys, hashlib
from sqlalchemy import create_engine, MetaData, text
from sqlalchemy.dialects.postgresql import insert
from data_ingestion.fetch_ips_data import fetch_all_records
from transform.normalize_ips import normalize_records
from config.settings import get_db_url
from etl.schema import define_ips_table
from etl.raw_schema import ensure_raw_schema, define_raw_table

def make_raw_id(dataset: str, fields: dict) -> str:
    # stable key: dataset|uai|rentree (fallback to md5 if missing)
    base = f"{dataset}|{fields.get('uai','')}|{fields.get('rentree_scolaire','')}"
    return hashlib.md5(base.encode()).hexdigest()

def load_raw(engine, records, dept_code):
    ensure_raw_schema(engine)
    md = MetaData()
    raw_ecoles   = define_raw_table(md, "raw_ips_ecoles")
    raw_colleges = define_raw_table(md, "raw_ips_colleges")
    raw_lycees   = define_raw_table(md, "raw_ips_lycees")
    md.create_all(engine, tables=[raw_ecoles, raw_colleges, raw_lycees])

    by_type = {"école": raw_ecoles, "collège": raw_colleges, "lycée": raw_lycees}

    with engine.begin() as conn:
        # Remove rows for the selected dept
        for tbl in [raw_ecoles, raw_colleges, raw_lycees]:
            conn.execute(text(f"DELETE FROM {tbl.schema}.{tbl.name} WHERE dept_code = :d"), {"d": dept_code})

        for rec in records:
            t = rec.get("school_type", "unknown")
            if t not in by_type:
                continue
            fields = rec.get("fields", {}) or {}
            rid = make_raw_id(t, fields)
            stmt = insert(by_type[t]).values(
                id=rid,
                dataset=t,
                dept_code=dept_code,
                payload=rec
            ).on_conflict_do_nothing(index_elements=["id"])
            conn.execute(stmt)

def insert_records_to_db(engine, table, records):
    md = MetaData()
    md.create_all(engine, tables=[table])
    with engine.begin() as conn:
        for row in records:
            stmt = insert(table).values(**row).on_conflict_do_nothing(index_elements=['uai', 'rentree_scolaire'])
            conn.execute(stmt)

def main():
    dept_code = sys.argv[1] if len(sys.argv) > 1 else None
    print("Creating DB connection...")
    engine = create_engine(get_db_url())

    # write RAW first
    print("Fetching raw data...")
    raw_records = fetch_all_records(dept_code=dept_code)
    print("Loading RAW payloads...")
    if dept_code:
        load_raw(engine, raw_records, dept_code=dept_code)

    print("Ensuring ips_ecoles exists...")
    md = MetaData()
    ips_table = define_ips_table(md)
    md.create_all(engine, tables=[ips_table])

    print("Clearing old normalized data...")
    with engine.begin() as conn:
        conn.execute(text("TRUNCATE TABLE ips_ecoles"))

    print("Normalizing data...")
    normalized = normalize_records(raw_records, dept_code=dept_code)

    print("Inserting normalized data...")
    insert_records_to_db(engine, ips_table, normalized)
    print("✅ Done!")

if __name__ == "__main__":
    main()

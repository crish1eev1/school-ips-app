# etl/ingest_ips.py

from data_ingestion.fetch_ips_data import fetch_all_2022_2023_records
from transform.normalize_ips import normalize_records
from load.load_to_db import insert_records_to_db

def main():
    print("Fetching IPS records...")
    raw = fetch_all_2022_2023_records()
    print(f"Fetched {len(raw)} records.")

    print("Normalizing records...")
    normalized = normalize_records(raw)

    print("Inserting into database...")
    insert_records_to_db(normalized)
    print("Done!")

if __name__ == "__main__":
    main()

# data_ingestion/fetch_ips_data.py
import requests

BASE_URL = "https://data.education.gouv.fr/api/records/1.0/search/"
DATASET = "fr-en-ips-ecoles-ap2022"
RENTREE = "2022-2023"

def fetch_all_2022_2023_records(batch_size=1000):
    all_records = []
    start = 0
    total_hits = None

    while True:
        params = {
            "dataset": DATASET,
            "rows": batch_size,
            "start": start,
            "refine.rentree_scolaire": RENTREE
        }

        try:
            response = requests.get(BASE_URL, params=params)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(f"❌ Error at start={start} → {e}")
            break

        data = response.json()

        if total_hits is None:
            total_hits = data.get("nhits", 0)
            print(f"→ Total expected records: {total_hits}")

        records = data.get("records", [])
        if not records:
            print(f"❌ No records returned at start={start}, breaking.")
            break

        all_records.extend(records)
        print(f"→ Got {len(records)} records at start={start}")

        start += batch_size
        if start >= total_hits:
            break

    return all_records

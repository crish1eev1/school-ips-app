# data_ingestion/fetch_ips_data.py
import requests

BASE_URL = "https://data.education.gouv.fr/api/records/1.0/search/"
DATASET = "fr-en-ips-ecoles-ap2022"
RENTREE = "2022-2023"

def fetch_all_2022_2023_records(batch_size=1000, dept_code=None):
    all_records = []
    start = 0

    while True:
        params = {
            "dataset": DATASET,
            "rows": batch_size,
            "start": start,
            "refine.rentree_scolaire": RENTREE,
        }
        if dept_code:
            params["refine.code_du_departement"] = dept_code

        response = requests.get(BASE_URL, params=params)
        if not response.ok:
            print(f"❌ Error at start={start} → {response.text}")
            break

        data = response.json()
        records = data.get("records", [])

        print(f"→ Got {len(records)} records at start={start}")
        if not records:
            break

        all_records.extend(records)

        if len(records) < batch_size:
            break

        start += batch_size

    print(f"✅ Fetched {len(all_records)} records.")
    return all_records

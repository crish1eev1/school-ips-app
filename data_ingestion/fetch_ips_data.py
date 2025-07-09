# data_ingestion/fetch_ips_data.py

import requests

BASE_URL = "https://data.education.gouv.fr/api/records/1.0/search/"
DATASETS = {
    "école": "fr-en-ips-ecoles-ap2022",
    "collège": "fr-en-ips-colleges-ap2023",
    "lycée": "fr-en-ips-lycees-ap2023",
}

def fetch_all_records(batch_size=1000, dept_code=None):
    all_records = []

    for school_type, dataset_id in DATASETS.items():
        start = 0
        while True:
            params = {
                "dataset": dataset_id,
                "rows": batch_size,
                "start": start,
            }
            if dept_code:
                params["refine.code_du_departement"] = dept_code

            response = requests.get(BASE_URL, params=params)
            if not response.ok:
                print(f"❌ Error for {school_type} at start={start} → {response.text}")
                break

            data = response.json()
            records = data.get("records", [])
            if not records:
                break

            # Inject type info in each record
            for record in records:
                record["school_type"] = school_type

            all_records.extend(records)
            if len(records) < batch_size:
                break
            start += batch_size

    print(f"✅ Fetched {len(all_records)} total records.")
    return all_records

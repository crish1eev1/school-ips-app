# transform/normalize_ips.py

def normalize_records(records, dept_code=None):
    normalized = []
    for rec in records:
        fields = rec.get("fields", {})
        record_dept = fields.get("code_du_departement")

        if dept_code and record_dept != dept_code:
            continue  # 🔥 Enforce dept_code filter

        normalized.append({
            "uai": fields.get("uai"),
            "nom_etablissement": fields.get("nom_de_l_etablissement"),  
            "ips": None if fields.get("ips") in ["NS", ""] else fields.get("ips"),
            "secteur": fields.get("secteur"),
            "academie": fields.get("academie"),
            "departement": fields.get("departement"),
            "code_du_departement": fields.get("code_du_departement"),
            "code_insee": fields.get("code_insee_de_la_commune"),
            "nom_commune": fields.get("nom_de_la_commune"),
            "rentree_scolaire": fields.get("rentree_scolaire"),
        })
    return normalized

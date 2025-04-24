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
            "nom_etablissement": fields.get("nom_etablissement"),
            "ips": None if fields.get("ips") in ["NS", ""] else fields.get("ips"),
            "ips_min": fields.get("ips_min"),
            "ips_max": fields.get("ips_max"),
            "ips_moy": fields.get("ips_moy"),
            "nb_eleves": fields.get("nb_eleves"),
            "secteur": fields.get("secteur"),
            "academie": fields.get("academie"),
            "departement": fields.get("departement"),
            "code_du_departement": fields.get("code_du_departement"),
            "code_insee": fields.get("code_insee_de_la_commune"),
            "nom_commune": fields.get("nom_de_la_commune"),
            "geo_point": str(fields.get("coordonnees")) if fields.get("coordonnees") else None,
            "rentree_scolaire": fields.get("rentree_scolaire"),
        })
    return normalized

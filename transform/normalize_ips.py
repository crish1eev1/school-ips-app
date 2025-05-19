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
            "ips": try_float(fields.get("ips")),
            "ips_departemental_public": try_float(fields.get("ips_departemental_public")),
            "ips_academique": try_float(fields.get("ips_academique")),
            "ips_departemental_prive": try_float(fields.get("ips_departemental_prive")),
            "region": fields.get("region"),
            "rentree_scolaire": fields.get("rentree_scolaire"),
            "code_insee": fields.get("code_insee_de_la_commune"),
            "nom_commune": fields.get("nom_de_la_commune"),
            "ips_academique_public": try_float(fields.get("ips_academique_public")),
            "ips_national_prive": try_float(fields.get("ips_national_prive")),
            "code_academie": fields.get("code_de_l_academie"),
            "academie": fields.get("academie"),
            "departement": fields.get("departement"),
            "secteur": fields.get("secteur"),
            "code_du_departement": fields.get("code_du_departement"),
            "ips_national_public": try_float(fields.get("ips_national_public")),
            "ips_national": try_float(fields.get("ips_national")),
            "code_region": fields.get("code_region"),
            "ips_departemental": try_float(fields.get("ips_departemental")),
            "ips_academique_prive": try_float(fields.get("ips_academique_prive")),
            "num_ligne": fields.get("num_ligne"),
        })
    return normalized

def try_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


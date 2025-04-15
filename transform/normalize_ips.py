# transform/normalize_ips.py

def to_float(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return None

def normalize_records(records):
    normalized = []
    for rec in records:
        fields = rec.get("fields", {})
        normalized.append({
            "uai": fields.get("uai"),
            "nom_etablissement": fields.get("nom_etablissement"),
            "ips": to_float(fields.get("ips")),
            "ips_min": to_float(fields.get("ips_min")),
            "ips_max": to_float(fields.get("ips_max")),
            "ips_moy": to_float(fields.get("ips_moy")),
            "nb_eleves": fields.get("nb_eleves"),
            "secteur": fields.get("secteur"),
            "academie": fields.get("academie"),
            "departement": fields.get("departement"),
            "code_du_departement": fields.get("code_du_departement"),
            "code_insee": fields.get("code_insee_de_la_commune"),
            "nom_commune": fields.get("nom_de_la_commune"),
            "geo_point": fields.get("coordonnees"),
            "rentree_scolaire": fields.get("rentree_scolaire"),
        })
    return normalized


# transform/normalize_ips.py

def normalize_records(records, dept_code=None):
    normalized = []
    for rec in records:
        fields = rec.get("fields", {})
        record_dept = fields.get("code_du_departement")
        record_type = rec.get("school_type", "unknown")

        if dept_code and record_dept != dept_code:
            continue

        normalized.append({
            "type": record_type,
            "uai": fields.get("uai"),
            "nom_etablissement": fields.get("nom_de_l_etablissement"),
            "ips": try_float(fields.get("ips")) or fields.get("ips_etab"),
            "ips_etab": try_float(fields.get("ips_etab")),
            "ips_voie_pro": try_float(fields.get("ips_voie_pro")),
            "ips_post_bac": try_float(fields.get("ips_post_bac")),
            "ecart_type_de_l_ips": try_float(fields.get("ecart_type_de_l_ips")),
            "ecart_type_etablissement": try_float(fields.get("ecart_type_etablissement")),
            "type_de_lycee": fields.get("type_de_lycee"),
            "rentree_scolaire": fields.get("rentree_scolaire"),
            "code_region": fields.get("code_region"),
            "region": fields.get("region") or fields.get("region_academique"),
            "code_academie": fields.get("code_de_l_academie") or fields.get("code_academie"),
            "academie": fields.get("academie"),
            "code_du_departement": fields.get("code_du_departement"),
            "departement": fields.get("departement"),
            "code_insee": fields.get("code_insee_de_la_commune"),
            "nom_commune": fields.get("nom_de_la_commune"),
            "secteur": fields.get("secteur"),
            "ips_national": try_float(fields.get("ips_national")),
            "ips_national_public": try_float(fields.get("ips_national_public")),
            "ips_national_prive": try_float(fields.get("ips_national_prive")),
            "ips_academique": try_float(fields.get("ips_academique")),
            "ips_academique_public": try_float(fields.get("ips_academique_public")),
            "ips_academique_prive": try_float(fields.get("ips_academique_prive")),
            "ips_departemental": try_float(fields.get("ips_departemental")),
            "ips_departemental_public": try_float(fields.get("ips_departemental_public")),
            "ips_departemental_prive": try_float(fields.get("ips_departemental_prive")),
            "num_ligne": fields.get("num_ligne"),
        })
    return normalized

def try_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


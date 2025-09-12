with base as (
  select * from {{ source('public', 'ips_ecoles') }}
)
select
  uai,
  rentree_scolaire,
  nom_etablissement,
  type,
  nom_commune,
  secteur,
  ips,
  (uai || '-' || rentree_scolaire) as uai_rentree_unique
from base

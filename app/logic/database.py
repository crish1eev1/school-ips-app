# app/logic/database.py

import sqlalchemy
from sqlalchemy import text
from config.settings import get_db_url

def table_exists():
    engine = sqlalchemy.create_engine(get_db_url())
    with engine.connect() as conn:
        result = conn.execute(text("""
            SELECT EXISTS (
                SELECT FROM information_schema.tables 
                WHERE table_name = 'ips_ecoles'
            )
        """))
        return result.scalar()

def is_table_empty():
    engine = sqlalchemy.create_engine(get_db_url())
    with engine.connect() as conn:
        result = conn.execute(text("SELECT COUNT(*) FROM ips_ecoles"))
        return result.scalar() == 0

# config/settings.py

import os

def get_db_url():
    return os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/school_ips")

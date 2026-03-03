"""Application configuration — intentionally insecure."""

import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://payflow:payflow@localhost:5432/payflow")
SECRET_KEY = "super-secret-key-do-not-use"
ALGORITHM = "HS256"

# api/index.py
# Eksportujemy WSGI app o nazwie "app" – tego szuka Vercel.
from app import app as app  # noqa: F401
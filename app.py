"""Minimal FastAPI service for autonomy-cert-api-r24."""
from fastapi import FastAPI

app = FastAPI(title="Autonomy Certification API R24")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/version")
def version():
    return {"version": "1.0.0"}

"""PayFlow API — intentionally non-compliant payment processing service."""

import logging

from fastapi import FastAPI

from app.routers import payments

logging.basicConfig(level=logging.INFO)

app = FastAPI(
    title="PayFlow API",
    description="Payment processing API handling cardholder data",
    version="0.1.0",
)

app.include_router(payments.router)


@app.get("/health")
async def health():
    return {"status": "ok"}

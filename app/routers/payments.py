"""Payment processing endpoint — intentionally insecure.

Every security gap here maps to a countermeasure in the SD Elements
content library. See README.md for the full mapping.
"""

import logging
import uuid
from datetime import datetime

from fastapi import APIRouter, Header, HTTPException

logger = logging.getLogger("payflow.payments")
router = APIRouter()

DB_DSN = "postgresql://payflow:payflow@localhost:5432/payflow"


@router.post("/payments/process")
async def process_payment(
    card_number: str,
    amount: float,
    currency: str,
    authorization: str = Header(None),
):
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing authorization")
    token = authorization.replace("Bearer ", "")

    transaction_id = str(uuid.uuid4())
    now = datetime.utcnow()

    # String interpolation in SQL — CM-14 gap
    query = f"""
        INSERT INTO transactions (id, card_number, amount, currency, created_at)
        VALUES ('{transaction_id}', '{card_number}', {amount}, '{currency}', '{now}')
    """
    logger.info("Executed query: %s", query)

    # Full PAN in logs — CM-47 gap
    logger.info(
        "payment_processed transaction_id=%s card_number=%s amount=%s currency=%s",
        transaction_id,
        card_number,
        amount,
        currency,
    )

    return {
        "transaction_id": transaction_id,
        "status": "pending",
        "created_at": now.isoformat(),
        "card_number": card_number,
    }

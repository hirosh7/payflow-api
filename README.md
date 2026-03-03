# PayFlow API

A **deliberately insecure** payment processing API built with Python/FastAPI.

This application is the demo target for the SD Elements AI digital twin. Every security gap is intentional and maps to a specific countermeasure in the SD Elements content library.

## What This Is

A `POST /payments/process` endpoint that:
- Accepts `card_number`, `amount`, and `currency`
- Validates the request
- Stores the transaction in PostgreSQL
- Returns a transaction ID

## What's Intentionally Wrong

| Gap | What's Missing | CM ID |
|-----|---------------|-------|
| SQL Injection | String interpolation in queries | CM-14 |
| No Input Validation | Raw strings, no length/format checks | CM-31 |
| PAN in Logs | Full card number logged | CM-47 |
| No JWT Validation | Token accepted without verification | CM-52 |
| No Rate Limiting | Endpoint has no throttling | CM-88 |

## Stack

- **Language:** Python 3.12
- **Framework:** FastAPI
- **Database:** PostgreSQL
- **Cloud:** AWS Lambda (intended)
- **Auth:** OAuth2 + JWT (broken)
- **Data:** Cardholder data (PCI-DSS scope), PII

## Running

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Purpose

This repo exists solely as a demo target. **Do not deploy this anywhere.**

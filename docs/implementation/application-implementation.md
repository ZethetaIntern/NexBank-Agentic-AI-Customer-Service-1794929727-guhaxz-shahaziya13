# NexBank Application Implementation

## Implementation scope

This repository now includes a locally runnable FastAPI demonstration prototype.

Implemented components:

1. REST customer conversation endpoint.
2. Deterministic baseline intent classifier.
3. In-memory dialogue state.
4. Approved-public knowledge retrieval.
5. Separate demo verification endpoint.
6. Suspected-fraud P0 escalation.
7. Separate complaint case creation.
8. Customer feedback collection.
9. JSON Lines audit events.
10. Automated API tests.

## Run locally

Install dependencies:

    python -m pip install -r requirements.txt

Start the API:

    python -m uvicorn app.main:app --reload

Open interactive API documentation:

    http://127.0.0.1:8000/docs

Health check:

    http://127.0.0.1:8000/health

## Demo verification

The local-only demo OTP is 246810.

Use POST:

    /sessions/{session_id}/verify-demo

with:

    {"code": "246810"}

A customer message claiming OTP completion does not authenticate a session.

## Chat example

POST /chat

    {
      "session_id": "demo-001",
      "message": "I want to check my savings balance"
    }

## Feedback example

POST /feedback

    {
      "session_id": "demo-001",
      "rating": 5,
      "comment": "Helpful demonstration"
    }

## Run tests

    python -m unittest discover -s tests -v

## Limitations

- No live banking, payment, card, identity or OTP integration.
- The OTP endpoint is a demonstration mechanism only.
- Intent classification is deterministic and keyword-based, not a trained NLU model.
- Retrieval is lexical, not dense-vector or hybrid retrieval.
- Sessions, cases and feedback are held in memory and reset on restart.
- No actual human queue or agent receives the simulated escalation.
- Feedback is recorded but does not train or update a model.
- The synthetic balance is not customer data.
- This prototype is not production-ready and must not process real customer information.

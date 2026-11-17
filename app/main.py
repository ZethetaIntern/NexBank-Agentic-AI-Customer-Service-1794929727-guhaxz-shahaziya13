import csv
import json
import os
import re
import uuid
from datetime import datetime, timezone
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
RUNTIME_DIR = DATA_DIR / "runtime"
KB_FILE = DATA_DIR / "approved_demo_knowledge.csv"
AUDIT_FILE = RUNTIME_DIR / "audit_log.jsonl"

RUNTIME_DIR.mkdir(parents=True, exist_ok=True)

app = FastAPI(
    title="NexBank Agentic AI Customer Service",
    description=(
        "Local demonstration prototype using synthetic banking data. "
        "Not connected to live banking systems."
    ),
    version="1.0.0"
)

# In-memory state is suitable for this local prototype only.
sessions = {}
cases = {}
feedback_events = []


class ChatRequest(BaseModel):
    session_id: str = Field(min_length=3, max_length=100)
    message: str = Field(min_length=1, max_length=3000)


class DemoVerifyRequest(BaseModel):
    code: str = Field(min_length=1, max_length=20)


class FeedbackRequest(BaseModel):
    session_id: str = Field(min_length=3, max_length=100)
    rating: int = Field(ge=1, le=5)
    comment: str = Field(default="", max_length=1000)


def now():
    return datetime.now(timezone.utc).isoformat()


def audit(event_type, session_id, details=None):
    """Append a minimal, timestamped audit event."""
    record = {
        "event_id": str(uuid.uuid4()),
        "timestamp": now(),
        "event_type": event_type,
        "session_id": session_id,
        "details": details or {}
    }

    with AUDIT_FILE.open("a", encoding="utf-8") as file:
        file.write(json.dumps(record, ensure_ascii=False) + "\n")


def get_session(session_id):
    if session_id not in sessions:
        sessions[session_id] = {
            "verified": False,
            "turns": [],
            "active_fraud_case": None,
            "complaint_case": None
        }
    return sessions[session_id]


def detect_intent(message):
    """
    Deterministic baseline classifier.
    A production deployment would require a trained and evaluated NLU model.
    """
    text = message.lower()

    fraud_patterns = [
        r"\bnot mine\b",
        r"\bdid not make\b",
        r"\bdidn't make\b",
        r"\bunauthori[sz]ed\b",
        r"\bunfamiliar debit\b",
        r"\bsuspicious transaction\b",
        r"\bfraud\b",
        r"\bstolen card\b"
    ]

    if any(re.search(pattern, text) for pattern in fraud_patterns):
        return "SEC-001", "suspected_fraud"

    if any(word in text for word in [
        "balance", "account balance", "available amount"
    ]):
        return "ACC-001", "account_balance"

    if any(word in text for word in [
        "complaint", "complain", "unhappy with service",
        "formal complaint"
    ]):
        return "CMP-001", "complaint"

    if any(word in text for word in [
        "block my card", "lost my card", "card stolen"
    ]):
        return "SEC-002", "card_security"

    if any(word in text for word in [
        "transaction status", "payment status", "pending transaction"
    ]):
        return "TXN-001", "transaction_status"

    if any(word in text for word in [
        "credit card", "loan", "interest rate", "product",
        "savings account features"
    ]):
        return "PRD-001", "product_information"

    if any(word in text for word in [
        "hello", "hi", "good morning", "hey"
    ]):
        return "GEN-001", "greeting"

    return "GEN-003", "general_query"


def retrieve_knowledge(query):
    """Simple lexical retrieval over approved public demo knowledge."""
    if not KB_FILE.exists():
        return None

    query_terms = set(re.findall(r"[a-z0-9]+", query.lower()))
    candidates = []

    with KB_FILE.open("r", encoding="utf-8-sig", newline="") as file:
        for item in csv.DictReader(file):
            if item.get("status", "").lower() != "approved":
                continue

            if item.get("access_level", "").lower() != "public":
                continue

            searchable = (
                item.get("title", "") + " " +
                item.get("content", "") + " " +
                item.get("keywords", "")
            ).lower()

            terms = set(re.findall(r"[a-z0-9]+", searchable))
            score = len(query_terms.intersection(terms))

            if score > 0:
                candidates.append((score, item))

    if not candidates:
        return None

    candidates.sort(key=lambda item: item[0], reverse=True)
    return candidates[0][1]


def create_case(session_id, intent, priority, queue, summary):
    case_id = "CASE-" + uuid.uuid4().hex[:10].upper()

    case = {
        "case_id": case_id,
        "session_id": session_id,
        "intent": intent,
        "priority": priority,
        "queue": queue,
        "status": "pending_human",
        "summary": summary,
        "created_at": now()
    }

    cases[case_id] = case

    audit("case_created", session_id, {
        "case_id": case_id,
        "intent": intent,
        "priority": priority,
        "queue": queue
    })

    return case


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "application": "NexBank Customer Service Prototype",
        "version": "1.0.0",
        "demo_mode": True,
        "live_banking_connection": False
    }


@app.post("/sessions/{session_id}/verify-demo")
def verify_demo(session_id: str, request: DemoVerifyRequest):
    """
    DEMO ONLY. This is not real OTP authentication.
    Production authentication must use a trusted bank identity service.
    """
    if os.getenv("DEMO_MODE", "true").lower() != "true":
        raise HTTPException(
            status_code=404,
            detail="Demo verification is disabled."
        )

    expected = os.getenv("DEMO_OTP", "246810")

    if request.code != expected:
        audit("demo_authentication_failed", session_id)
        raise HTTPException(status_code=401, detail="Invalid demo code.")

    session = get_session(session_id)
    session["verified"] = True

    audit("demo_authentication_succeeded", session_id)

    return {
        "session_id": session_id,
        "verified": True,
        "mode": "SIMULATION ONLY",
        "message": "Demo verification completed. Not real banking authentication."
    }


@app.post("/chat")
def chat(request: ChatRequest):
    session = get_session(request.session_id)
    message = request.message.strip()

    intent_id, intent_name = detect_intent(message)

    session["turns"].append({
        "intent": intent_id,
        "timestamp": now()
    })

    response = ""
    action = "respond"
    escalation = None

    # Highest priority: suspected fraud.
    if intent_id == "SEC-001":
        if not session["active_fraud_case"]:
            fraud_case = create_case(
                request.session_id,
                "SEC-001",
                "P0",
                "Fraud Investigation",
                "Suspected unauthorised transaction reported by customer."
            )
            session["active_fraud_case"] = fraud_case["case_id"]
        else:
            fraud_case = cases[session["active_fraud_case"]]

        escalation = fraud_case
        action = "human_escalation"

        response = (
            "I understand your concern. I am treating this as a potential "
            "fraud issue. Your case is marked for the Fraud Investigation "
            "team with P0 priority. Please do not share your PIN, password "
            "or CVV in this chat. This is a simulated handoff; no live bank "
            "team has been contacted."
        )

    elif intent_id == "ACC-001":
        if not session["verified"]:
            response = (
                "I can help with your account balance. Please complete "
                "the secure verification process first. For this local "
                "prototype, use the separate demo verification endpoint. "
                "A message claiming OTP completion does not authenticate "
                "your session."
            )
            action = "authentication_required"
        else:
            response = (
                "The synthetic demo savings balance is INR 25,400.00. "
                "This is sample data and is not a real customer account."
            )
            action = "demo_balance_response"

    elif intent_id == "CMP-001":
        if not session["complaint_case"]:
            complaint = create_case(
                request.session_id,
                "CMP-001",
                "P2",
                "Customer Complaints",
                "Customer requested a formal complaint."
            )
            session["complaint_case"] = complaint["case_id"]
        else:
            complaint = cases[session["complaint_case"]]

        action = "complaint_recorded"

        if session["active_fraud_case"]:
            response = (
                "Your complaint request has been recorded as a separate "
                "simulated case. Your suspected fraud case remains the "
                "higher-priority P0 case. Both require human follow-up."
            )
        else:
            response = (
                "Your complaint request has been recorded in this "
                "simulation for human review. No real complaint has "
                "been submitted to a bank."
            )

    elif intent_id == "TXN-001":
        response = (
            "I can help with a transaction-status query. If you believe "
            "the transaction was not authorised by you, tell me so that "
            "the security escalation process can be triggered."
        )

    elif intent_id == "SEC-002":
        response = (
            "For a lost or stolen card, contact your bank through its "
            "official verified channel to block it. This prototype "
            "cannot block cards or perform account changes."
        )
        action = "security_guidance"

    elif intent_id == "PRD-001":
        result = retrieve_knowledge(message)

        if result:
            response = result.get("content", "")
            action = "knowledge_retrieval"
        else:
            response = (
                "I could not find an approved public knowledge entry "
                "for that question. I do not want to guess. Please "
                "contact an authorised support representative."
            )
            action = "knowledge_not_found"

    elif intent_id == "GEN-001":
        response = (
            "Hello! I am NexBank's AI customer-service prototype. "
            "I can help with general queries and simulated support "
            "workflows. I can also explain when human assistance is needed."
        )

    else:
        response = (
            "I am not confident enough to answer that accurately. "
            "Could you rephrase your question or ask for human support?"
        )
        action = "clarification_required"

    audit("chat_turn", request.session_id, {
        "intent": intent_id,
        "intent_name": intent_name,
        "action": action,
        "turn_number": len(session["turns"]),
        "case_id": escalation["case_id"] if escalation else None
    })

    return {
        "session_id": request.session_id,
        "intent_id": intent_id,
        "intent_name": intent_name,
        "response": response,
        "action": action,
        "authenticated": session["verified"],
        "turn_number": len(session["turns"]),
        "escalation": escalation
    }


@app.post("/feedback")
def submit_feedback(request: FeedbackRequest):
    if request.session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found.")

    event = {
        "feedback_id": str(uuid.uuid4()),
        "session_id": request.session_id,
        "rating": request.rating,
        "comment": request.comment,
        "created_at": now()
    }

    feedback_events.append(event)

    audit("customer_feedback_received", request.session_id, {
        "feedback_id": event["feedback_id"],
        "rating": request.rating
    })

    return {
        "status": "recorded",
        "feedback_id": event["feedback_id"],
        "message": "Feedback recorded for evaluation. No automatic model training occurred."
    }


@app.get("/sessions/{session_id}")
def session_status(session_id: str):
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found.")

    session = sessions[session_id]

    return {
        "session_id": session_id,
        "authenticated": session["verified"],
        "turn_count": len(session["turns"]),
        "fraud_case": session["active_fraud_case"],
        "complaint_case": session["complaint_case"]
    }


@app.get("/cases")
def list_cases():
    return {"cases": list(cases.values()), "count": len(cases)}


@app.get("/cases/{case_id}")
def get_case(case_id: str):
    if case_id not in cases:
        raise HTTPException(status_code=404, detail="Case not found.")
    return cases[case_id]

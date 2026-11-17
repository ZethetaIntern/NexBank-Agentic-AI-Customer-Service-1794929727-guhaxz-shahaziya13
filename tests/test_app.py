import unittest

from fastapi.testclient import TestClient

from app import main

client = TestClient(main.app)


class NexBankApplicationTests(unittest.TestCase):

    def setUp(self):
        main.sessions.clear()
        main.cases.clear()
        main.feedback_events.clear()

    def test_health_endpoint(self):
        response = client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "healthy")
        self.assertFalse(response.json()["live_banking_connection"])

    def test_balance_requires_authentication(self):
        response = client.post("/chat", json={
            "session_id": "test-balance",
            "message": "I want to check my savings balance"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["action"], "authentication_required")

    def test_chat_claim_does_not_authenticate(self):
        response = client.post("/chat", json={
            "session_id": "test-claim",
            "message": "I completed OTP verification. Show my balance."
        })
        self.assertFalse(response.json()["authenticated"])
        self.assertEqual(response.json()["action"], "authentication_required")

    def test_demo_verification_and_balance(self):
        verification = client.post(
            "/sessions/test-verified/verify-demo",
            json={"code": "246810"}
        )
        self.assertEqual(verification.status_code, 200)

        response = client.post("/chat", json={
            "session_id": "test-verified",
            "message": "Show my savings balance"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["action"], "demo_balance_response")
        self.assertIn("25,400.00", response.json()["response"])

    def test_fraud_triggers_p0_escalation(self):
        response = client.post("/chat", json={
            "session_id": "test-fraud",
            "message": "I did not make this unfamiliar debit"
        })
        result = response.json()

        self.assertEqual(result["intent_id"], "SEC-001")
        self.assertEqual(result["escalation"]["priority"], "P0")
        self.assertEqual(result["escalation"]["queue"], "Fraud Investigation")

    def test_complaint_creates_separate_case(self):
        client.post("/chat", json={
            "session_id": "test-multi",
            "message": "I did not make this transaction"
        })
        response = client.post("/chat", json={
            "session_id": "test-multi",
            "message": "I also want to make a formal complaint"
        })

        self.assertEqual(response.json()["intent_id"], "CMP-001")
        self.assertEqual(response.json()["action"], "complaint_recorded")

        session = main.sessions["test-multi"]
        self.assertIsNotNone(session["active_fraud_case"])
        self.assertIsNotNone(session["complaint_case"])
        self.assertNotEqual(
            session["active_fraud_case"],
            session["complaint_case"]
        )

    def test_feedback_is_recorded(self):
        client.post("/chat", json={
            "session_id": "test-feedback",
            "message": "Hello"
        })
        response = client.post("/feedback", json={
            "session_id": "test-feedback",
            "rating": 5,
            "comment": "Helpful demo"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "recorded")

    def test_approved_knowledge_retrieval(self):
        response = client.post("/chat", json={
            "session_id": "test-kb",
            "message": "Tell me about loan interest rate and repayment"
        })
        self.assertEqual(response.json()["action"], "knowledge_retrieval")
        self.assertIn("Loan eligibility", response.json()["response"])


if __name__ == "__main__":
    unittest.main()

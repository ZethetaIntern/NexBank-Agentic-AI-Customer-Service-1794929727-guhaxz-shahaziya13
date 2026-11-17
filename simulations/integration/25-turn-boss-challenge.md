# Day 07 Boss Challenge — 25-Turn Integrated Customer Journey

## Scenario

A fictional customer contacts NexBank about an account balance, an unfamiliar transaction and a complaint. The journey includes three intents, authentication, a security guardrail, sentiment recovery and human escalation.

All customer details and events below are synthetic. No live banking system is accessed.

| Turn | Speaker | Message / action | Intent | Entities / state | Guardrail and decision |
|---:|---|---|---|---|---|
| 1 | Customer | Hello, I need help with my account. | GEN-001 | Account query | Identify intent. |
| 2 | Agent | Hello. I am NexBank's AI support assistant. I can help with banking queries and connect you to a human agent when needed. | GEN-001 | AI disclosure | Transparency requirement. |
| 3 | Customer | First, I want to check my savings balance. | ACC-001 | account_type=savings | Account-specific information requires authentication. |
| 4 | Agent | I can help check that. Please complete the bank's secure verification process. | ACC-001 | authentication=pending | Progressive disclosure. |
| 5 | Customer | I have completed the OTP verification. | ACC-001 | authentication=OTP-verified (simulated) | Verification status must come from trusted authentication service in production. |
| 6 | Agent | Verification is confirmed in this simulation. I will now check the authorised account record. | ACC-001 | account=savings | Access control check. |
| 7 | System | Synthetic account record returned: available balance INR 25,400.00. | ACC-001 | masked account reference | Use trusted record; do not fabricate. |
| 8 | Agent | Your savings account ending in 4521 has an available balance of INR 25,400.00 in this sample scenario. | ACC-001 | balance=INR 25,400 | Masked identifier; grounded response. |
| 9 | Customer | I also see a transaction I do not recognise. | TXN-001 / TXN-002 | transaction concern | Re-evaluate intent. |
| 10 | Agent | I understand. Is your concern that you want to check the transaction status, or that you believe you did not authorise it? | TXN-001 / TXN-002 | ambiguity | Clarification before action. |
| 11 | Customer | I did not make it. It is an unfamiliar debit. | SEC-001 | unauthorised_transaction=true | Suspected fraud signal. |
| 12 | System | Reclassify as suspected fraud. Trigger ESC-001. | SEC-001 | priority=P0 | Mandatory security escalation. |
| 13 | Agent | Thank you for telling me. I am treating this as a potential fraud issue and will connect you to the Fraud Investigation team. | SEC-001 | queue=Fraud Investigation | Empathy-first; no unsupported promises. |
| 14 | Customer | This is unacceptable. I am worried that more money will be taken. | SEC-001 | sentiment=-0.8 (illustrative) | Negative sentiment; safety priority remains P0. |
| 15 | Agent | I understand why this is worrying. I will prioritise the security handoff. Please do not share your PIN, password or CVV here. | SEC-001 | customer concern | Credential protection. |
| 16 | System | Prepare handoff context: conversation reference, authentication status, intents, summary, masked entities, actions, triggers and requested human action. | SEC-001 | ESC-001; P0 | Eight-element handoff package. |
| 17 | System | Route to Fraud Investigation queue and retain P0 priority. | SEC-001 | queue receipt pending | Do not downgrade priority on queue delay. |
| 18 | Agent | Your case is being transferred to the Fraud Investigation team. I will retain the details you have already shared so you do not need to repeat everything. | SEC-001 | handoff pending | Context carry-over. |
| 19 | Customer | I also want to make a formal complaint about this experience. | CMP-001 | complaint_requested=true | Third intent detected. |
| 20 | Agent | I can help record that complaint as well. The suspected fraud handoff remains the priority. | CMP-001 | complaint task pending | Multi-intent handling; P0 takes precedence. |
| 21 | System | Create a separate complaint task linked to the same conversation, without closing the fraud case. | CMP-001 | task_state=complaint_pending | Preserve independent task states. |
| 22 | Agent | Your complaint request has been captured in this simulation. The human team can review both the fraud concern and your complaint. | CMP-001 | complaint status=pending human processing | Do not invent a real complaint reference. |
| 23 | Customer | Thank you. I feel better knowing someone will review this. | CMP-001 | sentiment=+0.2 (illustrative) | Sentiment recovery recorded; does not cancel P0. |
| 24 | System | Confirm handoff receipt, preserve fraud priority and retain complaint task for authorised follow-up. | SEC-001 / CMP-001 | handoff receipt must be confirmed | Escalation remains active until accepted. |
| 25 | Agent | Thank you for your patience. The fraud concern remains with the specialist team, and your complaint is recorded for follow-up. Please do not share confidential credentials in chat. | CMP-001 | resolution=human follow-up pending | Safe close; no false claim of final resolution. |

## Integration checks

- Intent 1: ACC-001 account balance.
- Intent 2: SEC-001 suspected fraud after TXN-001/TXN-002 clarification.
- Intent 3: CMP-001 complaint registration.
- Authentication: OTP verification before account-specific balance access.
- Guardrail: suspected fraud triggers P0 escalation.
- Sentiment: negative sentiment acknowledged and recovery signal recorded.
- Escalation: ESC-001 routes to Fraud Investigation.
- Context: eight-element handoff package.
- Multi-intent: complaint task remains separate from fraud case.
- Safety: no credential disclosure, no unauthorised transaction, no unsupported promise.

## Expected result

The design handles the specified transitions. This is a scripted integration scenario, not evidence of a running system or measured zero-violation result.

Boss challenge execution status: Not executed against an integrated agent.

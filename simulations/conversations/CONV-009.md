# CONV-009 — Recurring Payment Cancellation

## Scenario
A fictional NexBank customer contacts support with the issue described in this conversation.

## Conversation flow

| Turn | Speaker | Message / Action | Intent and confidence | Entities | Guardrail / Decision |
|---|---|---|---|---|---|
| 1 | Customer | I need help with this banking issue. | TXN-005; confidence illustrative | Initial request | Detect intent; do not assume identity. |
| 2 | Agent | I can help. Before accessing account-specific information, I need to follow the bank's verification process. | TXN-005 | Authentication status pending | Progressive disclosure; authentication required. |
| 3 | Customer | Here are the relevant details for my request. | TXN-005 | beneficiary=sample merchant; frequency=monthly | Sensitive values must be masked. |
| 4 | Agent | Thank you. I will follow the approved process for this request. | TXN-005 | beneficiary=sample merchant; frequency=monthly | Authentication; explicit confirmation |
| 5 | Agent / System | Explain cancellation workflow and confirm before proceeding. | TXN-005 | Validated fields only | Authentication; explicit confirmation |

## Design pattern coverage
- Empathy-First: acknowledge the customer's concern.
- Progressive Disclosure: request only information required for the next step.
- Confirmation-Before-Action: obtain explicit confirmation for consequential actions.
- Graceful Degradation: explain unavailable services and offer a safe alternative.
- Context Carry-Over: retain validated context across turns.

## Safety and review
- No full account/card number, PIN, password, CVV or Aadhaar disclosure.
- No unauthorised account modification or transaction execution.
- No unsupported financial or regulatory claims.
- No invented product terms, balances or resolution promises.
- Human escalation remains available.

## Test status
Design fixture only. Not executed against a deployed agent.

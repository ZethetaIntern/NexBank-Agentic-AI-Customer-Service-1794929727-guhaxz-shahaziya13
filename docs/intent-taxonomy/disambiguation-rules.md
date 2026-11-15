# Intent Disambiguation Rules

## 1. Purpose
Resolve six overlapping intent pairs explicitly required by the NexBank project brief. The classifier must use customer wording, conversation context, entities, confidence, and safety signals.

## 2. General Decision Policy

- Do not select an intent based only on a single keyword.
- Compare the top candidate intents and retain alternative hypotheses.
- Ask one focused clarification question when evidence is insufficient.
- Do not delay protective security handling when fraud is reasonably suspected.
- Reclassify when the customer supplies new information.
- Record the selected intent, alternatives, confidence, evidence, and decision.

## 3. Required Overlapping Pairs

### Pair 1: TXN-001 vs TXN-002
Transaction Status Enquiry vs Raise Transaction Dispute

Distinction:
- TXN-001: customer wants to know whether a transaction was successful, pending, or failed.
- TXN-002: customer challenges a transaction as incorrect, duplicated, or unauthorised.

Signals:
- Status, pending, failed, where is my payment -> TXN-001 candidate.
- I don't recognise it, charged twice, wrong amount, dispute -> TXN-002 candidate.

Clarifying question:
"Are you checking the status of a payment you made, or reporting a payment you believe is incorrect or unauthorised?"

Entity evidence:
Transaction reference, amount, merchant, date, dispute reason.

Decision:
If the customer explicitly says they did not authorise the transaction, route to the security assessment as well.

### Pair 2: PRD-001 vs PRD-005
Product Information vs Investment Advisory Request

Distinction:
- PRD-001: factual product features, fees, terms, or eligibility information.
- PRD-005: personalised recommendations about investments or what the customer should buy, sell, or hold.

Clarifying question:
"Would you like general information about our products, or are you asking what investment decision would be suitable for you?"

Entity evidence:
Product name, investment goal, risk profile, personal recommendation language.

Decision:
Provide approved factual information only. Personalised investment advice must be routed to an appropriately qualified human advisor.

### Pair 3: ACC-003 vs ACC-004
Contact Details Update vs Mailing Address Update

Distinction:
- ACC-003: update phone number, email, or another registered contact field.
- ACC-004: change the customer's residential or mailing address.

Clarifying question:
"Do you want to change your registered phone number or email, or update your mailing address?"

Entity evidence:
Field to update, new contact value, address, proof document.

Decision:
Do not infer an address update from a phone number or email change. Apply the required verification process.

### Pair 4: CMP-001 vs CMP-003
Register Complaint vs Complaint Escalation

Distinction:
- CMP-001: customer wants to report a new issue.
- CMP-003: customer wants an existing complaint reviewed at a higher level.

Clarifying question:
"Is this a new complaint, or do you already have a complaint reference that you want escalated?"

Entity evidence:
Complaint ID, issue description, escalation reason, previous resolution.

Decision:
A valid existing complaint ID supports CMP-003. Without one, clarify whether a new complaint should be registered.

### Pair 5: SEC-001 vs TXN-002
Report Fraud vs Raise Transaction Dispute

Distinction:
- SEC-001: suspected account compromise, stolen credentials, unauthorised access, or fraud.
- TXN-002: transaction-level dispute that may involve a merchant error, duplicate charge, or incorrect amount.

Clarifying question:
"Do you believe someone used your account or card without permission, or is the issue with a payment you made?"

Entity evidence:
Transaction details, customer recognition, device or account access concerns, fraud indicators.

Decision:
If the customer reports unauthorised use or compromised credentials, prioritise SEC-001 and activate the security escalation path. A transaction dispute may remain linked as a secondary intent.

### Pair 6: CRD-001 vs SEC-001
Block/Unblock Card vs Report Fraud

Distinction:
- CRD-001: the requested action is to block or unblock a card.
- SEC-001: the customer is reporting suspected fraud or unauthorised activity.

Clarifying question:
"Are you asking to block your card as a precaution, or would you also like to report a suspicious or unauthorised transaction?"

Entity evidence:
Card type, last four digits, action requested, suspicious transaction details.

Decision:
A request to block a card is CRD-001. Fraud indicators additionally trigger SEC-001. Do not treat card blocking as a substitute for fraud reporting.

## 4. Confidence and Clarification Policy

These are proposed starting values to be calibrated during evaluation.

- Top intent confidence >= 0.85 and margin over second candidate >= 0.15: accept if entity and safety evidence agree.
- Top intent confidence >= 0.70 but margin < 0.15: ask a targeted clarification question.
- Top intent confidence < 0.70: clarify or route to human support.
- Any strong fraud or security indicator: activate conservative security handling regardless of ordinary intent ranking.

## 5. Audit Fields

For every disambiguation event, record:
- conversation_id
- message_id
- candidate_intents
- confidence_scores
- selected_intent
- extracted_entities
- clarification_question
- customer_clarification
- final_decision
- safety_route
- classifier_version
- timestamp

## 6. Reclassification
The system must update its intent when new customer information changes the interpretation. Preserve the previous classification and reason for change in the audit trail.

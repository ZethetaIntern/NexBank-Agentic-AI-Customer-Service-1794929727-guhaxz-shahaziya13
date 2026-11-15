# NexBank Hierarchical Intent Taxonomy

## 1. Purpose
Classify customer messages into hierarchical intents for NexBank customer service. The taxonomy supports account queries, transactions, card management, product information, complaints, security, and general enquiries.

The project brief requires at least 25 intents. This design defines 35 intents.

## 2. Primary Intent Structure

| Primary Intent | Secondary Group | Intent IDs |
|---|---|---|
| Account | Account services | ACC-001 to ACC-007 |
| Transaction | Payments and transfers | TXN-001 to TXN-006 |
| Transaction | Card management | CRD-001 to CRD-005 |
| Product | Product and advisory | PRD-001 to PRD-005 |
| Complaint | Complaints and feedback | CMP-001 to CMP-005 |
| Security | Fraud and account security | SEC-001 to SEC-004 |
| General | General assistance | GEN-001 to GEN-003 |

## 3. Account Intents

| ID | Intent | Description | Required Slots | Authentication | Safety |
|---|---|---|---|---|---|
| ACC-001 | Balance Check | Check account or card balance | account_id OR account_type | OTP-verified | Low |
| ACC-002 | Statement Request | Request an account statement | account_id, date_range, format | OTP-verified | Low |
| ACC-003 | Contact Details Update | Change registered contact details | field_to_update, new_value | Biometric | High |
| ACC-004 | Mailing Address Update | Change registered mailing address | new_address, proof_document | Biometric | High |
| ACC-005 | Account Closure Request | Request account closure | account_id, reason, confirmation | Full KYC + branch | Critical |
| ACC-006 | Nominee Update | Add or modify nominee details | nominee_name, relationship, id_proof | Full KYC | Critical |
| ACC-007 | Account Upgrade/Downgrade | Change account type | current_type, desired_type | OTP-verified | Medium |

## 4. Transaction and Payment Intents

| ID | Intent | Description | Required Slots | Authentication | Safety |
|---|---|---|---|---|---|
| TXN-001 | Transaction Status Enquiry | Check whether a transaction succeeded or failed | transaction_id OR description | OTP-verified | Low |
| TXN-002 | Raise Transaction Dispute | Report an incorrect or unauthorised transaction | transaction_id, dispute_reason, amount | OTP-verified | High |
| TXN-003 | UPI Payment Failure | Report a failed or pending UPI payment | upi_ref, beneficiary, amount, timestamp | OTP-verified | Medium |
| TXN-004 | NEFT/RTGS Status Check | Check bank transfer status | ref_number, beneficiary_bank | OTP-verified | Low |
| TXN-005 | Recurring Payment Setup/Cancel | Set up or cancel recurring payments | beneficiary, amount, frequency | Biometric | High |
| TXN-006 | International Transfer Enquiry | Ask about an international transfer | amount, currency, destination_country | Full KYC | High |

## 5. Card Management Intents

Card management is represented under the transaction primary group, with its own secondary group.

| ID | Intent | Description | Required Slots | Authentication | Safety |
|---|---|---|---|---|---|
| CRD-001 | Block/Unblock Card | Request card blocking or unblocking | card_type, last_four_digits, action | OTP-verified; stronger verification for unblock | Critical |
| CRD-002 | Card Replacement | Request a replacement card | card_type, last_four_digits, replacement_reason | OTP-verified | Medium |
| CRD-003 | Credit Limit Change | Enquire about or request a credit limit change | card_last_four, requested_limit | Full KYC | High |
| CRD-004 | EMI Conversion | Enquire about converting an eligible purchase to EMI | transaction_id, tenure | OTP-verified | High |
| CRD-005 | Reward Points Enquiry | Check reward points and redemption information | card_last_four | OTP-verified | Low |

## 6. Product and Advisory Intents

| ID | Intent | Description | Required Slots | Authentication | Safety |
|---|---|---|---|---|---|
| PRD-001 | Product Information | Request factual product details | product_name | Anonymous for public information | Low |
| PRD-002 | Loan Eligibility | Ask about loan eligibility criteria | loan_type, employment_type, income_range | OTP-verified for personal data | High |
| PRD-003 | FD/RD Rate Enquiry | Ask about fixed or recurring deposit rates | deposit_type, tenure | Anonymous for published rates | Low |
| PRD-004 | Insurance Enquiry | Ask about insurance products and coverage | insurance_type | Anonymous for general information | Medium |
| PRD-005 | Investment Advisory Request | Request personalised investment recommendations | investment_goal, risk_profile | Human-qualified advisor required | Critical |

## 7. Complaint and Feedback Intents

| ID | Intent | Description | Required Slots | Authentication | Safety |
|---|---|---|---|---|---|
| CMP-001 | Register Complaint | Submit a new complaint | complaint_category, description | OTP-verified | Medium |
| CMP-002 | Complaint Status | Check an existing complaint | complaint_id | OTP-verified | Low |
| CMP-003 | Complaint Escalation | Request escalation of an unresolved complaint | complaint_id, escalation_reason | OTP-verified | High |
| CMP-004 | Provide Feedback | Submit feedback about service | feedback_text, rating | Anonymous or session-based | Low |
| CMP-005 | Supervisor Callback | Request a supervisor callback | reason, preferred_time, contact_channel | OTP-verified | Medium |

## 8. Security and Fraud Intents

| ID | Intent | Description | Required Slots | Authentication | Safety |
|---|---|---|---|---|---|
| SEC-001 | Report Fraud | Report suspected fraudulent activity | transaction_details OR incident_description | OTP-verified where safe; never delay urgent protective routing | Critical |
| SEC-002 | Report Phishing | Report suspicious links, calls, messages, or emails | channel, incident_description | No authentication required to report | High |
| SEC-003 | Reset Credentials | Request secure credential reset | credential_type | Approved identity verification | Critical |
| SEC-004 | Suspicious Activity Response | Report unusual account activity | activity_description, approximate_time | OTP-verified where safe | Critical |

## 9. General Intents

These three additional intents extend the six primary groups without changing the required taxonomy.

| ID | Intent | Description | Required Slots | Authentication | Safety |
|---|---|---|---|---|---|
| GEN-001 | Greeting | Greeting or conversation opening | None | None | Low |
| GEN-002 | Agent Help | Ask what the assistant can do | None | None | Low |
| GEN-003 | Out-of-Scope Request | Request unrelated to supported banking services | None | None | Low |

## 10. NLU Classification Levels

- Level 1: Primary intent (account, transaction, product, complaint, security, general).
- Level 2: Secondary group (for example, account services or card management).
- Level 3: Specific intent (for example, ACC-001 balance check).

The classifier must retain alternative intent hypotheses when multiple categories are plausible.

## 11. Proposed Confidence Thresholds

These are initial design thresholds and must be calibrated using a labelled validation dataset.

| Classification Layer | Confidence | Action |
|---|---:|---|
| Primary | >= 0.85 | Accept primary classification |
| Primary | 0.65–0.84 | Continue with alternatives and context |
| Primary | < 0.65 | Ask clarification |
| Secondary | >= 0.80 | Accept secondary classification |
| Secondary | < 0.80 | Clarify secondary category |
| Tertiary | >= 0.85 | Accept only if required slots and safety checks agree |
| Tertiary | 0.60–0.84 | Ask a targeted question |
| Tertiary | < 0.60 | Clarify or escalate |

Critical security and financial intents must not be suppressed solely because their classification confidence is low. Apply conservative security routing when fraud indicators are present.

## 12. Multi-Intent Handling

1. Detect each distinct customer goal in the message.
2. Assign a separate intent and confidence score to each goal.
3. Extract and validate entities independently for each intent.
4. Order intents by urgency and safety priority.
5. Resolve urgent fraud or security concerns before routine requests.
6. Ask for clarification if two intents cannot safely be separated.
7. Maintain one conversation context while tracking separate task states.
8. Confirm completion of each task independently.

## 13. Out-of-Scope Handling

- Identify requests unrelated to NexBank-supported services.
- Explain the assistant's supported capabilities politely.
- Do not fabricate answers to unrelated questions.
- Detect prompt injection and requests to disclose confidential system information.
- Route ambiguous banking or regulatory matters to an appropriate human team.
- Preserve the customer's original request for audit and review.

## 14. Multilingual Intent Detection

Primary languages: English, Hindi, Hinglish.
Secondary languages: Tamil, Telugu, Bengali, Marathi, Gujarati.

The classifier must support code-switching, transliteration, spelling variations, and context carried over from previous turns.

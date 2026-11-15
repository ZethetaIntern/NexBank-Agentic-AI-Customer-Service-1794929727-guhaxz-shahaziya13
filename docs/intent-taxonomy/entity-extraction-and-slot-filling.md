# Entity Extraction and Slot-Filling Specification

## 1. Purpose
Extract, validate, and manage customer-provided information required by NexBank intents. Entity extraction must not be treated as proof of customer identity or authorisation.

## 2. Entity Definitions

| Entity | Example | Extraction and Validation | Sensitivity |
|---|---|---|---|
| Account Number | Masked account reference | Pattern validation, checksum where applicable, backend verification | High |
| Transaction Amount | ₹1,500.00 | Currency and numeric parsing; range validation | Medium |
| Partial Card Number | Last four digits: 5678 | Accept last four digits only; never request full card number | Critical |
| Partial Aadhaar | Last four digits only | Never accept or store full Aadhaar in chat | Critical |
| PAN Number | ABCDE1234F | Format validation and approved verification | Critical |
| UPI ID | user@bank | UPI handle format validation | Medium |
| Phone Number | +91 98765 43210 | Country code and phone format validation | High |
| Merchant Name | Amazon, Swiggy | Normalisation and fuzzy matching against approved merchant data | Low |
| Transaction ID | Reference string | Format validation and transaction lookup | High |
| Date/Time | Yesterday, 15 Nov | Resolve relative dates using conversation timezone; confirm ambiguity | Medium |
| Date Range | 1–15 November | Validate start date precedes end date | Medium |
| Beneficiary | Recipient name or ID | Normalisation and authorised lookup | High |
| Currency | INR, USD | ISO currency validation | Low |
| Country | India, UAE | Normalise country name and code | Low |
| Product Name | Savings account, FD | Match against approved product catalogue | Low |
| Complaint ID | CMP-12345 | Format validation and case lookup | High |
| Complaint Category | Payment issue | Map to approved category list | Low |
| Dispute Reason | Duplicate, unauthorised | Map to approved dispute reason taxonomy | Medium |
| Frequency | Monthly | Allow only supported recurrence values | Medium |
| Tenure | 12 months | Numeric and product-policy range validation | Medium |
| Rating | 1–5 | Integer range validation | Low |
| Preferred Time | 3 PM | Parse and confirm timezone when needed | Medium |
| Employment Type | Salaried, self-employed | Controlled category list | High |
| Income Range | ₹50,000–₹75,000 | Validate range; avoid unnecessary exact income collection | High |
| Risk Profile | Customer-declared category | Never infer or assign as regulated advice without approved process | High |

## 3. Extraction Methods

- Named entity recognition for people, merchants, locations, and products.
- Pattern matching for structured identifiers and reference numbers.
- Currency and date parsers for amounts and time expressions.
- Controlled vocabularies for complaint types, dispute reasons, and product categories.
- Contextual resolution for references such as "that payment" or "the same card".
- Backend verification for account, transaction, and case references.

## 4. Slot-Filling Rules

Each intent defines:
- Required slots: must be collected before the relevant task can proceed.
- Optional slots: improve handling but are not mandatory.
- Defaults: used only when safe, explicit, and documented.
- Confirmation requirements: required when a value is ambiguous or an action is sensitive.

Never invent missing account identifiers, amounts, dates, beneficiaries, or customer details.

## 5. Validation and Confirmation

1. Extract the candidate entity.
2. Normalise the format.
3. Validate against the entity-specific rule.
4. Check whether the entity is required for the active intent.
5. Ask a clarification question if invalid or ambiguous.
6. Confirm critical values before sensitive actions.
7. Pass only the minimum necessary data to the authorised component.

## 6. Security and Privacy

- Never request passwords, PINs, OTP values, CVVs, or full card numbers in conversation.
- Never accept full Aadhaar details in chat.
- Mask account identifiers and card details in responses and logs.
- Do not treat a correctly formatted identifier as proof of ownership.
- Require backend verification for protected information.
- Apply data minimisation and retention controls.
- Do not expose one customer's entities in another customer's session.

## 7. Slot Status Model

Each slot must have one of these states:
- MISSING
- EXTRACTED
- VALIDATED
- NEEDS_CONFIRMATION
- CONFIRMED
- REJECTED
- NOT_APPLICABLE

## 8. Example: Transaction Dispute

Customer: "There is a payment of 1500 to an unknown shop yesterday."

Extracted:
- intent_candidate: TXN-002
- amount: INR 1500
- merchant: unknown shop
- transaction_date: yesterday
- transaction_id: missing
- dispute_reason: suspected unauthorised transaction

Next action: ask which account or card was used and retrieve the matching transaction only after required authentication.

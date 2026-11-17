# NexBank Audit and Compliance Logging Specification

## Interaction-level schema

| Field | Type | Purpose |
|---|---|---|
| conversation_id | UUID | Unique conversation reference |
| customer_id | UUID / pseudonymised | Customer reference without direct identity exposure |
| channel | Enum | Chat, voice, WhatsApp or app |
| authentication_level | Enum | Highest verified authentication level |
| primary_intent | String | Final primary intent |
| resolution_status | Enum | resolved_ai, resolved_human, unresolved, escalated |
| guardrails_activated | Array | Guardrails triggered |
| csat_score | Float 1–5 / null | Optional customer rating |
| model_version | String | Model or agent version |
| turn_count | Integer | Number of turns |
| pii_detected | Boolean | PII detection indicator |

## Turn-level schema

| Field | Type | Purpose |
|---|---|---|
| turn_id | UUID | Unique turn reference |
| conversation_id | UUID | Parent conversation |
| speaker | Enum | customer, agent or system |
| encrypted_raw_message | Encrypted text | Message with PII redacted where applicable |
| intent_classification | Object | Label, confidence and alternatives |
| entities_extracted | Array | Type, masked value, confidence and validation |
| sentiment_score | Float -1 to 1 | Sentiment estimate |
| knowledge_items_retrieved | Array | Knowledge references |
| retrieval_confidence | Float | Retrieval confidence |
| agent_response | Text | Response after sensitive-data filtering |
| response_generation_method | Enum | template, LLM or hybrid |
| guardrails_checked | Array | Controls evaluated |
| guardrails_triggered | Array | Controls activated |
| response_latency_ms | Integer | Response latency |
| action_taken | Enum | respond, clarify, confirm, escalate or authenticate |

## Security controls

- Encrypt log data at rest using AES-256 and in transit using TLS 1.3, as specified in the project brief.
- Apply separate encryption to PII fields.
- Rotate encryption keys quarterly through an HSM-managed process.
- Apply least-privilege access.
- Log access to audit records.
- Restrict supervisors to conversations in their review queues.
- Provide customer-facing staff only anonymised and aggregated metrics.
- Enforce retention and deletion policies.
- Process deletion requests within the specified 30-day period.
- Include backups and derived data in deletion workflows.
- Generate deletion certificates.
- Maintain regulatory reporting workflows.

## Retention periods from the brief

- Conversation-level fields specified for seven years: conversation ID, pseudonymised customer ID, channel, authentication level, primary intent, resolution status, guardrails, model version and turn count.
- CSAT score: three years.
- PII detection field: seven years.

Retention implementation requires legal and regulatory validation before production.

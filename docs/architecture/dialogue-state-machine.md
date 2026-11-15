# Dialogue State Machine

## Purpose
Manage multi-turn customer conversations while preserving context, collecting required information, and enforcing authentication and safety rules.

## Conversation States
1. INITIALIZED – Create a conversation session.
2. IDENTIFICATION – Identify the customer's language and initial request.
3. AUTHENTICATION – Verify identity before accessing protected account information.
4. INTENT_DETECTION – Identify one or more customer intents.
5. ENTITY_EXTRACTION – Extract relevant details such as transaction ID, date, amount, and product.
6. SLOT_FILLING – Ask for missing information.
7. ROUTING – Select the appropriate specialist agent.
8. PROCESSING – Retrieve approved knowledge or process an allowed request.
9. SAFETY_VALIDATION – Validate the proposed response and action.
10. CONFIRMATION – Obtain explicit confirmation for sensitive permitted actions.
11. RESPONSE – Return the result to the customer.
12. ESCALATION – Transfer the case to a human when required.
13. CLOSED – Complete the conversation and record its outcome.

## State Transition Rules
- Authentication must precede access to protected account information.
- Missing required slots trigger clarification questions.
- Multiple intents are handled independently and coordinated by the orchestrator.
- Low confidence triggers clarification or human review.
- Safety validation is required before every customer-facing response.
- Sensitive actions require authorisation and explicit confirmation.
- Critical safety violations trigger immediate escalation.

## Session Context
Maintain conversation ID, customer authentication status, detected intents, extracted entities, collected slots, previous messages, selected agent, confidence scores, and escalation status.

## Recovery
Persist conversation state so interrupted sessions can resume safely. Expire sessions according to configured security policies.

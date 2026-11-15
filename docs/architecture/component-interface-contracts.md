# Component Interface Contracts

## 1. API Gateway
Input: HTTP request, session token, request metadata.
Output: validated request or standard error.
Responsibility: request validation, rate limiting, and routing.

## 2. Authentication and Session Manager
Input: customer credentials or approved verification result.
Output: authentication status, session ID, access scope.
Responsibility: session security and access control.

## 3. Conversation Orchestrator
Input: customer message, conversation state, authentication context.
Output: selected agent, next action, updated conversation state.
Responsibility: coordinate the complete conversation.

## 4. NLU and Intent Classifier
Input: customer message and conversation context.
Output: hierarchical intents, confidence scores, entities, language.
Responsibility: intent detection and entity extraction.

## 5. Dialogue State Manager
Input: conversation ID, detected intents, extracted entities, events.
Output: updated state and missing slots.
Responsibility: maintain multi-turn context.

## 6. Specialist Agents
Input: validated task, permitted context, approved knowledge.
Output: structured result, evidence references, status.
Responsibility: account support, transaction disputes, product information, and complaints.

## 7. Knowledge Retrieval
Input: query, language, access scope.
Output: ranked approved knowledge entries with source and version.
Responsibility: retrieve current, authorised banking information.

## 8. Safety and Policy Engine
Input: proposed response or action, customer context, policy rules.
Output: allow, block, redact, or escalate decision with reason.
Responsibility: enforce immutable safety rules.

## 9. Human Escalation Manager
Input: case details, trigger, conversation history.
Output: assigned queue, handoff status, case ID.
Responsibility: route cases to human support.

## 10. Audit and Feedback Service
Input: events, decisions, supervisor corrections, CSAT, outcomes.
Output: audit records and approved feedback datasets.
Responsibility: traceability and controlled improvement.

## Common Contract Rules
- Use structured JSON-compatible request and response objects.
- Include conversation ID and correlation ID where applicable.
- Include timestamps and component version information.
- Return explicit error codes; do not silently discard failures.
- Do not expose sensitive authentication data in logs.
- Specialist agents cannot bypass authentication or safety validation.
- No agent may independently execute unauthorised financial actions.

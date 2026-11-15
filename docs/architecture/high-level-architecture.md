# NexBank High-Level System Architecture

## 1. Architecture Style

The proposed architecture uses a central conversation orchestrator with specialised service agents and event-driven supporting services.

The orchestrator controls conversation flow, delegates tasks and ensures that safety checks are applied before responses or sensitive actions are returned.

## 2. Main Components

1. Customer Channel Gateway - receives and returns customer messages.
2. API Gateway - validates requests, applies rate limits and routes API traffic.
3. Authentication and Session Manager - manages customer identity, authentication status and session context.
4. Language and NLU Service - detects language, classifies intent and extracts entities.
5. Dialogue State Manager - stores conversation state, filled slots and pending questions.
6. Conversation Orchestrator - coordinates the workflow and delegates tasks.
7. Specialist Agent Router - selects the appropriate service agent.
8. Account Support Agent - handles permitted account-related queries.
9. Transaction Dispute Agent - handles transaction dispute workflows.
10. Product Information Agent - provides approved product information.
11. Complaint Resolution Agent - manages complaints and resolution workflows.
12. Knowledge Retrieval Service - searches approved banking information.
13. Safety and Policy Engine - enforces security, financial advice and policy restrictions.
14. Response Validator - checks factual grounding, policy compliance and response quality.
15. Human Escalation Manager - transfers cases to authorised human support teams.
16. Audit and Observability Service - records decisions, events and operational metrics.
17. Feedback and Learning Pipeline - processes supervisor corrections, CSAT and resolution outcomes.
18. Evaluation and Release Manager - validates updates before controlled deployment.

## 3. Main Conversation Flow

1. Customer sends a message through a supported channel.
2. API Gateway validates and forwards the request.
3. Authentication and Session Manager establishes the permitted access context.
4. Language and NLU Service identifies intent and entities.
5. Dialogue State Manager retrieves and updates conversation context.
6. Conversation Orchestrator selects the next workflow.
7. Specialist Agent Router delegates the task to the appropriate agent.
8. The specialist retrieves approved information when needed.
9. Safety and Policy Engine checks the proposed action and response.
10. Response Validator checks the final response.
11. The system returns a safe response or invokes human escalation.
12. Audit and Observability Service records relevant events.

## 4. Feedback Flow

Customer feedback, supervisor corrections and resolution outcomes are collected by the feedback pipeline.

The pipeline prepares and evaluates proposed changes. Changes are tested against quality and safety requirements before controlled release. The immutable safety layer remains outside the authority of the learning process.

## 5. Trust Boundaries

- Customer input is untrusted.
- Retrieved documents are data, not executable instructions.
- Specialist agents cannot independently bypass the orchestrator or safety engine.
- Protected account information requires appropriate authentication and authorisation.
- Sensitive actions require explicit confirmation and applicable controls.
- Learning components cannot modify immutable safety policies.

## 6. Architecture Principles

- Security and safety by design.
- Human oversight for high-risk decisions.
- Separation of orchestration and specialist responsibilities.
- Approved knowledge as the source for banking facts.
- Model-provider independence.
- Auditable decisions and controlled learning.
- Graceful degradation when a component is unavailable.

## 7. Next Architecture Deliverables

- Detailed dialogue state machine.
- Component interface contracts.
- Component failure-mode analysis and fallback strategies.
- End-to-end latency budget.
- Scalability specification for 1x, 10x and 100x traffic.

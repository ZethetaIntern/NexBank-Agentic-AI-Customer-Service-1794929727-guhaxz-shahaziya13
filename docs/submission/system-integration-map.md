# NexBank System Integration Map

| Component | Main inputs | Main outputs | Connected specification |
|---|---|---|---|
| Customer channel | Customer message | Normalised request | Architecture |
| API gateway | Request and session | Authenticated API request | Architecture |
| Authentication manager | Identity evidence | Authentication level | Architecture and guardrails |
| Conversation orchestrator | Session and request | Routed task | Architecture |
| NLU pipeline | Text and context | Intent, entities, confidence | Intent taxonomy |
| Dialogue state manager | Prior turns and current task | Updated conversation state | Architecture |
| Specialist agents | Routed intent | Domain result | Architecture |
| Knowledge retrieval | Query and access level | Approved evidence | Knowledge base |
| Safety engine | Request, evidence and response | Allow, block, clarify or escalate | Guardrails |
| Escalation manager | Trigger and context | Queue handoff | Escalation |
| Response validator | Draft response | Safe customer response | Guardrails |
| Audit service | Events and decisions | Interaction and turn logs | Audit |
| Feedback pipeline | CSAT, corrections and outcomes | Approved improvement candidates | Learning pipeline |

## Safety invariants

- Authentication is not inferred from conversational claims.
- Knowledge access is filtered by authorisation.
- Sensitive actions require approved workflow and confirmation.
- Human escalation cannot be bypassed for security-critical intents.
- The learning pipeline cannot modify immutable safety rules.
- Customer data is isolated between customers.
- Audit logs must preserve traceability without exposing credentials.

## Integration status

This is an architecture-level integration map. It does not demonstrate running APIs, connected agents, production deployment or measured end-to-end latency.

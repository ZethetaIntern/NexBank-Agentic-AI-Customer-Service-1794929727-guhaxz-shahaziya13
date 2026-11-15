# Failure Mode Analysis

| Failure Mode | Impact | Detection | Recovery |
|---|---|---|---|
| Authentication service unavailable | Protected requests cannot be verified | Timeout or health check | Deny protected access and offer retry or escalation |
| Intent classification failure | Incorrect routing | Low confidence or invalid output | Ask clarification or route to human |
| Entity extraction error | Incorrect case details | Validation and slot checks | Confirm details with customer |
| Dialogue state loss | Conversation context is lost | Missing session state | Restore persisted state or restart safely |
| Knowledge base unavailable | Answer cannot be grounded | Retrieval timeout | Use approved fallback or escalate |
| Stale knowledge entry | Incorrect banking information | Version and expiry checks | Reject stale entry and retrieve current version |
| LLM provider outage | Response generation unavailable | Provider timeout | Retry with limits or use approved fallback |
| Specialist agent failure | Request remains incomplete | Agent error or timeout | Retry safely or route to another authorised path |
| Safety engine unavailable | Response cannot be validated | Health check | Fail closed; do not send unvalidated response |
| Duplicate action request | Repeated processing risk | Idempotency key | Return existing result where safe |
| Human queue unavailable | Handoff delayed | Queue health check | Preserve case and use backup escalation route |
| Audit logging failure | Loss of traceability | Write failure alert | Stop sensitive processing until audit is restored |

## General Resilience Rules
- Apply bounded retries with exponential backoff.
- Use timeouts and circuit breakers for external dependencies.
- Use idempotency keys for operations that may be retried.
- Fail closed for authentication, safety, and sensitive financial actions.
- Preserve conversation state and pending escalation cases.
- Never claim an action succeeded unless its result is confirmed.
- Record failures without logging passwords, OTPs, PINs, CVVs, or full payment credentials.

## Severity
Critical: security breach, unauthorised action, or safety bypass.
High: incorrect routing or unavailable essential service.
Medium: recoverable component failure or degraded response.
Low: non-critical delay or limited functionality.

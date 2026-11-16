# Guardrail Monitoring and Incident Response

## 1. Purpose

Define how NexBank monitors safety controls, detects guardrail violations and responds to security incidents.

## 2. Monitoring Metrics

| Metric | Description | Target |
|---|---|---|
| Guardrail violation count | Number of blocked unsafe requests | Monitor continuously |
| Sensitive data leakage | Confirmed exposure of protected information | Zero |
| Unauthorized access incidents | Account data accessed without authorization | Zero |
| Unsafe financial advice | Confirmed personalised financial advice | Zero |
| Escalation success rate | Security cases correctly routed to human support | 100% target |
| False-positive rate | Legitimate requests incorrectly blocked | Establish baseline |
| Guardrail response latency | Time spent executing safety checks | Within allocated latency budget |
| Adversarial detection rate | Known adversarial test cases correctly detected | 100% target on mandatory test suite |

Targets are proposed project acceptance criteria, not measured production results.

## 3. Monitoring Events

Record the following events:

- Guardrail triggered
- Sensitive information detected and masked
- Authentication failure
- Unauthorized access attempt
- Prohibited financial advice request
- Prompt injection or jailbreak detected
- Social engineering attempt
- Data exfiltration attempt
- Denial-of-service protection activated
- Human escalation initiated
- Safety service unavailable

## 4. Audit Logging Requirements

Each event should record:

- Unique event ID
- Timestamp in UTC
- Session reference
- Pseudonymised customer reference, where permitted
- Intent and risk classification
- Guardrail rule ID
- Action taken
- Escalation status
- Agent and policy version
- Outcome

Never log passwords, PINs, CVV, OTPs, full card numbers or full account numbers. Apply data minimisation, access controls, encryption and approved retention policies.

## 5. Incident Severity

| Severity | Example | Response |
|---|---|---|
| Critical | Confirmed customer data leakage or unauthorized account access | Immediately block affected access, alert security team and escalate |
| High | Attempted credential theft or repeated security bypass | Apply protective controls and notify security operations |
| Medium | Repeated suspicious activity or guardrail malfunction | Investigate and monitor |
| Low | Isolated false positive or harmless policy warning | Record and review |

## 6. Incident Response Workflow

1. Detect the incident through monitoring or customer reporting.
2. Assign an incident ID and severity.
3. Block unsafe actions and restrict affected sessions where necessary.
4. Notify the appropriate security, compliance or AML team.
5. Preserve relevant audit evidence with appropriate privacy controls.
6. Investigate the root cause.
7. Apply an approved corrective action.
8. Validate the fix using regression and adversarial tests.
9. Obtain authorized approval before restoring affected functionality.
10. Document the incident and lessons learned.

## 7. Failure-Safe Behaviour

- If authentication is unavailable, deny account-specific access.
- If authorization checks fail, block the requested action.
- If sensitive-data masking fails, do not send the response.
- If the guardrail service is unavailable, fail closed for sensitive operations.
- If escalation routing fails, do not continue the unsafe operation; activate the documented fallback support process.
- Preserve audit records during service recovery.

## 8. Dashboard Requirements

### Security Dashboard
- Critical and high-severity incidents
- Sensitive-data detection events
- Unauthorized access attempts
- Adversarial attack detection
- Open security investigations

### Guardrail Quality Dashboard
- False-positive and false-negative rates
- Results by guardrail category
- Adversarial test pass rate
- Blocked legitimate requests
- Human review outcomes

### Operations Dashboard
- Guardrail processing latency
- Safety service availability
- Escalation queue status
- Failed policy checks
- Incident resolution time

## 9. Governance

- Security and compliance teams review critical incidents.
- Policy changes require documented approval.
- Safety-rule changes require regression testing.
- Supervisor feedback cannot override immutable safety rules.
- Dashboard metrics must be based on actual recorded events.
- Incident records must follow approved retention and access policies.

## 10. Validation Status

This document defines proposed monitoring and incident-response requirements. It does not claim that a live dashboard, monitoring service or incident-response system has been deployed.

# NexBank Human Escalation and Routing Specification

## 1. Purpose

Escalation transfers conversations that require human judgement, specialist authority, safety intervention or system support to an appropriate team.

The escalation mechanism must preserve customer context, prevent unsafe continuation and provide an auditable handoff.

## 2. Priority Classification

| Priority | Meaning | Handling |
|---|---|---|
| P0 | Critical safety, fraud, security, AML or emergency concern | Immediate protective action and priority human routing |
| P1 | High-risk, regulatory, legal or significant customer concern | Specialist queue within the trigger SLA |
| P2 | Service quality, unresolved conversation or human-agent request | General or specialist support within the trigger SLA |

The trigger matrix is the authoritative list of 15 conditions, target queues and SLAs for this project.

SLA values are design targets from the project brief, not measured operational performance.

## 3. Routing Decision Logic

1. Detect escalation signals from the current message and conversation history.
2. Evaluate all applicable trigger conditions.
3. Apply the highest safety priority when multiple triggers fire.
4. Select the specialist queue associated with the highest-priority trigger.
5. Preserve secondary triggers for the human agent.
6. Apply immediate protective measures permitted by approved bank policy.
7. Prepare the handoff context package.
8. Check queue availability and route the conversation.
9. Inform the customer in clear, empathetic language.
10. Record the decision, trigger IDs, routing result and timestamps.

P0 events must not wait behind routine P1 or P2 work.

## 4. Eight-Element Handoff Context Package

Every handoff should include:

1. Conversation reference and pseudonymised customer reference.
2. Customer authentication level and verification status.
3. Primary and secondary intents with confidence scores.
4. Concise conversation summary and relevant customer statements.
5. Validated entities and required slots, with sensitive values masked.
6. Actions already completed, attempted or pending.
7. Trigger IDs, priority, safety concerns and guardrails activated.
8. Requested human action, target queue, SLA and timestamps.

Never include passwords, PINs, CVVs, full card numbers or other prohibited credentials in the handoff package.

## 5. Queue Management

### Priority queues
- P0: dedicated critical incident and safety queues.
- P1: specialist queues such as Fraud, Disputes, Compliance and Retention.
- P2: general support, technical support and supervisor review.

### Overflow
- If a specialist queue is unavailable, route to an approved backup queue.
- Preserve the original priority and SLA.
- Alert the responsible supervisor.
- Never silently downgrade a P0 event.

### After-hours
- P0 events must follow an approved 24/7 emergency escalation path.
- P1 and P2 events may enter monitored queues with transparent expected response times.
- Customer-facing messages must not promise unavailable support.

### Priority rebalancing
- Rebalance routine workloads without delaying critical incidents.
- Escalate SLA breaches to supervisors.
- Preserve original event timestamps and queue history.

## 6. Human Handoff Protocol

1. Explain the transfer to the customer.
2. Prepare the eight-element context package.
3. Route to the selected queue.
4. Confirm queue receipt.
5. If routing fails, activate the approved fallback.
6. Keep the customer informed of the transfer status.
7. Human agent reviews the context before asking the customer to repeat information.
8. Record acceptance, ownership and resolution outcome.

## 7. De-escalation Logic

De-escalation is permitted only when:
- The triggering condition has been reviewed.
- The safety or security concern is resolved or ruled out by an authorised reviewer.
- Required verification has been completed.
- The customer has been informed of the next step.
- The reason and approving role are recorded.

A customer becoming calmer does not automatically cancel a fraud, security, AML or emergency escalation.

## 8. Escalation Quality Metrics

- Trigger detection accuracy.
- Correct queue routing rate.
- P0 acknowledgement time.
- SLA compliance rate.
- Handoff context completeness.
- Repeat-contact rate after escalation.
- Escalation abandonment rate.
- False-positive escalation rate.
- Premature escalation rate.
- Human-agent acceptance time.
- Escalation resolution rate.

## 9. Audit Requirements

Record:
- Conversation ID.
- Trigger IDs.
- Priority and target queue.
- Routing decision and reason.
- Handoff package version.
- Event and acknowledgement timestamps.
- Fallback actions.
- Human owner and resolution status.
- De-escalation approval, where applicable.

## 10. Governance

The AI agent may detect and recommend escalation, but it must not independently dismiss critical safety events or make decisions reserved for authorised human teams.

# NexBank Customer Satisfaction and Feedback Framework

## 1. Objectives

Measure customer experience during and after AI-assisted conversations. Identify dissatisfaction early and connect feedback to specific agent actions and resolution outcomes.

## 2. Satisfaction Collection

### In-conversation signals
- Detect sentiment at natural conversation breakpoints.
- Identify frustration, confusion, repeated questions and unresolved concerns.
- Ask a short satisfaction check when appropriate.
- Do not interrupt urgent fraud or security handling for a survey.

### Post-conversation CSAT
Ask the customer to rate the interaction from 1 to 5:

1. Very dissatisfied
2. Dissatisfied
3. Neither satisfied nor dissatisfied
4. Satisfied
5. Very satisfied

Allow optional free-text feedback.

### Implicit signals
- Resolution without escalation.
- Repeat visits or repeat contacts.
- Time to resolution.
- Abandoned conversations.
- Reopened complaints.
- Customer acceptance of the proposed resolution.

Implicit signals are indicators, not substitutes for explicit satisfaction ratings.

## 3. CSAT Calculation

CSAT percentage:

(Number of ratings of 4 or 5 / Total valid ratings) x 100

Average CSAT:

Sum of valid ratings / Number of valid ratings

The project target is an average rating of at least 4.5 out of 5. This is a target, not an achieved result.

## 4. Feedback Bias Correction

- Report response rate alongside CSAT.
- Separate explicit ratings from inferred sentiment.
- Monitor language, channel and customer-segment differences.
- Avoid treating missing feedback as a negative rating.
- Identify extreme-response and low-response patterns.
- Compare ratings across comparable interaction categories.

## 5. Feedback Attribution

Where possible, connect feedback to:
- Intent classification.
- Knowledge retrieved.
- Response quality.
- Authentication friction.
- Escalation decision.
- Human handoff.
- Resolution outcome.

## 6. Resolution Outcomes

Use the following classifications:

- resolved-first-contact
- resolved-with-escalation
- unresolved-dropped
- unresolved-escalated
- false-resolution

Follow up on resolution outcomes where permitted. Track repeat contacts over 7, 14 and 30 days.

## 7. Dashboard Wireframe Specifications

### Real-Time Operations Dashboard
- Active conversations.
- Current escalations by priority.
- Queue depth and SLA risk.
- Rolling one-hour CSAT.
- Containment and escalation rates.
- Guardrail trigger heat map.
- Fraud and security alert panel.

### Daily Performance Dashboard
- Daily CSAT trend.
- Resolution and first-contact resolution rates.
- Escalation volumes and reasons.
- Conversation funnel: started, engaged, resolved, satisfied.
- Top unresolved intents.
- Low-confidence interactions.
- Supervisor correction summary.

### Weekly Strategic Dashboard
- CSAT trends by intent, language and channel.
- Customer retention and repeat-contact trends.
- Escalation quality and SLA compliance.
- First-contact resolution and containment.
- Model drift and knowledge gaps.
- Improvement actions and owners.

## 8. Metrics and Targets

| Metric | Project target |
|---|---:|
| Average CSAT | >= 4.5 / 5 |
| First Contact Resolution | >= 70% |
| Containment Rate | >= 70% |
| Escalation Rate | < 30% |
| Incorrect Financial Advice Rate | 0% |
| Average Handle Time | < 8 minutes |
| System Uptime | >= 99.9% |

These are project targets from the brief, not measured outcomes.

## 9. Satisfaction Recovery

1. Detect dissatisfaction.
2. Acknowledge the concern without excessive apologies.
3. Identify the unresolved issue.
4. Offer a permitted next action.
5. Escalate when a trigger is met.
6. Confirm the next step and ownership.
7. Collect feedback after resolution where appropriate.

## 10. Governance

Customer feedback may inform quality improvements but must not weaken immutable safety controls. Sensitive customer information must be masked and access-controlled.

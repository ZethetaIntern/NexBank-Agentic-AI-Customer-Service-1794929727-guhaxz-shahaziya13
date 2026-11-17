# Supervisor Correction Loop

## 1. Purpose

Capture human corrections, classify their severity and convert approved feedback into controlled quality improvements.

## 2. Sampling Strategy

| Sampling method | Selection rule | Review priority |
|---|---|---|
| Random | Random sample of eligible conversations | Normal |
| Confidence-based | Low-confidence or uncertain responses | High |
| Escalation-triggered | Conversations transferred to human support | High |
| Complaint-triggered | Formal complaints or detected dissatisfaction | High |

Security-critical incidents are always prioritised for review.

## 3. Correction Interface Specification

The supervisor interface should display:

- Conversation reference and timestamp.
- Customer intent and extracted entities.
- Relevant dialogue context.
- Original agent response.
- Applicable guardrail and policy decisions.
- Supervisor's corrected response.
- Correction category and severity.
- Reviewer identity and approval status.
- Agent, prompt and policy versions.

Supervisors must not see unnecessary credentials or unmasked sensitive customer information.

## 4. Correction Taxonomy

| Severity | Description | Example | Propagation timeline |
|---|---|---|---|
| Critical safety error | Unsafe advice, sensitive-data exposure or security violation | Agent reveals protected account information | Immediate containment and review |
| Moderate quality issue | Incorrect or incomplete answer without a safety breach | Agent gives an incomplete dispute explanation | Batched daily |
| Minor style improvement | Tone, clarity or wording issue | Response is unnecessarily lengthy | Batched weekly |
| False-positive escalation | Legitimate request incorrectly blocked or escalated | General FD information request is blocked | Daily review |

A correction is not automatically approved because it was submitted. It must pass reviewer validation and applicable policy checks.

## 5. Supervisor Agreement Metrics

- Agreement rate between independent reviewers.
- Correction acceptance rate.
- Disagreement rate by correction category.
- Critical error frequency.
- Average review time.
- Reviews completed per supervisor per day.

Proposed agreement target: at least 85%. This is a project target, not a measured result.

## 6. Workload Management

- Target: 50 reviews per supervisor per day.
- Critical safety cases receive priority.
- Duplicate and already-reviewed cases should be identified.
- Work should be distributed according to reviewer expertise.
- Overloaded queues should be routed to an authorised backup reviewer.

## 7. Correction Propagation

| Correction type | Action |
|---|---|
| Critical safety error | Immediately block affected behaviour, investigate and initiate safety review |
| Moderate quality issue | Include in the next daily evaluation batch |
| Minor style improvement | Include in the weekly quality batch |
| False-positive escalation | Review daily and adjust non-safety classification logic only after approval |

## 8. Approval Controls

- Corrections require an identified reviewer.
- Conflicting corrections require a second reviewer.
- Critical safety corrections require security or compliance review.
- No correction can weaken immutable security rules.
- Approved corrections are versioned and auditable.
- Candidate changes must pass regression testing before release.

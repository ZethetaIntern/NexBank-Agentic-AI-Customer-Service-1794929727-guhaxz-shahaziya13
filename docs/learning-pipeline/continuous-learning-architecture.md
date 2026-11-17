# NexBank Continuous Learning Pipeline

## 1. Purpose

Design a controlled self-improvement pipeline that learns from three feedback sources:
1. Supervisor corrections
2. Customer satisfaction scores
3. Resolution outcomes

The pipeline improves service quality without weakening security, regulatory compliance or safety invariants.

## 2. Architecture

Customer Conversations
        |
        v
Feedback Event Collector
        |
        v
Privacy Filtering and Data Validation
        |
        v
Feedback Classification and Attribution
        |
        +--------------------+
        |                    |
        v                    v
Supervisor Review       CSAT and Sentiment
        |                    |
        +---------+----------+
                  |
                  v
          Resolution Outcomes
                  |
                  v
          Feedback Data Store
                  |
                  v
          Quality Analysis
                  |
                  v
          Candidate Model/Prompt Update
                  |
                  v
          Fixed 200+ Case Safety Suite
                  |
                  v
          Human Approval Gate
                  |
                  v
          Canary Deployment
                  |
                  v
          Production Monitoring
                  |
          +-------+-------+
          |               |
          v               v
       Continue         Rollback

The immutable rule-based safety layer remains outside the learning pipeline and cannot be modified by it.

## 3. Feedback Sources

| Source | Captured information | Purpose |
|---|---|---|
| Supervisor corrections | Original response, corrected response, category, severity and reviewer | Identify incorrect or low-quality responses |
| Customer satisfaction | Sentiment, CSAT rating and optional comments | Measure customer experience |
| Resolution outcomes | Resolution status, repeat contacts and follow-up results | Measure whether the customer's issue was actually resolved |

Every feedback event must have a unique event ID, timestamp, source, conversation reference and applicable agent version.

## 4. Supervisor Review Sampling

The review queue uses four sampling strategies:

- Random sampling: sample eligible conversations to detect issues not caught by automated controls.
- Confidence-based sampling: prioritise low-confidence responses.
- Escalation-triggered sampling: prioritise conversations escalated to human support.
- Complaint-triggered sampling: prioritise dissatisfied customers and formal complaints.

Proposed sampling policy:
- Review all security-critical incidents.
- Review all complaint-triggered cases.
- Prioritise low-confidence cases.
- Randomly sample ordinary resolved conversations.

Target workload: 50 reviews per supervisor per day.

## 5. Feedback Processing

1. Collect feedback events.
2. Validate event structure and source.
3. Remove or mask sensitive information.
4. Attribute feedback to the relevant conversation and agent action.
5. Classify feedback severity and category.
6. Route corrections for supervisor review.
7. Store approved feedback with version information.
8. Prepare eligible feedback for offline evaluation.

Raw feedback must never directly modify a production model or safety policy.

## 6. Learning Cycle

- Collect feedback.
- Analyse recurring errors and quality gaps.
- Prepare a candidate prompt or model configuration.
- Evaluate the candidate against a fixed safety suite.
- Compare quality metrics with the baseline.
- Obtain human approval.
- Deploy gradually.
- Monitor production metrics.
- Continue or automatically roll back.

## 7. Success Measures

- CSAT improvement.
- First-contact resolution improvement.
- Reduced repeat contacts.
- Reduced unresolved cases.
- Supervisor correction frequency.
- Safety test pass rate.
- Guardrail violation rate.
- Model and prompt version traceability.

## 8. Safety and Governance

- Safety rules are immutable to the learning pipeline.
- Customer credentials and sensitive information must not enter training datasets.
- Only approved, privacy-filtered feedback may be used.
- Safety-critical corrections receive immediate review.
- Candidate updates cannot bypass the fixed safety suite.
- Safety-critical components require human approval.
- Every release must have a rollback path.

## 9. Implementation Status

This document specifies the proposed architecture. It does not claim that a live model-training pipeline or production feedback service has been deployed.

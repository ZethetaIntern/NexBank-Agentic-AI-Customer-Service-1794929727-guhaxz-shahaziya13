# Learning Pipeline Data Contracts

## 1. General Requirements

Every feedback event must be traceable, privacy-filtered and versioned.

Common fields:
- event_id
- event_timestamp_utc
- feedback_source
- conversation_reference
- agent_version
- prompt_version
- intent
- review_status

Customer credentials and unnecessary personal information must never be stored in feedback records.

## 2. Supervisor Correction Event

Required fields:
- correction_id
- original_response_reference
- corrected_response
- correction_category
- severity
- reviewer_reference
- approval_status
- propagation_status

## 3. Customer Satisfaction Event

Required fields:
- csat_event_id
- rating (integer 1-5, when supplied)
- optional_comment (privacy-filtered)
- sentiment_signal
- feedback_channel
- attributed_agent_action

A missing rating must remain missing; it must not be invented or converted to zero.

## 4. Resolution Outcome Event

Required fields:
- outcome_event_id
- issue_reference
- outcome_classification
- resolution_timestamp
- repeat_contact_window (7, 14 or 30 days)
- escalation_status
- verification_status

## 5. Candidate Release Record

Required fields:
- candidate_version
- baseline_version
- safety_suite_version
- safety_cases_total
- safety_cases_passed
- safety_cases_failed
- quality_metric_comparison
- human_approval
- rollout_stage
- rollback_version

## 6. Data Governance

- Apply data minimisation.
- Use pseudonymous references.
- Restrict access by role.
- Encrypt data in transit and at rest.
- Maintain retention and deletion rules.
- Record data and model versions.
- Prevent unapproved feedback from entering candidate training data.

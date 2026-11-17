# Changelog

## Day 1 - Initial project setup
- Connected the local project to the NexBank GitHub repository.
- Created the required documentation and project directory structure.
- Added initial requirements analysis.
- Added requirements traceability matrix.
- Added high-level system architecture.

## 2026-11-15 — Day 02: Intent Taxonomy and NLU Design
- Created a 35-intent hierarchical taxonomy across six primary intent groups.
- Preserved the required account, transaction, card, product, complaint, and security intent identifiers from the project brief.
- Added general assistance and out-of-scope classifications.
- Defined entity extraction, validation, privacy, and slot-filling rules.
- Documented all six required overlapping-intent pairs and clarification strategies.
- Added proposed confidence thresholds, multi-intent handling, and out-of-scope rules.
- Design decision: card management is represented as a secondary group under the transaction primary category while retaining CRD identifiers.
- Open work: create at least 10 sample utterances per intent and validate the confidence thresholds against a labelled dataset.
- Next: build the utterance library and NLU evaluation scenarios.

## 2026-11-15 — Day 02: Intent Taxonomy and NLU Design
- Created a 35-intent hierarchical taxonomy across six primary intent groups.
- Preserved the required account, transaction, card, product, complaint, and security intent identifiers from the project brief.
- Added general assistance and out-of-scope classifications.
- Defined entity extraction, validation, privacy, and slot-filling rules.
- Documented all six required overlapping-intent pairs and clarification strategies.
- Added proposed confidence thresholds, multi-intent handling, and out-of-scope rules.
- Design decision: card management is represented as a secondary group under the transaction primary category while retaining CRD identifiers.
- Open work: create at least 10 sample utterances per intent and validate the confidence thresholds against a labelled dataset.
- Next: build the utterance library and NLU evaluation scenarios.

## Day 04 – Security and Guardrails

- Added financial advice and account security guardrail specification.
- Documented regulatory compliance controls and six adversarial attack vectors.
- Created 60 adversarial test cases across six attack categories.
- Added false-positive analysis with 10 legitimate-request scenarios.
- Documented safety monitoring, audit logging, dashboards and incident response.
- Defined fail-closed behaviour for security-critical failures.


## Day 05 - Continuous Learning Pipeline

- Designed the feedback pipeline using supervisor corrections, customer satisfaction and resolution outcomes.
- Added supervisor sampling, correction taxonomy, severity levels and propagation timelines.
- Documented CSAT, sentiment, feedback attribution and bias correction.
- Added resolution outcome classification and 7/14/30-day repeat-contact tracking.
- Created a fixed 200-case safety regression test fixture.
- Defined human approval, adversarial validation, gradual rollout and automatic rollback requirements.
- Added synthetic feedback events and an illustrative CSAT +0.3 boss-challenge simulation.
- Clarified that model training and live safety evaluation have not yet been performed.


## 2026-11-17 - Day 06: NLU Pipeline Finalisation and Evaluation

- Finalised the 35-intent taxonomy and reused the existing 350-example utterance library.
- Preserved the held-out test split and generated 105 held-out NLU evaluation examples.
- Added targeted tests for all six overlapping-intent pairs, multi-intent requests, out-of-scope messages and seven supported languages.
- Documented the NLU processing sequence, confidence handling, entity validation and evaluation metrics.
- Added NLU pipeline configuration and test execution instructions.
- Design decision: ambiguous or intermediate-confidence requests are clarified rather than automatically accepted until confidence thresholds are calibrated.
- Limitation: evaluation cases are fixtures and have not been executed against a trained classifier.
- Next: proceed to the next project phase, Knowledge Base and Retrieval Architecture.

## 2026-11-17 — Day 06: Escalation and Customer Satisfaction

- Added all 15 escalation trigger conditions from the project brief, including priority, queue and SLA.
- Added escalation decision logic, eight-element handoff context, queue overflow, after-hours handling and de-escalation governance.
- Created 10 ambiguous escalation test scenarios with expected routing and documented reasoning.
- Added customer satisfaction collection, CSAT calculation, implicit feedback, bias correction and outcome tracking.
- Specified real-time, daily and weekly dashboard wireframes.
- Added machine-readable escalation and satisfaction configuration.
- Limitation: routing scenarios are test fixtures; automated routing execution and the 9/10 boss challenge have not yet been verified.

## 2026-11-17 — Day 07: Final Integration and Submission Preparation

- Created 20 individual sample conversation flows covering account, transaction, card, product, complaint, security and escalation scenarios.
- Created a 25-turn integration challenge spanning account balance, suspected fraud and complaint registration.
- Included authentication, guardrail activation, sentiment recovery and P0 escalation.
- Added interaction-level and turn-level audit logging specifications.
- Added technical, business and ethical risk assessment.
- Added five mandatory conversation design patterns and eight anti-pattern review criteria.
- Added a provisional 10-item safety submission checklist. The original brief references ten automatic failure conditions but does not enumerate them in the accessible submission section; exact official criteria remain to be confirmed.
- Added a system integration map and submission navigation.
- Limitation: all scenarios are synthetic design fixtures; no integrated production agent or automated zero-violation result is claimed.
- Open work: manual conversation review, executable integration tests, official failure-condition confirmation, current regulatory verification and repository transfer.
- Next: complete final review and submit the repository after authorised access is arranged.

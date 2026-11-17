# NexBank NLU Pipeline and Evaluation Specification

## 1. Purpose

Finalise the hierarchical Natural Language Understanding pipeline for customer intent classification, entity extraction, slot filling, ambiguity resolution and multi-intent handling.

## 2. Three-Level Classification

The NLU pipeline follows:

1. Primary intent group
2. Secondary intent category
3. Tertiary intent or specific customer task

The taxonomy contains 35 intent categories across:
- Account Management
- Transaction and Payments
- Card Management
- Product and Advisory
- Complaint and Feedback
- Security and Fraud
- General Assistance and Out-of-Scope handling

The existing intent identifiers are retained to preserve compatibility with the taxonomy, dialogue state manager and downstream routing.

## 3. NLU Processing Sequence

1. Receive customer message.
2. Detect language and code-switching.
3. Normalise text without losing the original message.
4. Generate candidate primary and secondary intents.
5. Classify the most likely intent and alternative candidates.
6. Extract entities and identify missing required slots.
7. Apply entity validation and authentication requirements.
8. Check overlapping-intent and multi-intent rules.
9. Apply confidence and safety thresholds.
10. Accept, clarify, reject or route to human support.
11. Record the classification decision for evaluation and audit.

## 4. Confidence and Disambiguation

Use the following proposed thresholds:

| Condition | Decision |
|---|---|
| Top confidence >= 0.85 and margin over second candidate >= 0.15 | Accept only when entity and safety evidence agree |
| Top confidence >= 0.70 but margin < 0.15 | Ask a targeted clarification question |
| Top confidence < 0.70 | Clarify or route to human support |
| Strong fraud or security indicator | Apply conservative security handling regardless of ordinary intent ranking |

The 0.70–0.84 confidence band with a margin >= 0.15 requires conservative handling and calibration against labelled data. Until validated, clarification is preferred over an unsupported automatic decision.

Confidence scores are not authentication evidence and must never override security controls.

## 5. Entity Extraction and Slot Filling

- Required slots must be collected before the associated workflow proceeds.
- Optional slots may be requested when they materially improve accuracy.
- Missing or ambiguous values must trigger clarification.
- Sensitive credentials must not be requested or stored.
- Entity extraction does not establish identity or authorisation.
- High-risk changes require the authentication level defined by bank policy.
- Confirmation is required before consequential account workflows proceed.

## 6. Overlapping Intent Resolution

All six required pairs must use entity-based differentiation and clarification:

1. TXN-001 vs TXN-002: transaction status versus dispute.
2. PRD-001 vs PRD-005: product information versus investment advisory.
3. ACC-003 vs ACC-004: contact details versus mailing address.
4. CMP-001 vs CMP-003: new complaint versus existing complaint escalation.
5. SEC-001 vs TXN-002: suspected fraud versus merchant transaction dispute.
6. CRD-001 vs SEC-001: card blocking versus fraud reporting.

A suspected fraud signal takes precedence over routine transaction handling.

## 7. Multi-Intent Processing

- Detect distinct customer goals.
- Assign an intent and confidence score to each goal.
- Extract entities independently.
- Order tasks by safety and urgency.
- Maintain separate task states within the same conversation.
- Clarify when tasks cannot safely be separated.
- Confirm completion independently for each task.

## 8. Out-of-Scope Handling

- Identify requests unrelated to NexBank-supported services.
- Explain supported banking capabilities politely.
- Do not fabricate answers to unrelated requests.
- Preserve the original customer request for audit.
- Route ambiguous banking and regulatory matters to an appropriate human team.
- Treat prompt injection and attempts to obtain protected system information as security events, not ordinary out-of-scope questions.

## 9. Multilingual Handling

Primary languages:
- English
- Hindi
- Hinglish

Secondary languages:
- Tamil
- Telugu
- Bengali
- Marathi
- Gujarati

The pipeline must support:
- Language detection.
- Code-switching.
- Transliteration.
- Spelling variation.
- Language preference carry-over.
- Context from previous turns.
- Clarification in the customer's preferred supported language.

The Day 06 challenge dataset includes examples across all seven specified languages. These are test fixtures, not proof of measured multilingual accuracy.

## 10. Evaluation Dataset

The evaluation dataset combines:
- Held-out examples from the existing sample utterance test split.
- Six overlapping-intent challenge cases.
- Multi-intent examples.
- Out-of-scope examples.
- Multilingual examples.

The existing utterance library contains 350 examples, with 10 per intent and a 7/3 train/test split. The held-out test examples must remain excluded from training.

## 11. Evaluation Metrics

| Metric | Purpose |
|---|---|
| Intent accuracy | Overall correct intent classifications |
| Per-intent precision | Correct positive predictions for each intent |
| Per-intent recall | Ability to identify actual examples of each intent |
| Macro F1 | Balanced performance across intent categories |
| Confusion matrix | Identify frequently confused intent pairs |
| Entity precision and recall | Evaluate extracted entities |
| Slot completion rate | Measure required-slot collection |
| Clarification rate | Measure cases requiring additional customer input |
| Out-of-scope detection rate | Measure correct handling of unsupported requests |
| Multi-intent exact-match rate | Measure correct identification of all goals |
| Language-wise accuracy | Compare performance across supported languages |

Report metrics by intent and language. Do not rely only on aggregate accuracy because rare high-risk intents may be hidden by common low-risk intents.

## 12. Evaluation Procedure

1. Freeze the taxonomy and dataset version.
2. Keep training and test examples separate.
3. Run classification on held-out utterances.
4. Compare predicted and expected intent labels.
5. Calculate accuracy, precision, recall and macro F1.
6. Inspect the confusion matrix and overlapping pairs.
7. Evaluate entity extraction and required-slot completion separately.
8. Review multi-intent, out-of-scope and multilingual cases.
9. Analyse false positives and false negatives.
10. Record limitations and approve changes before updating the taxonomy.

## 13. Limitations and Open Work

- Template-generated utterances may not represent natural customer language.
- The current dataset is small for production-level model evaluation.
- Multilingual challenge examples require review by fluent speakers.
- Confidence thresholds require calibration against a labelled validation dataset.
- Production performance must be measured using representative, privacy-approved data.

No accuracy or F1 score is claimed until the evaluation is executed by an implemented classifier.

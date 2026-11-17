# Customer Satisfaction and Resolution Outcome Tracking

## 1. Customer Satisfaction Signal

The system collects customer satisfaction through explicit and implicit feedback.

### Explicit feedback

- In-conversation sentiment checks at natural breakpoints.
- Post-conversation CSAT rating from 1 to 5.
- Optional free-text comments.
- Feedback linked to the relevant conversation and agent actions.

### Implicit feedback

- Resolution without human escalation.
- Repeat visits or contacts.
- Time taken to resolve the issue.
- Customer abandoning an unresolved conversation.
- Customer requesting a human agent.
- Customer returning with the same issue.

An implicit signal must not be treated as definitive proof of satisfaction.

## 2. Sentiment Monitoring

Sentiment should be evaluated at natural conversation breakpoints rather than after every message.

Dissatisfaction may be detected even when a customer does not submit an explicit rating.

When dissatisfaction is detected:
1. Acknowledge the customer's concern.
2. Reassess whether the current answer resolved the issue.
3. Offer clarification or an appropriate next step.
4. Escalate when the applicable escalation conditions are met.

## 3. CSAT Measurement

CSAT = Sum of valid customer ratings / Number of valid ratings.

Ratings range from 1 to 5.

The reporting process must record:
- Number of ratings received.
- Average rating.
- Rating distribution.
- Feedback response rate.
- Results by intent, channel and agent version.
- Change against the approved baseline.

## 4. Feedback Bias Correction

- Do not assume customers who submit ratings represent all customers.
- Track feedback response rates.
- Compare ratings across channels, languages and intent categories.
- Monitor differences between customers who rate and those who do not.
- Avoid using a single rating as the sole basis for model changes.
- Do not use protected or unnecessary personal attributes to optimise ratings.
- Review suspicious or duplicated feedback.

## 5. Feedback Attribution

Where possible, connect customer feedback to:
- Intent classification.
- Relevant agent response.
- Knowledge-base version.
- Escalation decision.
- Resolution action.
- Agent and prompt version.

This helps identify which part of the customer journey contributed to the feedback.

## 6. Resolution Outcome Verification

The system should use approved follow-up mechanisms to check whether the customer's issue was actually resolved.

Repeat contacts must be tracked over 7, 14 and 30 days.

### Required outcome classifications

| Classification | Meaning |
|---|---|
| resolved-first-contact | Resolved during the first interaction |
| resolved-with-escalation | Resolved after transfer to human support |
| unresolved-dropped | Customer left without confirmed resolution |
| unresolved-escalated | Escalated but not yet resolved |
| false-resolution | Agent marked the issue resolved, but subsequent evidence shows it was not |

## 7. Long-Term Outcome Tracking

Where lawful and appropriately authorised, analyse:
- Repeat contact patterns.
- Customer retention trends.
- Product adoption trends.
- Recurring complaint categories.
- Long-term resolution quality.

These outcomes are aggregate quality signals and must not be used to infer unsupported individual financial suitability.

## 8. Reporting

Report CSAT, resolution rate, repeat contacts, unresolved cases and escalation outcomes separately.

A high CSAT score must never compensate for a safety failure.

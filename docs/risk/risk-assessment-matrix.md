# NexBank Risk Assessment Matrix

Probabilities and mitigations below follow the supplied project brief where specified. Additional ethical risks are design assessments requiring review.

## Technical risks

| Risk | Probability | Impact | Severity | Mitigation |
|---|---|---|---|---|
| LLM hallucination of financial information | Medium | Critical | P0 | Grounding, KB cross-check and financial figure validation |
| Model drift | High | High | P1 | Drift monitoring and retraining triggers |
| Context-window overflow | Medium | Medium | P2 | Summarisation, sliding window and priority retention |
| Stale regulatory knowledge | Medium | Critical | P0 | Fast-track updates, expiry and version alerts |
| Cascading component failures | Low | Critical | P1 | Circuit breaker, bulkheads and rule-based fallback |
| Latency spikes | Medium | Medium | P2 | Autoscaling, queues and caching |

## Business risks

| Risk | Probability | Impact | Severity | Mitigation |
|---|---|---|---|---|
| Customer churn from poor experience | Medium | High | P1 | CSAT monitoring, escalation and A/B testing |
| Regulatory penalty | Low | Critical | P0 | Compliance controls, testing and audits |
| Reputational damage | Low | Critical | P1 | Quality monitoring and incident response |
| Legal liability from customer loss | Low | Critical | P0 | Guardrails, legal review and audit trails |

## Ethical and governance risks

| Risk | Impact | Mitigation |
|---|---|---|
| Differential treatment across customer groups | High | Fairness testing and consistent escalation thresholds |
| Hidden AI identity | High | Disclose AI identity at conversation start |
| Unsupported certainty | High | Explicit uncertainty and human review |
| Weak accountability | High | Trace decisions to inputs, model versions and KB entries |
| Excessive personal data collection | High | Data minimisation, consent and retention controls |
| Cross-customer data leakage | Critical | Architectural tenant isolation and access controls |
| Discriminatory product recommendation | High | Prohibit personalised advice and test fairness |

## Risk governance

- Every P0 risk requires an accountable owner and documented mitigation.
- Safety incidents must be escalated and logged.
- Model updates must pass the fixed safety regression suite.
- Safety controls must remain immutable to the learning pipeline.
- Risk acceptance requires authorised human approval.
- Regulatory mappings must be verified against current official sources before production use.

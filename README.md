# NexBank - Agentic AI Customer Service Agent with Feedback Loops

A 15-day project to design a production-grade conversational Agentic AI customer service system for a fictional Indian neo-bank.

## Project context

- Active customers: 2.7 million
- Daily interactions: approximately 18,000
- Service domains: account queries, transaction disputes, product information and complaints
- Core requirements: dialogue state, hierarchical NLU, knowledge retrieval, safety guardrails, human escalation and continuous learning

## Documentation

- Requirements: `docs/requirements/`
- Architecture: `docs/architecture/`
- Intent taxonomy: `docs/intent-taxonomy/`
- Knowledge base: `docs/knowledge-base/`
- Guardrails: `docs/guardrails/`
- Learning pipeline: `docs/learning-pipeline/`
- Escalation: `docs/escalation/`
- Metrics: `docs/metrics/`

## Safety notice

This is an educational design and prototype. It does not connect to real banking systems or process real customer transactions. Simulated data must be used.

## Progress

- [x] Day 1 initial requirements analysis
- [x] Day 1 requirements traceability matrix
- [x] Day 1 high-level architecture
- [ ] Detailed dialogue state machine
- [ ] Component interface contracts
- [ ] Failure-mode analysis
- [ ] Latency and scalability specification

## Final integration and submission materials

- `simulations/conversations/` — 20 individual sample conversation flows.
- `simulations/integration/25-turn-boss-challenge.md` — three-intent integration journey.
- `docs/audit/` — interaction-level and turn-level audit logging specification.
- `docs/risk/` — technical, business and ethical risk assessment.
- `docs/submission/` — integration map, conversation quality gate and provisional failure checklist.
- `tests/integration/` — final integration validation materials.

All conversations are synthetic design examples. They are not production transcripts or evidence of a deployed agent.

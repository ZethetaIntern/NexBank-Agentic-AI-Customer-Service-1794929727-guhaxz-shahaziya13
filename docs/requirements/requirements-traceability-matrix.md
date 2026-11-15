# Requirements Traceability Matrix

| ID | Requirement | Planned component / document | Validation evidence |
|---|---|---|---|
| FR-01 | Accept customer queries | Channel/API layer | Channel input tests |
| FR-02 | Hierarchical intent classification | NLU and intent taxonomy | Intent evaluation |
| FR-03 | Entity extraction and slot filling | NLU and dialogue manager | Entity and slot tests |
| FR-04 | Multi-turn dialogue state | Dialogue state manager | Conversation simulations |
| FR-05 | Support four service domains | Specialist agents | Domain scenario tests |
| FR-06 | Dynamic knowledge retrieval | Knowledge base and retrieval service | Retrieval latency tests |
| FR-07 | Grounded response generation | Response generator and validator | Grounding tests |
| FR-08 | Authentication and authorisation | Identity/session service | Access-control tests |
| FR-09 | Detect unsafe requests | Safety and policy engine | Adversarial tests |
| FR-10 | Human escalation | Escalation manager | Escalation scenario tests |
| FR-11 | Audit important actions | Audit and observability service | Audit-log inspection |
| FR-12 | Collect feedback | Feedback ingestion pipeline | Feedback pipeline tests |
| FR-13 | Evaluate updates | Evaluation and release pipeline | Regression and canary tests |
| FR-14 | Multilingual support | Language detection and NLU | Language test set |
| NFR-01 | End-to-end latency below 3 seconds | Overall architecture | Performance tests |
| NFR-02 | Retrieval p95 below 200 ms | Retrieval service | Retrieval benchmark |
| NFR-03 | Traffic scalability | Infrastructure and deployment design | Load tests |
| NFR-04 | Secure customer data | Security and access-control design | Security tests |
| NFR-05 | Auditability | Observability and audit service | Audit review |
| NFR-06 | Graceful failure | Component fallback design | Failure-injection tests |
| NFR-07 | Model-provider portability | Model abstraction layer | Provider substitution test |
| NFR-08 | Preserve safety during learning | Immutable safety layer | Safety regression tests |

## Requirement dependencies

1. Channel/API layer depends on authentication and session management.
2. NLU depends on language detection and intent taxonomy.
3. Dialogue management depends on NLU output and stored conversation state.
4. Specialist agents depend on routing, policies and approved knowledge.
5. Response generation depends on retrieved evidence and safety validation.
6. Human escalation depends on risk detection, routing rules and case context.
7. Continuous learning depends on audit data, supervisor corrections and evaluation.
8. Deployment of learned changes depends on passing safety and quality gates.

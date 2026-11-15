# NexBank Customer Service Agent - Requirements Analysis

## 1. Project Overview

NexBank is a fictional Indian neo-bank with 2.7 million active customers and approximately 18,000 daily customer interactions.

The project aims to design a production-grade Agentic AI Customer Service Agent with feedback loops. The system will handle customer interactions autonomously within clearly defined safety boundaries and escalate sensitive or complex cases to human support.

## 2. Business Problem

The existing customer service operation relies on a large human support team. NexBank wants to automate routine first-line support while maintaining customer satisfaction, security, regulatory compliance and reliable human oversight.

The system must not sacrifice customer safety for automation.

## 3. Project Objectives

- Handle routine banking account queries.
- Identify and assist with transaction disputes.
- Provide permitted product information and recommendations.
- Manage customer complaints.
- Maintain context across multiple conversation turns.
- Retrieve accurate information from an approved knowledge base.
- Escalate high-risk and unresolved interactions to human agents.
- Learn from supervisor corrections, customer satisfaction scores and resolution outcomes.
- Preserve safety rules during every learning and update cycle.

## 4. Stakeholders

| Stakeholder | Main responsibility |
|---|---|
| Customers | Ask questions and receive support |
| Customer Support Agents | Handle escalated interactions |
| Support Supervisors | Review cases and correct responses |
| Compliance Team | Define regulatory and operational requirements |
| Security Team | Protect customer information and account access |
| Product Team | Maintain accurate product information |
| Engineering Team | Develop and operate the AI system |
| Risk Committee | Review safety and operational risks |
| Customer Experience Board | Monitor service quality and satisfaction |

## 5. Functional Requirements

FR-01: Accept customer queries through supported conversational channels.

FR-02: Identify customer intent using hierarchical intent classification.

FR-03: Extract entities and fill missing conversation slots.

FR-04: Maintain dialogue state across multiple turns.

FR-05: Support account queries, transaction disputes, product information and complaints.

FR-06: Retrieve relevant information from a dynamic knowledge base.

FR-07: Generate responses grounded in approved information.

FR-08: Apply authentication and authorisation before protected account operations.

FR-09: Detect unsafe, ambiguous and high-risk requests.

FR-10: Escalate eligible interactions to human support.

FR-11: Record conversation decisions and important actions for audit.

FR-12: Collect supervisor corrections, customer satisfaction scores and resolution outcomes.

FR-13: Evaluate proposed improvements before deployment.

FR-14: Support English, Hindi and Hinglish, with additional Indian languages considered.

## 6. Non-Functional Requirements

NFR-01: Target end-to-end response time must remain below 3 seconds under the assignment's defined performance conditions.

NFR-02: Knowledge retrieval p95 latency target must be below 200 milliseconds.

NFR-03: Architecture must support the stated daily interaction volume and planned traffic growth.

NFR-04: Customer data must be protected through authentication, access control and secure handling.

NFR-05: System decisions must be observable and auditable.

NFR-06: Components must support graceful failure and recovery.

NFR-07: The architecture must support model-provider replacement.

NFR-08: Learning updates must not weaken immutable safety controls.

## 7. Safety Requirements

- Never disclose protected account information without appropriate authentication.
- Never request or expose customer passwords, PINs or OTPs.
- Never perform sensitive account changes without required authorisation and confirmation.
- Never invent account balances, transaction statuses or banking policies.
- Do not provide unauthorised personalised financial or investment advice.
- Escalate fraud, security incidents and other high-risk cases.
- Keep human review available for decisions requiring judgement.
- Preserve an auditable record of important decisions.

## 8. Scope

### In scope
- Conversational AI architecture.
- Intent classification and dialogue state management.
- Knowledge retrieval and response generation.
- Banking safety guardrails.
- Human escalation.
- Feedback and continuous learning.
- Evaluation, monitoring and audit design.

### Out of scope
- Connecting to real customer bank accounts.
- Executing real financial transactions.
- Accessing production banking databases.
- Making autonomous credit approval decisions.

All prototype interactions will use simulated customer and transaction data.

## 9. Proposed Success Measures

The following are project validation targets, not measured results:

- End-to-end response time: below 3 seconds.
- Knowledge retrieval p95: below 200 milliseconds.
- Customer satisfaction target: 4.5/5.
- No incorrect financial advice in the defined safety evaluation scenarios.
- No unauthorised account changes.
- Successful escalation of all applicable critical-risk test cases.

## 10. Project Constraints and Assumptions

- NexBank is fictional.
- Real banking credentials and customer records will not be used.
- Regulatory requirements must be verified against authoritative sources before implementation.
- LLM providers must be replaceable.
- Human oversight is mandatory for defined high-risk interactions.

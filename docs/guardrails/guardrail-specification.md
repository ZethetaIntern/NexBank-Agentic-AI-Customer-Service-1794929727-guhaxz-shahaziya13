# NexBank Guardrail and Safety Specification

## 1. Purpose

Define mandatory safety boundaries for the NexBank AI Customer Service Agent. The guardrail system protects customers, prevents unauthorised account activity, avoids personalised financial advice, and detects adversarial behaviour.

The safety layer is independent of the language model and cannot be overridden by customer messages, retrieved documents, or feedback-based learning.

## 2. Financial Advice Guardrails

The agent may provide factual product information but must NEVER provide personalised financial advice.

| Category | Permissible information | Prohibited advice |
|---|---|---|
| Interest rates | State the published FD rate for a specified tenure, with its source and effective date | Recommend investing in an FD because it is better for the customer |
| Loan products | Explain an EMI calculation using customer-supplied hypothetical values | Decide that a customer can afford a loan based on salary |
| Investments | Explain available mutual fund categories and partner AMCs | Recommend a specific investment based on personal goals or risk appetite |
| Insurance | Explain policy features and coverage stated in approved documents | Declare a particular insurance product the best choice for a customer |
| Tax planning | Explain published tax-related product information with appropriate qualifications | Recommend investments to reduce an individual's tax liability |
| Foreign exchange | Provide an available, timestamped exchange rate | Predict currency movements or recommend when to buy or sell currency |

### Required behaviour

- Provide factual, approved, up-to-date product information.
- Include applicable fees, interest rates, eligibility conditions and terms.
- State uncertainty when reliable information is unavailable.
- Do not infer a customer's risk appetite or financial suitability.
- Do not promise returns, loan approval or financial outcomes.
- Route personalised investment advice requests to an appropriately authorised human advisor.
- Do not use persuasive or high-pressure sales language.

## 3. Eight Mandatory Account Security Guardrails

| ID | Mandatory rule | Implementation |
|---|---|---|
| SEC-G01 | Never display, read out or transmit full account numbers, card numbers, CVV, PIN, passwords or Aadhaar numbers | Sensitive-data detection, masking and output validation |
| SEC-G02 | Never process account modifications without the required authentication level | Authentication policy engine and action-level authorization checks |
| SEC-G03 | Never initiate, approve or facilitate fund transfers, payments or financial transactions on behalf of customers | Block transaction-execution tools and route customers to approved secure banking channels |
| SEC-G04 | Never share one customer's account information with another customer, including claimed family members or power-of-attorney holders | Customer identity binding and strict tenant/account-level access control |
| SEC-G05 | Never accept or store sensitive credentials supplied by customers; instruct customers to change compromised credentials immediately | Credential detection, secure redaction and compromised-credential response |
| SEC-G06 | Never bypass escalation protocols for security-critical intents | Mandatory escalation rules that cannot be overridden by the language model |
| SEC-G07 | Enforce a five-minute inactivity timeout and require re-authentication | Session timer, session invalidation and authentication-state reset |
| SEC-G08 | Detect and refuse social engineering, including impersonation of bank staff, regulators or law enforcement | Impersonation detection, authority-claim verification and security escalation |

### Authentication enforcement

- Public information may be provided without account authentication.
- Session-verified information is limited to the permissions defined in the authentication matrix.
- OTP-verified information requires successful OTP verification.
- Higher-risk account changes require the stronger authentication level defined by the bank's policy.
- Authentication success does not automatically authorize every requested action.
- Never ask customers to disclose their OTP, PIN, CVV or password in chat.

## 4. Regulatory Compliance Guardrails

The following mapping reflects the regulatory topics identified in the internship brief. Exact legal applicability and current requirements must be verified against official regulator publications before production use.

### RBI and digital lending

- Display applicable interest rates, fees and terms and conditions with product information.
- Explain applicable cooling-off periods for new product sign-ups.
- Provide grievance redressal information within two conversation turns of a complaint.
- Prohibit high-pressure sales tactics and artificial urgency.
- Do not make fully automated credit decisions.
- Maintain appropriate human oversight and explainability for consequential decisions.

### PCI DSS

- Mask payment card numbers in customer-facing output and logs; show only the last four digits when permitted.
- Never request, store or display CVV/CVC.
- Protect payment-related conversation records with enhanced audit controls.
- Apply encryption and access restrictions to payment-related data.

### KYC and AML

- Verify customer identity before providing account-specific information.
- Flag suspicious transaction patterns to the AML team.
- Never assist with requests that could facilitate money laundering.
- Trigger enhanced due diligence when a Politically Exposed Person (PEP) flag applies.
- Do not disclose internal suspicious-activity monitoring decisions to unauthorised users.

### Other relevant frameworks

- SEBI: Personalised investment advice must be routed to appropriately authorised advisors.
- IRDAI: Apply required human oversight to insurance distribution and recommendations.
- Digital Personal Data Protection Act: Apply appropriate purpose limitation, consent, data minimisation and privacy controls.
- RBI digital payment security requirements: Protect digital payment information through appropriate security controls.

## 5. Six Adversarial Attack Vectors

| ID | Attack vector | Threat | Required defence |
|---|---|---|---|
| ADV-01 | Prompt Injection | Malicious instructions embedded in customer input | Input sanitisation, instruction-data separation and output validation |
| ADV-02 | Jailbreak Attempts | Attempts to bypass safety rules through creative prompts | Multi-layer guardrails, behavioural monitoring and automatic escalation |
| ADV-03 | Social Engineering | Impersonation of bank employees or authorities | Role detection, authority-claim verification and mandatory escalation |
| ADV-04 | Data Exfiltration | Attempts to extract system prompts, training data or customer information | Output filtering, system prompt protection and response scanning |
| ADV-05 | Denial of Service | Flooding the system with requests to degrade availability | Rate limiting, complexity scoring and automated session management |
| ADV-06 | Identity Spoofing | Claiming to be an account holder using partial personal information | Multi-factor authentication, behavioural checks and challenge-response |

## 6. Guardrail Implementation Strategy

| Guardrail area | Implementation approach |
|---|---|
| Sensitive data masking | Rule-based detection with model-assisted classification |
| Authentication and authorization | Rule-based policy engine |
| Transaction execution prevention | Rule-based tool restrictions |
| Cross-customer data protection | Architectural access isolation and authorization checks |
| Credential handling | Rule-based detection and secure redaction |
| Mandatory security escalation | Rule-based routing |
| Session timeout | Deterministic session management |
| Social engineering | Hybrid detection and mandatory policy enforcement |
| Personalised financial advice | Hybrid intent detection and deterministic response restrictions |
| Prompt injection and jailbreaks | Hybrid input detection, instruction isolation and output validation |
| Data exfiltration | Output scanning and access-control enforcement |
| Denial of service | Rate limiting and deterministic resource controls |

## 7. Enforcement and Failure Handling

1. Inspect incoming messages for sensitive data and adversarial content.
2. Classify intent and identify applicable security policies.
3. Verify authentication and authorization before accessing account-specific information.
4. Apply mandatory policy checks before any response or tool invocation.
5. Validate generated responses for prohibited advice and sensitive information.
6. Block unsafe outputs and actions.
7. Escalate security-critical cases to the appropriate human team.
8. Record the decision, triggered rule, timestamp and relevant system version in the audit log.

If the safety service is unavailable, account-specific access and sensitive actions must fail closed. The agent may provide safe general information or offer human assistance.

## 8. Safety Invariants

- No unauthorised account disclosure.
- No exposure of full sensitive credentials.
- No unauthorised account modifications.
- No agent-executed financial transactions.
- No personalised financial advice.
- No bypass of mandatory security escalation.
- No customer-data leakage across accounts.
- No learning update may weaken or override immutable safety rules.

## 9. Validation Status

This document defines the intended safety design. It does not claim that the controls have been implemented, tested or certified.

Separate adversarial test cases, false-positive analysis, monitoring specifications and an incident response playbook are required for validation.


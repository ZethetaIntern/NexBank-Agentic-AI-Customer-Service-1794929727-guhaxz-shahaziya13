# Knowledge Maintenance and Access Control

## 1. Update workflow

1. Knowledge owner submits a new entry or change.
2. System validates schema, source and metadata.
3. Compliance review is required for regulatory or safety-related content.
4. Product owner reviews product and operational content.
5. Approved version is indexed in the retrieval systems.
6. Smoke tests and retrieval checks are performed.
7. Version is published with an effective date.
8. Previous version is retained for rollback.

## 2. Approval roles

| Knowledge type | Required approval |
|---|---|
| Product information | Product owner |
| General FAQ | Customer support knowledge owner |
| Account and transaction procedures | Banking operations |
| Security guidance | Security team |
| Regulatory content | Compliance officer |
| Safety-critical policy | Compliance and risk approval |

## 3. RBI regulatory knowledge management
- Monitor official RBI publications and circulars.
- Record circular number, title, source URL and publication date.
- Record effective date and affected business process.
- Identify impacted knowledge entries and system prompts.
- Require compliance review before publication.
- Preserve superseded circular references.
- Run regression tests before deployment.
- Never treat an unverified summary as an authoritative regulatory instruction.

Official source: https://www.rbi.org.in/

Other relevant official sources:
- NPCI: https://www.npci.org.in/
- SEBI: https://www.sebi.gov.in/
- IRDAI: https://www.irdai.gov.in/

## 4. Freshness and TTL policy

| Content type | Proposed review interval |
|---|---|
| Promotions | 1 day |
| Operational incidents | 1 day |
| Product information | 30 days |
| FAQs | 90 days |
| Internal procedures | 90 days |
| Regulatory content | Review on every relevant update |

TTL is a review trigger, not permission to extend expired content. Expired regulatory content must not be presented as current.

## 5. Access control matrix

| Authentication level | Permitted knowledge |
|---|---|
| Public | General product information and FAQs |
| Session verified | General account-support procedures |
| OTP verified | Protected account and transaction guidance |
| Biometric verified | Sensitive profile-change procedures |
| Full KYC | High-risk account procedures, subject to required approvals |
| Human officer | Role-authorized operational and case information |

Authentication does not independently authorize a transaction or account change. Additional permissions and explicit confirmation are required.

## 6. Rollback
- Retain the last approved version.
- Disable the faulty version.
- Restore the previous approved version.
- Rebuild affected search indexes.
- Verify retrieval and response quality.
- Record rollback reason, approver and timestamp.

## 7. Audit requirements
Record entry ID, version, author, reviewer, approval status, source, effective date, deployment time, rollback events and retrieval references.

## 8. Security
- Apply access filtering before retrieval.
- Prevent unauthorized cross-customer data access.
- Encrypt stored knowledge and audit records.
- Exclude secrets and customer PII from sample datasets.
- Restrict publishing permissions by role.

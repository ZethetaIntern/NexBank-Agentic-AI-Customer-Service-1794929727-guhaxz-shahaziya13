# NexBank Knowledge Base Schema

## 1. Purpose
Provide versioned, traceable and access-controlled knowledge for the NexBank customer service agent.

## 2. Knowledge categories
- Product information
- Banking policies
- Regulatory requirements
- Frequently asked questions
- Troubleshooting procedures
- Escalation procedures
- Account and transaction support
- Card services
- Security guidance
- Deposits and lending

## 3. Entity relationship model

KnowledgeEntry (1) ---- (M) KnowledgeVersion
KnowledgeEntry (M) ---- (M) KnowledgeTag
KnowledgeVersion (M) ---- (1) SourceReference
KnowledgeVersion (M) ---- (1) ApprovalRecord

## 4. KnowledgeEntry fields

| Field | Type | Description |
|---|---|---|
| entry_id | String | Unique KB identifier |
| title | String | Entry title |
| category | Enum | Knowledge category |
| content | Text | Knowledge content |
| tags | Array | Search and classification tags |
| auth_level | Enum | Minimum authentication |
| language | String | Content language |
| source | String | Origin of information |
| version | String | Version identifier |
| status | Enum | Draft, approved, retired |
| effective_date | Date | Start of validity |
| expiry_date | Date | End of validity |
| ttl_days | Integer | Freshness period |
| approval_id | String | Approval record reference |

## 5. Versioning
Every update creates a new immutable version. Previous approved versions remain available for rollback. Only approved and currently effective versions may be used for customer responses.

## 6. Data representation
- Structured: JSON key-value records and relational metadata.
- Semi-structured: JSON/YAML product and policy documents.
- Unstructured: searchable natural-language passages.
- Regulatory: source, circular identifier, publication date, effective date and compliance approval metadata.

## 7. Data integrity
- Unique entry IDs.
- Mandatory source and version metadata.
- Approval before publication.
- Expired content excluded from retrieval.
- Audit trail for every change.
- No real customer PII in sample knowledge records.

## 8. Important limitation
All sample entries are fictional design examples. They are not approved NexBank policies or verified regulatory advice.

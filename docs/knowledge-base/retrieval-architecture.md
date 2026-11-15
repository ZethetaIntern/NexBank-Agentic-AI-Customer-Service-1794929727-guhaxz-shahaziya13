# NexBank Retrieval Architecture

## 1. Selected approach
Hybrid retrieval combining dense vector search and sparse BM25 search.

Initial fusion weights:
- Dense retrieval: 0.60
- Sparse BM25 retrieval: 0.40

These are proposed starting values and require evaluation against a labelled query dataset.

## 2. Retrieval pipeline

Customer query
  -> Language detection
  -> Context and dialogue-state extraction
  -> Query modification
  -> Access-control filtering
  -> Dense retrieval
  -> Sparse BM25 retrieval
  -> Reciprocal rank / weighted fusion
  -> Cross-encoder reranking
  -> Confidence evaluation
  -> Grounded response generation
  -> Response safety validation

## 3. Dense retrieval
Convert approved knowledge passages and customer queries into embeddings. Retrieve semantically similar passages using vector similarity.

## 4. Sparse retrieval
Use BM25 to retrieve exact terms, product names, transaction terminology and regulatory identifiers.

## 5. Fusion
Combine dense and sparse rankings using weighted reciprocal rank fusion.

Proposed formula:
Score(d) = 0.60 x DenseScore(d) + 0.40 x SparseScore(d)

Normalize component scores before applying weighted fusion.

## 6. Cross-encoder reranking
Retrieve an initial candidate set, then score query-document pairs using a cross-encoder. Return the highest-ranked relevant passages after checking status, freshness and permissions.

## 7. Contextual query modification
Use:
- Current user message
- Previous conversation turns
- Active intent
- Filled and missing slots
- Detected language
- Relevant entity values

Resolve references such as "that transaction" using dialogue state. Never invent missing account identifiers or transaction details.

## 8. Initial confidence policy

| Confidence | Action |
|---|---|
| >= 0.85 | Use grounded result if all safety checks pass |
| 0.65 - 0.84 | Ask clarification or retrieve additional evidence |
| < 0.65 | Acknowledge uncertainty and offer human assistance |

Thresholds are proposed and must be calibrated using labelled evaluation data. Confidence alone never authorizes financial actions.

## 9. Latency budget

Target: retrieval p95 <= 200 ms.

| Operation | Proposed budget |
|---|---:|
| Query processing | 20 ms |
| Dense retrieval | 55 ms |
| Sparse retrieval | 35 ms |
| Fusion and filtering | 15 ms |
| Reranking | 60 ms |
| Final checks | 15 ms |
| Total | 200 ms |

These are design budgets, not measured performance.

## 10. No-result fallback
- Do not invent an answer.
- Try a safe query reformulation.
- Ask one relevant clarification.
- Check whether the knowledge is expired or inaccessible.
- Escalate unresolved or high-risk requests.

## 11. Evaluation metrics
Recall@5, Precision@5, MRR, nDCG, retrieval p50/p95 latency, no-result rate, stale-document rate and grounded-answer accuracy.

# Latency and Scalability

## End-to-End Latency Budget

Assignment target: end-to-end response time below 3 seconds.

| Component | Proposed Budget |
|---|---:|
| API gateway and request validation | 100 ms |
| Authentication and session lookup | 150 ms |
| Intent detection and entity extraction | 350 ms |
| Dialogue state and routing | 100 ms |
| Knowledge retrieval | 200 ms |
| Agent reasoning and response generation | 1700 ms |
| Safety validation and response delivery | 300 ms |
| Total | 2900 ms |

These are proposed engineering budgets, not measured performance results. Actual latency must be established through testing.

## Knowledge Retrieval
Target: p95 retrieval latency below 200 ms.

Potential techniques:
- Hybrid keyword and vector retrieval.
- Indexed metadata filtering.
- Cached frequently accessed approved entries.
- Bounded retrieval result sizes.
- Monitoring of p50, p95, and p99 latency.

## Scalability Strategy

### 1x Load
Support the initial expected workload with a modular application, persistent session storage, and basic monitoring.

### 10x Load
Introduce horizontal API and worker scaling, Redis caching, database connection pooling, and asynchronous processing for non-blocking tasks.

### 100x Load
Use independently scalable services, partitioned event processing, database read replicas or suitable partitioning, distributed caching, queue-based workloads, and automated capacity management.

## Reliability and Monitoring
Track request rate, error rate, response latency, retrieval latency, queue depth, agent failures, and resource utilisation.

## Validation
Run load tests at expected, 10x, and 100x traffic levels. Record throughput, p95/p99 latency, error rate, and resource consumption. Do not report targets as achieved until supported by test results.

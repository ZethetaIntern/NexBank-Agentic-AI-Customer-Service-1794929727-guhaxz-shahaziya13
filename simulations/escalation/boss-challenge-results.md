# Day 06 Boss Challenge — Escalation Routing

## Requirement

Evaluate 10 ambiguous escalation conversations. The project unlock condition is correct routing for at least 9 of 10 cases, with documented reasoning.

## Dataset

`tests/escalation/ambiguous-escalation-cases.csv`

## Current status

- Scenario fixtures created: 10
- Expected routing decisions documented: 10
- Automated routing engine execution: Not performed
- Human review: Pending
- Correctly routed cases: Not measured
- Unlock condition: Not yet verified

The expected decisions are test oracles based on the project trigger matrix. They are not observed test results.

## Review procedure

For each case:
1. Compare the detected signals with the trigger matrix.
2. Verify the priority.
3. Verify the destination queue.
4. Verify the SLA.
5. Check whether a higher-priority trigger takes precedence.
6. Record actual result and pass/fail.
7. Document the reason for any failure.

A minimum of 9 passing cases is required to claim the boss challenge has been passed.

# NLU Evaluation Test Suite

## Files

- `nlu-evaluation-cases.csv`: held-out utterances and targeted challenge cases.
- `../docs/intent-taxonomy/nlu-pipeline-and-evaluation.md`: NLU pipeline and evaluation procedure.

## Test Categories

The CSV includes:
- Held-out intent examples from the existing test split.
- Overlapping-intent cases.
- Multi-intent messages.
- Out-of-scope requests.
- Multilingual examples.

## Execution Status

All records are labelled test fixtures. They have not been executed against a trained or deployed classifier.

## Evaluation Rule

A test passes only when the predicted intent, required entity handling, clarification decision and safety routing match the expected behaviour.

Do not claim model accuracy from the number of test cases or from manually assigned expected labels.

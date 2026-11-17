# NexBank Agentic AI Customer Service

A customer-service agent project for the fictional NexBank scenario.

## Project contents

- Architecture and requirements documentation.
- Hierarchical intent taxonomy and sample utterances.
- Knowledge-base design and sample entries.
- Security guardrails and adversarial test fixtures.
- Feedback and continuous-learning design.
- Escalation and customer-satisfaction framework.
- Twenty scripted conversation scenarios.
- Twenty-five-turn integrated boss challenge.
- FastAPI demonstration application.

## Run the application

    python -m pip install -r requirements.txt
    python -m uvicorn app.main:app --reload

API documentation: http://127.0.0.1:8000/docs

## Run automated tests

    python -m unittest discover -s tests -v

## Important scope statement

The application is a local demonstration prototype using synthetic data. It is not connected to live banking systems. Its intent classifier is deterministic, its knowledge retrieval is lexical, and its state is held in memory. It is not a production banking service.

See `docs/implementation/application-implementation.md` for implementation details and limitations.

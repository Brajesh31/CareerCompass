# ADR 0002: Persist label mapping with the trained pipeline

- **Status:** Proposed
- **Date:** 2026-11-17

## Context

The notebook uses a label encoder, while app.py has a separately maintained mapping. The two are inconsistent for IDs 10–13.

## Decision

Propose packaging text preprocessing, TF-IDF, estimator, and label encoder as a single versioned pipeline artifact. The application should ask the pipeline for the decoded label instead of maintaining a parallel numeric map.

## Consequences

- Training and inference class order can remain synchronized.
- Artifact rebuilds become explicit and testable.
- Migration needs compatibility tests against the existing pickle artifacts.
- This ADR is not implemented by this documentation change.

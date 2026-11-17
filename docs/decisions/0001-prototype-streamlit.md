# ADR 0001: Streamlit prototype as current interface

- **Status:** Accepted as a description of the existing prototype
- **Date:** 2026-11-17

## Context

The repository's active application is a single Streamlit script that coordinates sign-in, upload, preprocessing, prediction, and job lookup.

## Decision

Document the existing Streamlit implementation as the current runtime. This record does not claim it is the ideal long-term architecture or production-ready.

## Consequences

- Setup and operation remain straightforward for a small demonstration.
- Authentication, UI, model, and provider concerns are coupled in one file.
- Unit testing requires future extraction of pure functions and adapters.
- The interface must not be opened to real résumé uploads until the documented blockers are fixed.

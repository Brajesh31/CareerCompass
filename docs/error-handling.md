# 🧯 Error Handling Guide

## Current behavior and gaps

| Stage | Current behavior | Gap |
|---|---|---|
| OAuth | Authorization button and session token gate | No documented lifecycle or sign-out/revocation flow |
| Upload | UTF-8 decode with Latin-1 fallback | No size/type validation; PDF not parsed |
| Cleaning | Regex transformations | No robust empty/invalid input feedback |
| Model | Loads pickle artifacts and predicts | No artifact compatibility or uncertainty handling |
| Job provider | Non-200 response becomes empty list | No timeout; empty and failure are conflated |
| Rendering | Expects provider job fields | Missing fields and unsafe HTML require handling |

## Suggested error categories
`UPLOAD_EMPTY`, `UPLOAD_TOO_LARGE`, `UNSUPPORTED_FILE_TYPE`, `FILE_CONTENT_INVALID`, `TEXT_EXTRACTION_FAILED`, `MODEL_ARTIFACT_UNAVAILABLE`, `MODEL_INFERENCE_FAILED`, `PROVIDER_TIMEOUT`, `PROVIDER_AUTH_FAILED`, `PROVIDER_RATE_LIMITED`, `PROVIDER_BAD_RESPONSE`, and `PROVIDER_EMPTY_RESULT`.

Do not expose stack traces, local paths, secrets, token payloads, raw provider payloads, or résumé content to end users.

## Validation
Test each state with synthetic inputs and mocked services. Confirm messages are useful, accessible, and free of personal or secret values.

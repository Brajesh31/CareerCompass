# 🧪 Testing Strategy

## Current state

No automated application test suite was present in the reviewed repository before this documentation enhancement. The new CI checks are intentionally limited to syntax and documentation hygiene. They do not validate model quality, data rights, security controls, or production readiness.

## Test layers to implement

| Layer | Coverage target |
|---|---|
| Unit | Text cleaning, input validation, category decoding, configuration |
| Model contract | Vectorizer/classifier compatibility, known class IDs, deterministic output |
| Integration | OAuth responses and job-provider success/failure with mocks |
| Upload | Empty, oversized, malformed, extension mismatch, encoding and PDF handling |
| Security | HTML injection, secret leakage, malicious file and pickle provenance controls |
| Accessibility | Keyboard flow, labels, focus, contrast, screen-reader semantics |
| Model evaluation | Leakage-free split, per-class metrics, robustness and bias review |

## Synthetic test inputs

Use fictional text only. Include URLs, hashtags, punctuation, Unicode, misleading substrings such as `RT` and `cc` inside ordinary words, empty content, very long content, and script-like provider strings.

## External calls

Mock OAuth token exchanges and the job provider. Tests must not call the live provider or use production credentials. Cover timeout, non-success status, malformed JSON, missing fields, empty jobs, and unexpected response types.

## Model integrity

A test should assert that the persisted label encoder and estimator agree for every class. The current application hand-written map is known to be inconsistent; do not bless current output by snapshotting the incorrect values.

## Commands

```bash
python -m compileall -q app.py session_state.py
```

A future test suite can be run with:

```bash
python -m pytest
```

The latter command is a target, not a claim that tests currently exist or pass.

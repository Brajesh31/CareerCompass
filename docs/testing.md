# 🧪 Testing Strategy

## Current coverage

| Area | Implemented check | Not covered |
|---|---|---|
| Text cleaning | Isolated regression tests for `clean_resume` | All edge cases and semantic correctness |
| Documentation links | Local relative Markdown link check | Remote links and anchor IDs |
| SVG files | XML well-formedness | Browser rendering and visual quality |
| Python syntax | compileall | Runtime behavior of all components |
| Model pipeline | Not yet automated | Accuracy, fairness, calibration, leakage remediation |
| OAuth/provider | Not yet automated | Live provider calls are deliberately not made |
| Upload/PDF | Not yet automated | PDF structure parsing is not implemented |
| Accessibility | Manual checklist | Formal conformance testing |

## Run locally

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
python scripts/check_repository.py
python -m compileall -q app.py session_state.py scripts
```

The unit test extracts only the pure `clean_resume` function from the Python AST. It does not import the full Streamlit script, so it avoids model deserialization, NLTK downloads, OAuth setup, and provider requests during test collection.

## Next test layers
1. Upload validation: empty, oversized, malformed, and extension/content mismatch.
2. PDF parsing: supported documents, damaged files, parser limits, and extraction quality if PDF support is retained.
3. Label contract: every estimator class ID agrees with the persisted encoder.
4. Model evaluation: split before fitting TF-IDF and report per-class metrics.
5. Provider adapter: mocked success, empty response, invalid JSON, timeout, rate limit, and missing fields.
6. OAuth lifecycle: mocked token exchange, bad state, expiration, and sign-out.
7. Security: unsafe provider strings, secrets, file payloads, and artifact provenance.
8. Accessibility: keyboard, screen reader, focus, contrast, zoom, and responsive layouts.

Use synthetic résumé content only. A passing test suite is not model validation or approval for employment-related decisions.

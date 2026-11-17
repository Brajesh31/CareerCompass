# ✅ Release Readiness Checklist

## Security
- [ ] Exposed credentials rotated and history exposure assessed.
- [ ] Secrets injected by secret manager, absent from source and logs.
- [ ] Upload validation, size limits, and output escaping verified.
- [ ] Network timeouts and error paths tested.

## Data and privacy
- [ ] Dataset provenance, license, consent, and redistribution rights recorded.
- [ ] Notebook examples reviewed for personal information.
- [ ] Processing, third-party transfers, retention, and deletion explained accurately.
- [ ] Privacy and security review signed off.

## Model
- [ ] Train/test split occurs before fitting preprocessing.
- [ ] Label encoder is packaged with estimator/vectorizer.
- [ ] Per-class metrics and confusion analysis published.
- [ ] Robustness, fairness, and limitations reviewed.
- [ ] Not used for employment or other consequential decisions.

## Engineering
- [ ] Supported Python version and artifacts documented.
- [ ] Unit and integration tests pass.
- [ ] Docs and changelog updated.
- [ ] Accessibility review performed.
- [ ] Rollback and disable procedure tested.

A checked list is not legal certification or proof of production suitability.

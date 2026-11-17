# 🏛️ Project Governance

## Purpose and boundaries
This file describes how Career Compass is reviewed and maintained. Career Compass is an experimental résumé-text classification and job-discovery prototype. It is not approved for hiring, applicant screening, candidate ranking, selection, rejection, or any other consequential employment decision.

## Maintainer
The project is maintained by Brajesh Kumar through [@brajesh31](https://github.com/Brajesh31). The maintainer reviews changes, manages repository settings, and decides when releases are ready. No response-time or support-level guarantee is made.

## Decision principles
1. Resolve critical security and data-rights risks before expanding functionality.
2. Require evidence for claims about accuracy, fairness, security, privacy, accessibility, and compliance.
3. Use synthetic data in tests, issues, examples, and screenshots.
4. Keep model builds reproducible and document provenance.
5. State uncertainty and known limitations clearly.
6. Prefer accessible, privacy-preserving designs.

## Change process
- Small fixes may be proposed in a focused pull request.
- Changes to data, labels, preprocessing, model artifacts, OAuth, uploads, external services, or deployment should start with an issue or written proposal.
- Architectural changes should include an ADR in [docs/decisions](docs/decisions/README.md).
- Changes to personal-data processing require a privacy review.
- Model changes require an evaluation report and updated model card.
- Security vulnerabilities must be reported privately through [SECURITY.md](SECURITY.md).

## Merge and release criteria
A contribution should explain user impact, scope, risks, validation, documentation updates, and unresolved work. A green workflow does not validate the model or establish the right to process résumé data. Releases require maintainer review of [the release checklist](docs/templates/release-readiness-checklist.md).

## Disagreements
Discuss technical disagreements respectfully in issues and pull requests. Sensitive security, privacy, or conduct matters should use the channels documented in [SECURITY.md](SECURITY.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## Amendments
Update this document when ownership, decision authority, review practices, or release rules materially change.

# 🚀 Release Process

## Release principles

No release should be described as production-ready while critical credential exposure, data rights, or unsafe résumé-processing risks remain unresolved.

## Preparation

1. Review [known issues](known-issues.md) and release readiness checklist.
2. Confirm secrets are rotated and absent from current source and logs.
3. Confirm data provenance and redistribution rights.
4. Verify label mapping, preprocessing, and artifact compatibility.
5. Run syntax, unit, integration, security, and model evaluation checks.
6. Update README, model card, data documentation, and changelog.
7. Verify no personal data or secrets enter the release.

## Versioning

Use semantic versioning only after the project has a stable public compatibility contract. Until then, label releases as experimental and describe the exact commit and artifact provenance.

## Post-release

Review deployment health, provider usage, error rates, and privacy/security reports. Keep rollback and service-disable instructions available.

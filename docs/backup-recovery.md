# 💾 Backup and Recovery

## Current scope
The project has no application database or documented user-account store. Git is the source-control record for source and documentation. Dataset and model files have independent provenance, privacy, and integrity concerns.

## Preserve
- Git history and reviewed release tags.
- Source code and project documentation.
- Approved datasets or references to approved external data sources.
- Model build manifests and verified checksums.
- Deployment templates without secret values.

Do not create backups of real user résumés merely because a backup mechanism exists.

## Recovery sequence
1. Restore source from a verified commit.
2. Rebuild artifacts from documented, rights-cleared data where possible.
3. Verify artifact checksums and runtime compatibility.
4. Rotate credentials suspected of exposure.
5. Recheck OAuth callback and provider configuration.
6. Run CI, unit tests, and a synthetic smoke test.
7. Re-enable uploads only after security and privacy review.

Automated backup infrastructure, RPO, and RTO targets are not currently implemented or claimed.

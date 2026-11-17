# 🔑 Secret Rotation Runbook

## Why this runbook exists
The current application source has contained a hard-coded third-party job-search API credential. Treat that credential as exposed. Do not reproduce it in tickets, commits, documentation, or terminal output.

## Immediate actions
1. Sign in to the provider's account using the approved owner account.
2. Revoke the exposed credential and issue a replacement.
3. Review provider access history, quota usage, and billing for unexpected activity.
4. Update the application to read the replacement from a secret manager or supported environment configuration.
5. Verify the code no longer contains a literal credential.
6. Check current files, workflow configuration, logs, and deployment settings for accidental copies.
7. Redeploy with the new secret and verify the integration using a controlled test query.
8. Record the incident and the rotation date without recording the credential itself.

## Git history
Removing a string from the latest version does not remove earlier commits, forks, cached clones, or copied logs. Rotation makes the exposed value invalid. Consider history rewriting only after coordinating with collaborators and understanding the disruption. Do not force-push as a substitute for credential revocation.

## Verification checklist
- [ ] Old credential revoked.
- [ ] Provider activity and billing reviewed.
- [ ] Replacement stored outside source control.
- [ ] Application reads secret configuration rather than a literal.
- [ ] Tests use mocks and do not require the live credential.
- [ ] Git history and public exposure assessed.
- [ ] Deployment verified.
- [ ] Incident record completed.

## Do not
- Paste the key into `.env.example`.
- Include it in issue templates, PR screenshots, CI logs, or documentation.
- Ask a contributor to send credentials in a public issue.

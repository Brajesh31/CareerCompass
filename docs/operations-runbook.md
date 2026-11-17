# 🚨 Operations Runbook

## Service scope

Career Compass is a prototype Streamlit app. Do not accept real or confidential résumé uploads until critical security, data-governance, privacy, and model issues are resolved.

## Disable use during an incident

1. Remove public access or stop the hosted app using the host's controls.
2. Disable or revoke the affected provider credential.
3. Preserve only necessary security evidence; avoid copying résumé content or tokens into logs.
4. Identify affected time range and systems.
5. Review provider usage, application logs, and repository history.
6. Notify the project maintainer and follow applicable incident obligations.

## Credential compromise

- Revoke/rotate at the provider first.
- Review billing, quota, and audit logs.
- Remove the secret from active code and configuration.
- Review Git history and forks/caches where feasible.
- Re-deploy only after verification.

## Data exposure

- Stop uploads and restrict access.
- Determine what data was exposed and where it may have been retained.
- Avoid downloading additional personal data during investigation.
- Follow an approved notification and deletion process. Do not improvise legal assurances.

## Recovery gate

Before reopening, confirm credential rotation, safe configuration, data rights, upload limits, correct category mapping, safe response rendering, request timeout behavior, and a reviewed privacy notice. Record validation evidence.

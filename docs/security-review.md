# 🛡️ Security Review

## Scope

This review covers the current Streamlit entry point, upload handling, OAuth gate, serialized model artifacts, external job provider, static page, and repository data.

## Findings register

| Severity | Finding | Evidence / action |
|---|---|---|
| Critical | Provider credential embedded in source | Revoke/rotate immediately; review history; move secret to approved secret manager |
| High | Untrusted pickle deserialization risk | Load only verified artifacts; define artifact provenance and integrity |
| High | External job fields inserted into HTML | Render as escaped text; validate schema and URLs |
| High | Network request has no explicit timeout | Add connect/read timeout, bounded retries, status and schema checks |
| High | Personal résumé examples may be tracked | Establish rights/consent; remove or replace unauthorized data |
| High | Upload content and size not validated | Enforce size, MIME/signature and parser limits |
| Medium | OAuth callback hard-coded | Use environment configuration and exact registered redirect URI |
| Medium | NLTK downloads at app startup | Pin resources and make startup deterministic/offline-friendly |
| Medium | No documented security tests | Add mocked integration and malicious-input tests |

## Immediate response for exposed credentials

1. Revoke or rotate the provider credential with the provider.
2. Review provider usage, quota, billing, and access logs.
3. Do not paste the replacement key into source, issues, screenshots, or commits.
4. Change code to read the replacement from a secret manager.
5. Search the repository and Git history for copies.
6. If history rewrite is necessary, coordinate it carefully and invalidate any leaked credential first.

A commit that deletes a secret does not make the old credential safe.

## Threat model

| Asset | Threat | Mitigation target |
|---|---|---|
| Provider API key | Repository exposure and misuse | Rotation, secret storage, least privilege |
| OAuth credentials/tokens | Accidental disclosure | Secret storage, short-lived session handling, no logging |
| Uploaded résumé | Confidentiality breach | Data minimization, TLS, access/retention controls |
| Pickle artifacts | Malicious deserialization | Trusted provenance, integrity checks, safer format review |
| Provider job fields | Script/markup injection | Escaped rendering and URL validation |
| Application availability | Slow or abusive uploads/API calls | Size limits, timeouts, rate limits |
| Dataset | Unauthorized redistribution | Provenance and license review |

## Verification checklist

- [ ] Exposed credentials rotated and historical exposure assessed.
- [ ] No secrets in current files, workflow logs, or issue content.
- [ ] Upload byte and size limits enforced.
- [ ] Real file format verified, not extension alone.
- [ ] Provider request uses timeout and bounded retry policy.
- [ ] External text rendered without unsafe HTML.
- [ ] Model artifacts verified and trusted.
- [ ] Synthetic malicious-input tests added.
- [ ] Data access, retention, deletion, and incident procedures documented.

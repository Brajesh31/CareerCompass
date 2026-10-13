# Security Policy

## Supported code

Security reports are considered for the current `main` branch. The repository
does not publish versioned releases or a formal support schedule. The app
processes uploaded résumé content, loads Python pickle artifacts, uses Google
OAuth configuration, and calls an external job-search service.

## Report privately

Do not publish vulnerabilities, API keys, OAuth credentials, résumé samples,
or sensitive deployment details in a public issue or pull request. If GitHub
private vulnerability reporting is enabled for this repository, submit a
report at:

<https://github.com/Brajesh31/CareerCompass/security/advisories/new>

If that channel is unavailable, contact the maintainer, Brajesh Kumar
([@brajesh31](https://github.com/brajesh31)), through GitHub and request a
private reporting channel before sending technical details. Include the
affected commit, impact, and a minimal reproduction using synthetic data.
Remove personal information, credentials, and private paths from logs.

The maintainer will acknowledge and assess reports as reasonably soon as
possible, coordinate a fix and disclosure when practical, and credit reporters
if requested. No fixed response or remediation deadline is promised.

## Known security and privacy concerns

These are repository observations, not a complete security audit:

- A third-party job-search API credential is embedded in the application
  source. Treat it as compromised and revoke or rotate it with the provider.
  Moving or deleting it in a new commit does not remove it from earlier Git
  history. Do not repeat the value in a report or documentation.
- Uploaded résumé text is handled by the app's Python server. Job-search
  requests are made to an external provider. The repository does not define a
  complete retention, deletion, or privacy-control system; do not upload real
  or confidential résumés until the complete deployment data flow has been
  reviewed.
- The app deserializes `clf.pkl` and `tfidf.pkl` using `pickle`. Python pickle
  files can execute code during loading; only load artifacts from a trusted
  source.
- Job-position text returned by the external service is inserted into HTML
  with unsafe HTML rendering. Treat that content as untrusted and escape or
  render it as plain text before production use.
- OAuth client values must remain private. The redirect URI is hard-coded in
  the application, and the repository does not document a production identity
  or access-control review.
- The pinned dependencies are old and should be reviewed for security updates
  before a deployment is exposed to the public internet.

## Deployment hygiene

- Revoke exposed provider credentials and issue replacements before enabling
  external integrations.
- Store secrets in the hosting platform's secret manager. Do not commit `.env`,
  `.streamlit/secrets.toml`, OAuth files, or copied credentials.
- Keep model artifacts from trusted, reviewed sources and document their
  provenance.
- Limit access to the app and logs according to the deployment's privacy and
  security requirements.
- Keep dependencies and the host runtime updated through reviewed changes.

The app is a prototype and is not a security or privacy certification. For
project data flow, see [docs/database.md](docs/database.md); for deployment,
see [docs/deployment.md](docs/deployment.md).

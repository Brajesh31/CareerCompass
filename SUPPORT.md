# Support

Career Compass is an experimental Streamlit project maintained on a best-effort
basis. It has no paid support, service-level agreement, or guaranteed response
time.

## Get help using the project

1. Read the [README](README.md) and relevant guides in [`docs/`](docs/).
2. Search existing issues at
   <https://github.com/Brajesh31/CareerCompass/issues>.
3. If the problem is not already reported, open an issue with a clear summary,
   steps to reproduce, expected and observed behavior, operating system,
   Python/dependency versions, and sanitized error messages.

Do not attach real résumés, personal information, OAuth tokens, API keys, or
private deployment logs. Use synthetic text when describing a model or upload
problem. The app's output is experimental and support cannot certify its
predictions for career, hiring, or employment decisions.

## Suggest a change

Open an issue before proposing new data sources, model behavior, file formats,
OAuth flows, or external integrations. Include the user need, source and license
of data, data flow, security/privacy impact, and validation plan. See
[CONTRIBUTING.md](CONTRIBUTING.md).

## Report a security issue

Do not use a public issue for vulnerabilities, credentials, or sensitive
deployment details. Follow the private reporting process in
[SECURITY.md](SECURITY.md). Rotate any credentials that may have been exposed.

## Report data or privacy concerns

If you believe a repository file contains personal information or data that
should not be redistributed, contact the maintainer privately through GitHub.
Do not repost the material in an issue. Provide the path and a concise
description without copying personal details into the report.

## Project scope

The repository contains a résumé-category classifier and job-search integration
prototype. Its data provenance, consent basis, model evaluation, and retention
behavior have not been established sufficiently for use with real résumés.
Review [docs/database.md](docs/database.md) before deploying or sharing data.

## Diagnostic checklist

For an installation or startup issue, include the command used, current directory, Python version, operating system, and whether the failure occurs during dependency installation or app startup.

Before sharing a traceback, remove OAuth tokens, API keys, usernames, local directory names, and any résumé text. Include the exception type and relevant sanitized frames instead of a full private log.

For a package issue, include the failing package name and pinned version from requirements.txt. Do not attach a full environment export if it contains private paths or tokens.

For an upload issue, describe the file extension, approximate size, and encoding using a synthetic sample. Do not send a real résumé as a reproduction attachment.

For an OAuth issue, report whether the configured redirect matches the callback registered with Google. Never include the client secret, authorization code, or token.

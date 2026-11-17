# 🔒 Privacy and Data-Flow Notes

## What the code currently does

- Displays consent language before Google OAuth authorization.
- Accepts uploaded files through Streamlit.
- Reads uploaded bytes and decodes them as text.
- Uses cleaned text for local model inference.
- Sends the predicted category, a geographic identifier, page value, and provider credential to the job-search endpoint.
- Does not explicitly write the résumé or prediction to a project-owned database.

## What is not established

The repository does not establish hosting-provider log retention, temporary upload lifecycle, backup retention, user-access controls, account deletion workflows, data subject request handling, or a reviewed legal privacy notice. Do not make promises about those topics based only on the current UI copy.

## Third-party transfers

Google OAuth receives the authentication flow data required by the configured scopes. The job-search provider receives the query parameters required for a category-based jobs request. Review each provider's terms and privacy documentation before enabling the integration for real users.

## Privacy-safe development

1. Use fictional résumé content.
2. Redact screenshots and logs.
3. Never share OAuth tokens or provider keys in issues.
4. Avoid storing request/response bodies containing personal data.
5. Review retention at the hosting and API provider layers.
6. Provide a real contact and deletion channel only after an operational process exists.

## User-facing transparency requirements

Before production, explain file types actually supported, processing location, data sent to each provider, purpose, retention, deletion, contact process, and limitations of automated classification. Consent text alone does not provide the underlying controls.

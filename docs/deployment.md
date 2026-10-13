# Deployment

This repository has no deployment manifest or hosting configuration. The app
can be started with Streamlit, but it is not ready for a public deployment that
accepts real résumés. The exposed job-search credential, undocumented data
rights, incomplete privacy design, model-label mismatch, and unsafe external
HTML rendering should be addressed first.

## Required before publishing

1. Revoke or rotate the third-party job-search API credential with its
   provider. It is present in source and Git history; changing the latest file
   does not invalidate or erase it.
2. Change the application to read replacement credentials from a supported
   platform secret store. The current app reads OAuth values with `os.getenv`
   and does not read the job key from configuration. Streamlit Community Cloud
   secrets are made available through Streamlit's secrets mechanism; the app
   must be updated to use that mechanism or another supported integration.
3. Establish data provenance, consent, and licensing for the repository's
   résumé dataset, notebook example, and model artifacts.
4. Define the upload privacy notice, data flow, retention, deletion, access
   controls, and incident handling. Do not accept real résumés until these are
   reviewed.
5. Correct the category mapping, HTML rendering, PDF handling, dependency
   compatibility, and model evaluation before presenting predictions as
   useful recommendations.

These are pre-deployment blockers, not optional hosting hardening.

## Streamlit Community Cloud

The app entrypoint is `app.py` at the repository root. The repository has a
`requirements.txt` with pinned packages, but it does not declare a Python
version. Streamlit documents the Community Cloud deployment flow in its
[deployment guide](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy)
and explains that the repository is run from its root in its
[file-organization guide](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/file-organization).

After the pre-deployment blockers above are addressed:

1. Push the reviewed branch to GitHub.
2. Create a Community Cloud app and select the repository, branch, and
   `app.py` entrypoint.
3. Choose a Python version compatible with the pinned packages and the
   serialized scikit-learn artifacts. The repository currently has no declared
   Python version, so verify compatibility in a separate clean environment
   before deployment.
4. Configure secrets through the platform's secret settings only after the app
   has been updated to read them securely. Streamlit's
   [secrets guide](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management)
   describes the platform mechanism; do not paste a secret into Git or a
   public issue.
5. Review build logs, OAuth behavior, provider errors, access permissions, and
   the public page before sharing the URL.

The current dependency snapshot pins Streamlit 1.32.2 and many other packages.
It may not be compatible with the host's default Python version. Streamlit
recommends declaring dependencies and pinning the version when reproducibility
matters; see its [dependency documentation](https://docs.streamlit.io/deploy/concepts/dependencies).
Do not upgrade the model dependencies without checking compatibility with the
pickled artifacts.

## Runtime and network requirements

The app downloads NLTK resources during script execution and calls Google OAuth,
an external image host, and the job-search provider. The host needs outbound
network access for those operations. The job request currently has no explicit
timeout. Failures can affect startup or leave the user without job results.

Streamlit runs Python on the host and sends widget/upload data from the browser
to that server. A hosted app therefore processes résumé content remotely. See
Streamlit's [client-server architecture documentation](https://docs.streamlit.io/develop/concepts/architecture/architecture)
and this project's [data-handling guide](database.md).

## Other hosting platforms

Use a host that supports a persistent Python process, the repository's
dependencies, model artifacts, outbound HTTPS, and the selected OAuth callback
flow. Start the app using `streamlit run app.py` and follow that provider's
instructions for interface/port binding, TLS, access controls, logging,
monitoring, and secrets. The application currently hard-codes the OAuth
redirect URI to the published Streamlit URL, so other hosts require an
application and OAuth-client configuration change.

## After deployment

- Confirm the intended audience and whether the app is public.
- Do not let users infer that the model makes a hiring recommendation or
  assesses a person's ability.
- Monitor provider usage, error logs, resource use, and credential rotation.
- Provide a way to disable uploads and external job lookup during an incident.
- Keep the privacy notice aligned with actual hosting and provider behavior.

For local setup, see [installation.md](installation.md). For operational
security findings, see [SECURITY.md](../SECURITY.md).

## Additional deployment review points

Community Cloud detects dependency-file changes and may rebuild the environment. Review build logs after requirements changes and keep a record of the Python and package versions used for the published app.

The current app reads OAuth values with os.getenv. Store values through the host's supported mechanism only after the code has been updated to retrieve them; a secret stored in a dashboard but not read by the app does not configure authentication.

Community Cloud lets the deployer choose a Python version during app creation. This repository has no version declaration, so select only after checking the pinned packages and model pickle compatibility.

The deployment source includes the tracked CSV, notebook, and model artifacts. A hosted build receives repository content; review whether each file belongs in a deployable source tree and whether any data should be removed from public distribution.

A public GitHub repository already exposes tracked files independently of the running app. Deployment access controls do not make the dataset, notebook example, or source credential private.

The Google OAuth button is a gate in the UI, but the app does not document identity-based permissions or a durable user model. Do not treat the presence of a sign-in screen as a complete privacy or authorization design.

The job-search provider call runs after a successful prediction. Until a rotated key is read securely and provider calls are bounded, do not expose the app to public traffic.

The page also fetches a background image from an external image host. Decide whether that third-party request is acceptable for the intended audience and document it in the privacy notice.

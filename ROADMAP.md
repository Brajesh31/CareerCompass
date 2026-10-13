# Roadmap

This roadmap is a proposed order of work, not a delivery commitment. No target
dates are set. The application should remain a demonstration until the data,
security, and model issues below have been addressed and reviewed.

## Current baseline

- Streamlit page with Google OAuth, résumé upload, category prediction, and
  external job lookup.
- 25-category classifier and TF-IDF artifacts, with notebook training code.
- Static HTML landing page and a résumé dataset of undocumented provenance.
- No documented automated test suite, CI workflow, or production privacy
  design.

## Proposed priorities

### 1. Contain credential and data exposure

- Revoke or rotate the third-party API key currently present in source and
  Git history.
- Move replacement credentials into a supported secret-management flow and
  remove all hard-coded secret values from application code.
- Establish provenance, consent, licensing, and redistribution rights for the
  dataset, notebook example, model artifacts, and external assets.
- Remove personal résumé details from examples and notebook outputs where
  publication rights cannot be demonstrated.

### 2. Correct the current behavior

- Use one saved label encoder or a verified class mapping so every model
  prediction ID resolves to the intended category.
- Either parse PDF files with an explicit, reviewed parser or stop advertising
  PDF support; add size/type validation and clear error handling.
- Escape external job-listing fields and render untrusted provider content
  safely.
- Add request timeouts and handle provider failures without blocking the app.
- Review Google OAuth redirect configuration and access-control behavior for
  each deployment.

### 3. Establish valid model evaluation

- Split data before fitting any preprocessing so test data remains isolated.
- Use a reproducible, appropriate split and report per-class metrics,
  uncertainty, and failure cases.
- Review class balance, source representativeness, data leakage, and possible
  bias across relevant groups where lawful and ethically appropriate.
- Obtain independent review before making any claim about real-world
  performance. Do not use the model for hiring or other consequential
  decisions without a separate, rigorous assessment and governance process.

### 4. Design privacy and product boundaries

- Define what uploaded content is processed, where it is sent, whether it is
  logged, who can access it, and how long it remains available.
- Provide an accurate privacy notice and clear user choice before upload.
- Decide whether the product is a personal exploration aid or a recruiting
  tool; do not imply suitability for employment screening.
- Document data deletion, incident response, and third-party provider terms.

### 5. Improve maintainability

- Add focused automated checks for text cleaning, label mapping, upload
  validation, and error handling using synthetic data only.
- Make model training and artifacts reproducible and separate UI, model,
  configuration, and external-service code.
- Review and minimize the pinned dependency list, declare a supported Python
  version, and add CI for safe static checks.
- Repair or remove the incomplete static registration page and unused legacy
  session-state helper.

## Proposing changes

Open an issue with the user need, data sources and licenses, privacy/security
impact, model-evaluation plan, and maintenance cost. See
[CONTRIBUTING.md](CONTRIBUTING.md). Progress on this roadmap does not by itself
establish that the classifier is suitable for employment decisions.

### Credential remediation detail

Credential rotation includes revoking the exposed provider key, checking its usage, changing the app to use a secret manager, and coordinating any history cleanup separately. Removing the visible string alone is insufficient.

### Dataset decision

Before further model work, record the résumé dataset source, rights, consent basis, and permitted uses. If these cannot be demonstrated, remove the dataset and sample content from future distribution and use synthetic or properly licensed material.

### Label integrity

Persist the encoder with the classifier and derive output labels from the trained class list. Add a consistency check that covers every class ID, including the current mismatch at IDs 10–13.

### File-format decision

Choose either a tested PDF parser with file-size and content validation or a text-only interface. Do not advertise a file type merely because the uploader accepts its extension.

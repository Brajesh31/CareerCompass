# Changelog

This file records notable repository changes. The project has no documented
tagged releases or versioning policy, so entries are grouped under
`Unreleased` until maintainers establish releases.

## Unreleased

### Documentation and repository guidance

- Added project overview, contribution, conduct, security, support, roadmap,
  citation, and technical documentation.
- Added an MIT license for original project code while documenting that the
  provenance and reuse rights of the résumé dataset, notebook example, model
  artifacts, and third-party assets remain to be established.
- Expanded repository hygiene files and documented the current OAuth
  environment-variable names.

### Existing application baseline recorded

- The Streamlit app classifies uploaded résumé text into one of 25 categories
  and queries an external job-search service.
- The upload control accepts `.txt` and `.pdf`, but the current implementation
  decodes uploaded bytes as plain text rather than parsing PDF structure.
- The notebook fits TF-IDF before its train/test split, and the app's manual
  category mapping does not align with the notebook's encoded labels for IDs
  10–13.
- The source contains a hard-coded third-party API credential. It must be
  revoked or rotated with the provider; a later source change alone would not
  remove it from Git history.
- The dataset and a notebook sample contain résumé text, but provenance,
  consent, and redistribution terms are not documented.

These notes describe the repository baseline reviewed for this documentation.
They do not certify model accuracy, privacy, security, or data rights.

### Additional review findings

- The active page is app.py; session_state.py is a legacy helper that the page does not import.

- OAuth uses Google authorization and token endpoints, requests openid email profile, and stores the returned value in Streamlit session state.

- The app calls NLTK download functions during script execution even though the current prediction path does not use those resources.

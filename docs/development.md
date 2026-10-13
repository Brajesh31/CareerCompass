# Development

Career Compass is a small Streamlit prototype, but its upload, OAuth, model,
and external-service paths process sensitive material. Follow
[CONTRIBUTING.md](../CONTRIBUTING.md) and [SECURITY.md](../SECURITY.md) before
changing those paths.

## Repository map

```text
app.py                              Streamlit UI and runtime orchestration
clf.pkl, tfidf.pkl                 Pickled model and vectorizer loaded by app
UpdatedResumeDataSet.csv           Labeled résumé text used by the notebook
Resume Screening with Python.ipynb Data exploration and model training
index.html, style.css              Static landing page and styles
session_state.py                   Legacy helper unused by current app.py
requirements.txt                   Pinned Python package list
docs/                              Project and technical guides
```

The notebook includes an example résumé with personal details in its source.
Do not re-run or republish it until the sample and any stored outputs have been
reviewed and cleared for publication. The dataset's source, consent basis, and
license are not documented.

## Set up a worktree

1. Fork the project or create a focused branch from `main`.
2. Follow [installation.md](installation.md) to create `.venv` and install the
   pinned dependencies.
3. Use only synthetic text. Do not use real or confidential résumés during
   development.
4. Before running `app.py`, be aware that it downloads NLTK resources and calls
   an external service after a file upload. The job API credential is currently
   hard-coded in source; avoid triggering that integration until it has been
   rotated and moved to secure configuration.

Do not commit `.env`, OAuth JSON files, `.streamlit/secrets.toml`, credentials,
uploaded documents, private logs, virtual environments, model artifacts of
unknown origin, or editor state. The repository `.gitignore` excludes common
local secrets and caches, but review every diff before committing.

## Model and preprocessing changes

- Establish data provenance and redistribution rights before using a dataset.
- Split examples into training and evaluation sets before fitting TF-IDF or
  other preprocessing. The current notebook fits TF-IDF before the split.
- Fit and persist the class encoder together with the classifier so displayed
  names always come from the trained model's class order. The app's manual map
  is currently inconsistent for four IDs.
- Report per-class results and limitations; a high overall score would not
  establish suitability for employment decisions.
- Keep examples synthetic and remove personal details from notebook outputs.
- Only load trusted pickle files. Do not accept model files from untrusted
  contributors or users.

## External integrations and uploads

Keep credentials out of code and Git, use provider-approved secret storage, and
add timeouts and explicit error handling to network requests. Validate upload
size and actual file format. Treat provider response fields as untrusted: do
not put raw external strings into HTML. Document what data leaves the app and
for what purpose whenever integrations change.

## Validation

The repository currently has no documented automated test suite or CI
workflow. Startup requires OAuth configuration, NLTK downloads, model artifacts,
and network access, so do not claim that a change is validated just because a
page renders. For code changes, add tests using synthetic fixtures and mocked
OAuth/job-search responses, then describe the checks performed. Model changes
also require a reproducible data split, per-class metrics, and limitations.

Before opening a pull request, inspect the diff for personal data and secrets,
check that category names match the training labels, and update the affected
guides. Do not include live service credentials or real résumé screenshots in
review materials.

## Pull requests

Open a pull request against `main`. Summarize the user need, implementation,
data sources and licenses, privacy and security impact, validation performed,
and remaining limitations. For interface changes, add screenshots only when
they contain no personal or confidential information.

## Focused review checks

For changes to clean_resume, use fictional edge-case strings that include URLs, hashtags, punctuation, non-ASCII text, and the substrings RT and cc inside ordinary words.

For a label-map change, compare all 25 integer classes against the encoder classes and include assertions for every mapping instead of checking only one prediction.

For training changes, split first, fit vectorization only on training text, and retain the exact split and seed so reported metrics can be reproduced.

For OAuth changes, mock authorization/token responses in development checks; do not rely on a shared production client or store tokens in fixtures.

For job-provider changes, mock empty, malformed, non-success, slow, and successful responses. Do not call the real endpoint with the exposed credential.

For HTML changes, include synthetic provider fields containing angle brackets and script-like strings, then verify they are shown as text rather than interpreted markup.

For file handling changes, test extension/content mismatches, empty input, invalid encodings, and oversized inputs using synthetic fixtures.

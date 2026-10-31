# Career Compass

Career Compass is a Streamlit prototype that classifies uploaded résumé text
into one of 25 job categories and requests matching job listings from an
external job-search service. The repository also contains a Jupyter notebook,
a CSV of résumé examples, and serialized scikit-learn artifacts.

This is an experimental demonstration, not a hiring or career-advice system.
Its training data, licensing, evaluation, bias characteristics, and category
mapping have not been established to a standard suitable for employment
decisions. Do not use its predictions to screen, rank, reject, or select job
applicants, or as the basis for another consequential decision.

## What the app currently does

1. Presents a Google OAuth sign-in button using credentials supplied through
   `GOOGLE_CLIENT_ID` and `GOOGLE_CLIENT_SECRET` environment variables.
2. Accepts a file named `.txt` or `.pdf` through Streamlit's upload control.
3. Decodes the uploaded bytes as UTF-8, falling back to Latin-1, and cleans
   portions of the resulting text.
4. Transforms the text with `tfidf.pkl` and predicts a category with
   `clf.pkl`.
5. Requests job listings for the predicted category from ScrapingDog's
   LinkedIn jobs endpoint and displays the returned results.

The current upload path does not extract text from PDF structure. A PDF may be
accepted by the control but produce meaningless text and an unreliable
prediction. Text files are the only format that this implementation actually
decodes as text.

The app maps model output IDs to category names in `app.py`. The notebook
creates labels with scikit-learn's `LabelEncoder`, while the app maintains a
separate hand-written mapping. The mapping for IDs 10–13 does not match the
notebook's alphabetically encoded categories; outputs for those IDs can be
misnamed. The model has not been independently validated for real-world use.

## Important security and privacy notes

- A third-party job-search API credential is embedded in the existing
  application source. Treat it as exposed: revoke or rotate it with the
  provider before using the integration, then move the replacement into a
  secret manager and update the code to read it from configuration. Do not
  copy credentials into issues, documentation, or new commits. Removing a
  value from the latest source does not remove it from Git history.
- The repository contains résumé text in a dataset and notebook example. These
  files may include personal information, and the repository does not document
  their provenance, consent, or redistribution rights. Review them before
  redistributing or deploying the project.
- The application loads `clf.pkl` and `tfidf.pkl` with Python `pickle`. Only
  load model artifacts from a source you trust; unpickling untrusted files can
  execute code.
- Uploaded résumé text is processed by the Streamlit server. Matching job
  lookups are sent to an external service. Do not submit real or confidential
  résumés until the data flow, retention, access controls, and privacy terms
  have been reviewed.
- The consent text shown by the app is not a substitute for verified privacy
  safeguards or a reviewed privacy notice.

See [SECURITY.md](SECURITY.md) for private vulnerability reporting and
[docs/database.md](docs/database.md) for the current data-flow notes.

## Requirements

- Python 3 (the repository does not declare a supported minimum version).
- The pinned Python packages in `requirements.txt`.
- Google OAuth client credentials for sign-in. The redirect URI is currently
  hard-coded in `app.py` to the published Streamlit app URL, so local OAuth
  requires an appropriate code and provider configuration change.
- A replacement ScrapingDog API key after the exposed credential has been
  revoked or rotated and the source has been changed to use secret
  configuration.

The application calls `nltk.download()` for tokenizer and stop-word data at
startup, so the runtime needs network access to download those resources. The
current prediction code does not otherwise use those downloads.

## Run locally

Clone the repository, enter its root directory, and create an isolated
environment.

Windows PowerShell:

```powershell
git clone https://github.com/Brajesh31/CareerCompass.git
cd CareerCompass
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
streamlit run app.py
```

macOS or Linux:

```sh
git clone https://github.com/Brajesh31/CareerCompass.git
cd CareerCompass
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
streamlit run app.py
```

For local OAuth configuration, copy `.env.example` to `.env` and fill in the
Google OAuth values. Keep `.env` private and untracked. The currently hard-coded
third-party API credential must be rotated and moved to secret configuration
before the job lookup integration is used again. See [installation.md](docs/installation.md)
and [deployment.md](docs/deployment.md) for more context. Stop Streamlit with
`Ctrl+C` in the terminal.

## Repository contents

| Path | Purpose |
| --- | --- |
| `app.py` | Streamlit login, upload, prediction, and external job lookup flow |
| `clf.pkl`, `tfidf.pkl` | Serialized classifier and TF-IDF vectorizer loaded by the app |
| `UpdatedResumeDataSet.csv` | Résumé text and category labels used in the notebook |
| `Resume Screening with Python.ipynb` | Exploratory data work, training, and artifact creation |
| `index.html`, `style.css` | Static sign-up/landing page; its form and popup scripts are incomplete |
| `session_state.py` | Legacy helper not imported by the current `app.py` |
| `requirements.txt` | Pinned Python packages; includes more packages than the app imports directly |
| `docs/` | Installation, architecture, deployment, data, API, and contributor guides |

The static page redirects toward the Streamlit app; it does not provide a
separate working registration backend. The current Streamlit app has no
application database or public REST API.

## Model and data limitations

The notebook loads 962 labeled résumé examples across 25 categories, cleans
text, fits a TF-IDF vectorizer, and compares several classifiers. It fits the
vectorizer before splitting the data into training and test sets, which leaks
information from the test text into feature construction. The source does not
provide a documented data source/license, a reproducible evaluation report,
calibration, fairness analysis, or independent validation. The bundled model
should therefore be treated as a demonstration artifact only.

Read [architecture.md](docs/architecture.md) for the implementation flow,
[api.md](docs/api.md) for the absence of a public application API, and
[troubleshooting.md](docs/troubleshooting.md) if the app does not start.

## Contributing, support, and license

Read [CONTRIBUTING.md](CONTRIBUTING.md) before proposing a change. For project
help, see [SUPPORT.md](SUPPORT.md); for conduct expectations, see
[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). The project source is offered under
the MIT License in [LICENSE](LICENSE), subject to rights in third-party data,
models, libraries, and assets being reviewed separately. See [CITATION.cff](CITATION.cff)
for citation metadata and [CHANGELOG.md](CHANGELOG.md) for recorded changes.

## Documentation map

- [Architecture](docs/architecture.md): components, inference flow, and limitations.

- [Installation](docs/installation.md): Python environment, OAuth setup, and local run instructions.

- [Development](docs/development.md): safe change, data, and model practices.

- [Deployment](docs/deployment.md): pre-deployment blockers and hosting guidance.

- [API](docs/api.md): current OAuth and external job-search integrations.

- [Database and data handling](docs/database.md): what the app processes and what it does not persist.

- [Troubleshooting](docs/troubleshooting.md): common startup, upload, model, and provider failures.

- [FAQ](docs/faq.md): common questions about categories, privacy, and model limits.

For contribution and operations guidance, see [CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md), [SUPPORT.md](SUPPORT.md), and [ROADMAP.md](ROADMAP.md).

Last updated: 2026-10-31 01:11 UTC

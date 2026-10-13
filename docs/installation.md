# Installation

This guide describes local setup for the current repository. The project pins
packages in `requirements.txt`, but it does not declare a supported Python
version. The requirements file is a large environment snapshot with packages
that the active app does not import directly, so installation may require a
compatible Python runtime.

## Before you start

The application source contains a hard-coded third-party API credential that
must be rotated with the provider and moved into secret configuration before
using the job-search flow. The app invokes that integration after a résumé is
uploaded. Do not upload real résumés or use this prototype on a public/shared
host until the credential and data-handling concerns in [SECURITY.md](../SECURITY.md)
have been addressed.

## 1. Clone the repository

```sh
git clone https://github.com/Brajesh31/CareerCompass.git
cd CareerCompass
```

Run commands from the repository root. The current app loads `clf.pkl` and
`tfidf.pkl` using relative paths from its working directory.

## 2. Create an isolated Python environment

On Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```sh
python3 -m venv .venv
source .venv/bin/activate
```

If PowerShell activation is blocked, use the virtual environment's Python
directly instead of changing machine-wide execution policy:

```powershell
.venv\Scripts\python.exe -m pip install --upgrade pip
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m streamlit run app.py
```

## 3. Install the pinned packages

With the environment activated, run:

```sh
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

The package versions are pinned, but the Python version is not. If installation
fails, review the first package build or compatibility error and use a Python
version compatible with the pinned dependencies. Do not replace the full
requirements file with guessed versions; review and validate a smaller
application-specific dependency set as a separate change.

## 4. Configure Google OAuth for local work

Copy `.env.example` to `.env` and set `GOOGLE_CLIENT_ID` and
`GOOGLE_CLIENT_SECRET` to OAuth credentials you control. The root `.gitignore`
excludes `.env`; never commit real credentials.

The OAuth redirect URI is hard-coded in `app.py` to the published Streamlit
site. Local OAuth will not work until the code and Google OAuth client are
configured with a local redirect URI. Do not paste client secrets into issues
or logs.

The job-search API credential is not read from an environment variable in the
current code. `.env.example` intentionally does not pretend that setting an
unused variable will secure the integration. Rotate the exposed credential,
change the app to read its replacement from a secret manager, and only then
configure the new value.

## 5. Start Streamlit

From the repository root, run:

```sh
streamlit run app.py
```

Streamlit prints the local URL, typically `http://localhost:8501`. The app
attempts to download NLTK tokenizer and stop-word data during script execution,
so the first run needs network access. Stop the server with `Ctrl+C`.

The upload widget accepts `.txt` and `.pdf`, but current code decodes the raw
file bytes as text and does not parse PDF structure. Use only synthetic test
text; do not use private résumés. Consult [troubleshooting.md](troubleshooting.md)
for common setup issues.

## Related guides

- [Development workflow](development.md)
- [Deployment considerations](deployment.md)
- [Architecture and data flow](architecture.md)
- [Data handling](database.md)

## Additional setup notes

The repository .gitignore excludes .venv and venv directories. Keep the environment outside tracked source and verify that .env remains untracked after local OAuth setup.

The pinned requirements file is a broad snapshot rather than a minimal list for app.py. Installing it may take longer than installing only the runtime packages because it includes notebook and unrelated framework dependencies.

Streamlit is pinned to version 1.32.2 in the current requirements file. This is the version expected by the existing environment snapshot, not a guarantee that it is compatible with every current Python release.

The repository does not pin Python or provide a lockfile. Record the interpreter version used for any reproduction and choose one compatible with the pinned package set.

Installing requirements needs access to the configured Python package index. Starting the app also attempts to download NLTK resources, so a fully offline first run is not supported by the current script.

Google OAuth requires valid credentials and a callback registered for the configured redirect. The supplied environment template contains placeholders only and cannot change the redirect URI.

Streamlit Community Cloud secrets use the Streamlit secret mechanism, while the current OAuth code reads os.getenv. Update that integration before expecting hosted secrets to populate the current environment lookup.

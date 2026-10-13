# Troubleshooting

## `streamlit` or a Python package is missing

Activate the project's virtual environment and install the pinned requirements
from the repository root:

```sh
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

If installation reports an incompatible package or Python version, note the
first failing package and review the pinned requirements. The repository does
not declare a supported Python version. Avoid upgrading one model dependency
without checking whether the serialized artifacts remain compatible.

## `clf.pkl` or `tfidf.pkl` cannot be found

The app opens these files using relative paths from the current working
directory. Start Streamlit from the repository root, where both files are
stored. Do not replace them with pickle files from an untrusted source.

## A pickle or scikit-learn compatibility error appears

Python pickle and scikit-learn artifacts can depend on the versions used to
create them. Use the pinned packages in `requirements.txt` and only trusted
artifacts. Do not try arbitrary pickle files to see if they work; unpickling an
untrusted file can execute code. The project does not document a reproducible
model build artifact or supported version matrix.

## OAuth fails or returns to the wrong page

- Confirm that `GOOGLE_CLIENT_ID` and `GOOGLE_CLIENT_SECRET` are present in the
  local environment and belong to an OAuth client you control.
- The redirect URI is hard-coded in `app.py` to the published Streamlit URL.
  It must match the OAuth provider's allowed callback and the actual deployment.
- In Streamlit Community Cloud, configuring a value in the Secrets field does
  not by itself make current `os.getenv()` calls read it; update the app to use
  a supported secrets mechanism.
- Never paste client credentials or OAuth tokens into an issue or log.

## The app fails while starting or rerunning

The source calls `nltk.download()` for tokenizer and stop-word resources.
Check the terminal traceback and host outbound network access. The prediction
path currently does not otherwise use those downloaded resources. If startup
fails before the page renders, provide a sanitized traceback and Python/package
versions in a GitHub issue.

## A `.pdf` upload gives a strange prediction

The upload control accepts `.pdf`, but the current code reads its raw bytes and
decodes them as UTF-8 or Latin-1. It does not extract PDF text. Use only a
synthetic plain-text `.txt` sample for any safe local review; do not upload real
résumés.

## The predicted category looks wrong

The app cleans text with broad regular expressions and uses a model trained on
an undocumented résumé dataset. The notebook's TF-IDF fit occurs before the
train/test split, and the app's manual category map is inconsistent for class
IDs 10–13. These issues can affect the result. Predictions are experimental
and must not be used for hiring or other consequential decisions.

## No job listings appear

The current integration converts non-200 provider responses to an empty list,
so the UI may not distinguish a provider outage, invalid credential, rate
limit, or genuinely empty result. The HTTP request has no explicit timeout and
the API credential is exposed in source history. Do not repeatedly call the
provider with that credential; rotate it and update the code to use secure
configuration first. Missing or malformed response fields may also cause an
exception.

## Report an unresolved problem

Open an issue with reproduction steps, expected and observed behavior, Python
and package versions, and sanitized logs. Use synthetic input. Do not attach
résumés, personal data, tokens, client secrets, or the exposed API-key value.
For vulnerabilities, use the private process in [SECURITY.md](../SECURITY.md).
## Additional diagnostic cases

### App fails to find local files

Run Streamlit from the repository root so relative paths to the model files
resolve as expected. Confirm that clf.pkl and tfidf.pkl are present in the
deployment checkout and that the published branch includes the intended
artifacts. Do not replace them with files from an untrusted source.
### Model cannot be deserialized

Pickle compatibility depends on the Python and library versions used to create
the artifact. Compare the runtime with the environment used by the notebook,
then regenerate and review the artifacts through a trusted process if needed.
Never attempt to fix this by loading an unknown pickle from a user or issue.
### Category label does not match the model

The app maintains its own integer-to-category mapping, while the notebook
derives label order with LabelEncoder. Those mappings differ for class IDs
10–13. Compare the saved classifier labels, notebook encoding, and app mapping
before relying on any category output.
### PDF upload produces unreadable output

The current implementation decodes uploaded bytes as text; it does not extract
PDF content. The file chooser accepting a PDF extension does not mean PDF
parsing is supported. Use a synthetic plain-text file for local checks and do
not submit a real résumé.
### OAuth redirect fails

Check that the configured provider allows the exact deployed redirect URL and
that the OAuth component and app use matching client credentials. The active
code reads OAuth values from environment variables. Do not paste client
secrets, authorization codes, or callback URLs containing tokens into issues.
### Hosted OAuth settings are missing

The deployment guide may store credentials using the hosting platform's
secrets interface, but the current code reads process environment variables.
Verify that the deployment exposes the expected variables to the process.
Never commit a secrets file as a workaround.
### Search returns no results after prediction

An empty list can mean no matching jobs or a provider error because the current
code treats non-success status responses as no results. Check sanitized
deployment logs and provider status, then review credentials and quotas. Rotate
the exposed credential before making further calls.

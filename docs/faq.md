# Frequently asked questions

## What does Career Compass do?

It accepts résumé-like text, predicts one of 25 job-category labels with a
TF-IDF/scikit-learn model, and requests job listings for that predicted label
from an external service. It is an experimental demonstration, not a validated
career advisor or hiring system.

## Can I use its prediction to screen or rank applicants?

No. The model's data provenance, evaluation, class mapping, and fairness
characteristics are not established for employment decisions. The notebook
also fits TF-IDF before splitting training and test rows, which leaks test text
into preprocessing. Do not use its output to accept, reject, rank, or select
applicants.

## Does the upload control support PDF files?

The control lists `.pdf` as an accepted extension, but the application reads
the bytes and decodes them as text. It does not extract text from PDF structure,
so a PDF upload may result in meaningless input and an unreliable prediction.
The current implementation only actually decodes text files as text.

## Which categories can it predict?

The model has 25 categories, including software roles, data roles, engineering,
HR, sales, operations, and other fields. The app's hand-written ID map does not
match the notebook's `LabelEncoder` order for IDs 10–13. Some outputs may
therefore be given the wrong category name. See [architecture.md](architecture.md).

## Does it search jobs using my complete résumé?

The current job-search request uses the predicted category, a fixed geographic
identifier, a page value, and an API credential. It does not include the
résumé text in that request. The résumé itself is still uploaded to and
processed on the Streamlit server. Hosting and provider logs and retention are
outside the code in this repository; do not upload confidential résumés.

## Does the app save my résumé or prediction?

The application code does not explicitly save uploads or results to a project
database or file. Streamlit handles the upload and session on the server, and
the hosting environment may have its own temporary storage, logs, or backups.
There is no complete retention or deletion policy in the repository. See
[database.md](database.md).

## Why does sign-in fail locally?

The app requires `GOOGLE_CLIENT_ID` and `GOOGLE_CLIENT_SECRET`. Its redirect URI
is hard-coded to the published Streamlit app address, so local development
requires updating both the application and the OAuth client's callback
settings. Keep the client secret private.

## Why are no job listings shown?

The provider request may fail, be rate-limited, return a non-200 status, or
return unexpected JSON. The current code displays all non-200 responses as an
empty result and has no explicit timeout. The API credential is hard-coded in
source and must be rotated before using that integration.

## Is the job-search credential safe to use?

No. A third-party API credential is present in the source and Git history.
Treat it as exposed, revoke or rotate it with the provider, and update the app
to read a replacement from secure configuration. A later commit does not erase
earlier Git history.

## Is there a public API or database?

No project-owned REST or GraphQL API and no application database are
implemented. See [api.md](api.md) and [database.md](database.md).

## Can I redistribute the dataset, notebook, or model files?

The repository does not document the source, consent, or license for the
résumé dataset, the notebook example, or the model artifacts. The repository's
MIT license does not establish reuse rights for third-party material. Obtain
and document permission before redistributing them.

## How do I run or contribute?

See [installation.md](installation.md) for local setup,
[development.md](development.md) for safe changes, and
[CONTRIBUTING.md](../CONTRIBUTING.md) for project guidelines. Use synthetic
text only.

## What training data is included?

The tracked CSV contains 962 résumé text rows assigned to 25 categories. Category sizes vary, and the repository does not document where the content came from, how consent was obtained, or whether redistribution is permitted. Do not assume that inclusion in Git makes the data free to reuse.

## Which model is stored in clf.pkl?

The notebook iterates through several classifiers and saves the final loop value as clf.pkl; from the notebook's declared order, that final classifier is the one-vs-rest SVM. The notebook does not save a label encoder alongside it, which contributes to the app's separate, mismatched manual label map.

## Has the model's accuracy been established?

The notebook calculates evaluation scores, but its TF-IDF vectorizer is fitted to all résumé rows before the train/test split. This leaks information from the eventual test partition into preprocessing. The repository does not provide a clean, independently reproducible evaluation suitable for real-world use.

## What does text cleaning change?

The cleaner removes URLs, every occurrence of the strings RT or cc, hashtags, mentions, punctuation, non-ASCII characters, and repeated whitespace. These broad substitutions may remove meaningful words, names, abbreviations, or technical details and can change predictions.

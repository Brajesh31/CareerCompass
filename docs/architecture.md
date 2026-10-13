# Architecture

## Scope

Career Compass is a single-file Streamlit application with supporting model
artifacts and a training notebook. The active interface and orchestration live
in repository-root `app.py`. `session_state.py` is a legacy helper that the
active app does not import. The app has no project-owned REST API, database, or
background worker.

## Runtime flow

```text
Browser
  └─ Google OAuth authorization ──> Google authorization/token endpoints
  └─ uploaded file ───────────────> Streamlit Python server
                                      ├─ decode bytes as UTF-8 or Latin-1
                                      ├─ clean text with regular expressions
                                      ├─ tfidf.pkl transforms the text
                                      ├─ clf.pkl predicts an integer class
                                      ├─ app.py maps class ID to a label
                                      └─ predicted label + fixed region ──> ScrapingDog
Browser <────────────────────────── predicted label and displayed job fields
```

The résumé bytes are processed by the Python server. The job lookup sends the
predicted category, a fixed geographic identifier, a page value, and an API
credential to the external provider; the current code does not pass the résumé
text to that job-search request. The provider and hosting platform have their
own processing and logging behavior, outside this repository.

## Components

- **Streamlit UI and orchestration (`app.py`):** displays the consent text,
  starts Google OAuth, accepts an upload, predicts a category, and renders job
  results.
- **Configuration:** `load_dotenv()` loads local environment variables.
  `GOOGLE_CLIENT_ID` and `GOOGLE_CLIENT_SECRET` are read with `os.getenv`. The
  redirect URI is hard-coded to the published app URL. A third-party job-search
  API credential is also hard-coded in source and should be treated as exposed.
- **Text preprocessing:** `clean_resume()` removes URLs, every `RT` or `cc`
  substring, hashtags, mentions, punctuation, non-ASCII characters, and repeated
  whitespace. These lossy substitutions can remove meaningful résumé content.
- **Model inference:** `tfidf.pkl` vectorizes the cleaned text and `clf.pkl`
  predicts an integer label. Both are loaded with Python `pickle` from the
  current working directory. Only trusted artifacts should be loaded.
- **External job search:** `fetch_linkedin_jobs()` calls ScrapingDog's
  LinkedIn-jobs endpoint. It has no explicit timeout; non-200 responses become
  an empty result, while malformed response content or missing fields can
  raise errors.
- **Static landing page:** `index.html` and `style.css` provide a separate
  landing page that redirects to the Streamlit deployment. Its popup handlers
  refer to elements that are not present in the HTML, and the form has no
  registration backend.
- **Training materials:** `Resume Screening with Python.ipynb` cleans the CSV,
  label-encodes categories, fits TF-IDF, compares classifiers, and writes model
  pickle files. The notebook fits TF-IDF before splitting data, leaking test
  text into preprocessing.

## Model and category mapping

The CSV has 962 résumé rows across 25 labels. The notebook uses
`LabelEncoder`, which orders class names, but the app duplicates the ID-to-name
mapping manually. IDs 10–13 do not match the notebook's alphabetical label
order: the notebook's IDs are Electrical Engineering, ETL Developer, Hadoop,
and HR, while the application maps those IDs to different names. Predictions
for these classes can therefore be mislabeled. The model and data have no
documented provenance or independent validation.

## State and persistence

The app keeps the OAuth result in Streamlit's per-session state. It does not
explicitly write uploaded résumés or prediction results to an application
database or file. Streamlit processes uploads on the server, and platform
temporary storage, logs, backups, and retention are controlled by the hosting
environment. NLTK downloads its tokenizer and stop-word resources at runtime;
the current prediction path does not otherwise use those resources.

## Design constraints

The application combines configuration, UI, preprocessing, model loading, and
network calls in one script. It lacks explicit upload-size validation, real PDF
text extraction, safe external HTML rendering, API timeouts, a privacy/retention
design, model metrics, and automated tests. The UI accepts `.pdf` but treats
the bytes as text. The job-position field is inserted into HTML with unsafe
rendering. These gaps make the current project a prototype only, not a safe
automated employment decision system.

### Startup and script reruns

Imports, dotenv loading, model deserialization, and NLTK download calls occur at module level in app.py. Streamlit executes the script again when the user interacts, so startup work is coupled to the page rerun path.

### File path assumptions

The model files are opened relative to the process working directory, not through the script_directory variable. Local and hosted launch commands must run with the repository root as the working directory.

### OAuth state

The returned OAuth result is assigned to st.session_state under the token key, then the page reruns. The application does not define a separate durable account record or explicit sign-out button.

### Input decoding

The uploader reads the entire file into memory. UTF-8 decoding is attempted first and Latin-1 is used after a UnicodeDecodeError; there is no parser branch for PDF structure or upload-size limit.

### Preprocessing boundaries

clean_resume applies substitutions before TF-IDF. It removes the literal strings RT and cc without word-boundary checks, which can alter unrelated words as well as common résumé markers.

### Prediction and presentation

The vectorizer and classifier run in the Streamlit process. The integer prediction is translated by a static dictionary; the label encoder is not loaded at inference time, so the dictionary can drift from model classes.

### Job request shape

The external request sends a category field and fixed location/page parameters. It is a role search, not a semantic similarity comparison between the uploaded document and each listing.

### Rendering boundary

Company, location, date, and link fields use Streamlit text rendering; job_position is inserted into raw HTML. The distinct rendering path means that field requires explicit escaping.

### State duration

The app does not call a database or explicitly save an upload, but Streamlit session state and upload handling exist while the session is active. Host logs and temporary storage require separate deployment review.

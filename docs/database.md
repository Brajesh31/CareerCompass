# Database and data handling

## Database status

The active application does not connect to a database. It has no schema,
migrations, application backup process, or persistent user-account store. It
does not explicitly save uploaded résumés or predictions to a project file or
database.

## Data flow in the current app

1. **Google sign-in:** the app requests `openid email profile` scopes and stores
   the OAuth result in `st.session_state`. The app uses the presence of a
   `token` value to decide whether to show the upload page. It does not define a
   separate account database or a documented token-retention policy.
2. **Résumé upload:** the browser sends the uploaded file to the Streamlit
   server. `app.py` reads the bytes, decodes them as text, cleans the text, and
   sends the cleaned content through the local vectorizer and classifier in
   that Python process. The code does not explicitly write the upload or
   prediction to a durable application store.
3. **Job lookup:** the app sends the predicted category, a fixed geographic
   identifier, a page number, and a hard-coded API credential to the external
   job-search provider. It does not send the résumé text in that request. The
   external provider's retention and logging practices are outside this repo.
4. **Runtime downloads:** `nltk.download()` obtains tokenizer and stop-word
   resources for the host environment. The current prediction path does not
   otherwise use those resources.

Streamlit applications use a browser client and Python server, and maintain
per-session state while a browser tab is connected. See Streamlit's official
[client-server architecture](https://docs.streamlit.io/develop/concepts/architecture/architecture)
and [session-state guide](https://docs.streamlit.io/develop/concepts/architecture/session-state).
For a hosted instance, résumé bytes are processed on the host, not solely on
the visitor's device.

## Repository data is a separate concern

`UpdatedResumeDataSet.csv` contains 962 résumé-text rows, and the training
notebook includes a sample résumé with personal details in its source. These
files are already part of the Git repository. Their source, consent basis,
license, and redistribution rights are not documented here. Do not assume the
MIT license for original code establishes rights to redistribute this data or
model artifacts. Review the dataset and notebook outputs before reuse or
redistribution.

## Privacy and retention limits

The in-app consent text describes collection, security, sharing, access, and
deletion rights, but this codebase does not implement an application database,
deletion workflow, or complete retention controls. Hosting logs, temporary
upload handling, platform backups, and OAuth/provider logs depend on the
deployment and external services. The repository cannot promise that data is
never retained by those systems.

Do not upload real, confidential, or personally identifying résumés until the
full deployment data flow, provider terms, access controls, logging, retention,
deletion, and privacy notice have been independently reviewed. Use synthetic
text for examples and development.

## Secrets

`GOOGLE_CLIENT_ID` and `GOOGLE_CLIENT_SECRET` are read from the environment.
The job-search API credential is currently hard-coded in source and has been
exposed. Revoke or rotate it and update the app to use a platform secret
manager. The `.env.example` contains placeholders for OAuth only; do not add a
real value to it. Never commit `.env`, OAuth credential JSON, tokens, or
`.streamlit/secrets.toml`.

## If persistence is proposed

Before adding storage, define the user need, minimum data collected, purpose,
access controls, encryption, retention, deletion, backups, incident response,
and applicable privacy/legal review. Update the architecture and user notice
before enabling collection. Keep model prediction possible without storing
identifying data where practical.
## Data governance checkpoints

### Keep the no-database description precise

The application does not define a database connection, schema, migration, or
repository-managed persistence layer. This does not establish that every
deployment component is storage-free: identity providers, the hosting platform,
and external job-search services have separate handling and retention rules.

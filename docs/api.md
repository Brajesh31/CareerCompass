# API

## Application API status

The repository does not expose a supported project REST, GraphQL, or command
line API. The user interface is a Streamlit page in `app.py`. Streamlit's own
browser/server protocol is an implementation detail and is not an API contract
for external clients.

## Google OAuth integration

When there is no `token` entry in `st.session_state`, the app renders a Google
authorization button through `streamlit-oauth`. The current source configures:

- Authorization endpoint: `https://accounts.google.com/o/oauth2/auth`
- Token endpoint: `https://oauth2.googleapis.com/token`
- Requested scope: `openid email profile`
- Client ID and client secret: `GOOGLE_CLIENT_ID` and
  `GOOGLE_CLIENT_SECRET` environment variables
- Redirect URI: hard-coded to the published Streamlit app URL

This is a sign-in integration, not an application API. The redirect cannot be
changed with the current `.env.example`. Review the OAuth client settings and
callback behavior before running on another host. Do not publish OAuth secrets
or tokens.

## External job-search API

After a prediction, `fetch_linkedin_jobs()` sends an HTTP GET request to
ScrapingDog's LinkedIn jobs endpoint:

```text
https://api.scrapingdog.com/linkedinjobs/
```

The current query includes an API key, the predicted category as `field`, a
fixed `geoid`, and `page=1`. The key is hard-coded in source and has been
exposed; it must be revoked or rotated. The current code does not read a
replacement from an environment variable or platform secret store.

The response handler accepts either a JSON list or an object with a `jobs`
array. The UI expects each job to include `job_id`, `job_position`,
`company_name`, `job_location`, `job_posting_date`, and `job_link`. This is an
internal integration assumption, not a stable public contract supplied by this
repository.

Current error behavior is limited: a non-200 status becomes an empty list, and
the UI reports that no jobs were found. There is no explicit request timeout,
retry policy, response schema validation, or clear distinction between an
empty search and provider failure. The job position is inserted into HTML with
unsafe rendering; external response content must be escaped before rendering.

The job-search request uses the predicted category rather than the uploaded
résumé text. Do not rely on this as a privacy guarantee until the actual
provider request and deployment logs have been reviewed.

## Inputs and prediction result

The UI accepts files ending in `.txt` or `.pdf`. The current implementation
reads bytes and decodes them as UTF-8 or Latin-1; it does not parse PDF text.
It cleans the resulting string, applies the pickled TF-IDF vectorizer, predicts
an integer class, and maps that ID to a category label. There is no separately
designed programmatic interface or supported endpoint for this prediction.

The app's manually maintained ID-to-label mapping is inconsistent with the
notebook's `LabelEncoder` order for class IDs 10–13. Category output can be
wrong for those labels. See [architecture.md](architecture.md).

## If a public API is proposed

Open an issue and define a versioned request/response schema, input limits,
file parsing, authentication, authorization, rate limits, error behavior,
logging/retention, and credential management. Use synthetic data in examples.
Any API returning model output must clearly state that the classifier is
unvalidated and not suitable for hiring or other consequential decisions.
## Additional implementation guidance

### Streamlit interaction is the current interface

The supported user interaction is the Streamlit page and its session state. The
repository does not register application-owned REST routes or define a stable
JSON contract. Streamlit's own internal transport endpoints are framework
details and should not be treated as public project APIs.
### Authentication flow boundaries

The app requests OpenID Connect identity scopes through the OAuth component.
Authentication establishes a sign-in flow; it does not by itself define
application roles, hiring permissions, or access to a separately managed
account record. Do not describe this as authorization for employment use.
### Configuration source

The active Python code reads OAuth values from process environment variables.
Streamlit Community Cloud also supports its own secrets configuration, but the
repository does not currently read those values through st.secrets. Confirm
the deployment's configuration bridge before expecting hosted sign-in to work.
Keep all actual credentials outside Git.
### Job-search request scope

After prediction, the app sends the predicted category and configured search
parameters to the external job-search provider. The current request does not
intentionally send the uploaded résumé text. Recheck this behavior whenever
the request construction changes, and review provider terms and deployment
logs before making privacy commitments.
### Validate provider responses

Treat the remote response as untrusted input. Check status, content type, JSON
parsing, top-level shape, and the type and presence of every displayed field.
Handle an empty result separately from network, authentication, quota, and
schema failures so users can understand what happened without exposing
secrets or stack traces.
### Bound remote calls

Give external requests a finite timeout and a deliberate retry policy. Retries
should be limited to transient failures and should not amplify rate limits.
Avoid logging full request URLs when they contain credentials; redact tokens
and query parameters in diagnostics.
### Render external text safely

Escape or render provider-supplied job titles and other text using safe text
components. Do not interpolate remote values into HTML with unsafe rendering.
Validate links before making them clickable, and use only expected URL schemes
such as HTTPS.

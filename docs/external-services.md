# 🌐 External Services and Integration Boundaries

## Services observed in source

| Service | Purpose | Current implementation |
|---|---|---|
| Google OAuth | Sign-in gate | Google authorization/token endpoints through streamlit-oauth |
| ScrapingDog | External job search | Requests GET to LinkedIn jobs endpoint |
| Unsplash | Background image | Remote image URL embedded in inline styling |
| NLTK download host | Tokenizer/stopword assets | Download calls during app execution |

## Data sent
The job-search request currently includes a predicted category, fixed geographic identifier, page value, and provider credential. The code does not pass the full résumé in that request. Uploaded résumé content is still processed by the Streamlit server, and hosting logs/retention are not fully documented.

OAuth requests `openid email profile` scopes. The callback URL is hard-coded in the current application.

## Integration requirements
- Rotate exposed credentials and use platform secret storage.
- Add finite connect/read timeouts and bounded retry behavior.
- Validate status codes, JSON shape, required fields, and data types.
- Treat provider text and URLs as untrusted.
- Render external data as escaped text, not raw HTML.
- Avoid logging tokens, secrets, résumé text, or raw payloads.
- Document provider terms, privacy policy, rates, costs, and retention.
- Provide a configuration switch to disable optional external lookups.

## Failure semantics
The current helper maps non-200 responses to an empty list and has no explicit timeout. A safer implementation should distinguish timeout, authentication failure, rate limit, malformed response, provider outage, and a successful empty result.

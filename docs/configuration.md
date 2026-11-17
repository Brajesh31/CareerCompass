# ⚙️ Configuration Reference

## Existing variables

| Variable | Read by current app | Description |
|---|---|---|
| `GOOGLE_CLIENT_ID` | Yes | Google OAuth client ID |
| `GOOGLE_CLIENT_SECRET` | Yes | Google OAuth client secret |

## Fixed values currently in source

The OAuth redirect URI, job provider endpoint, provider credential, location identifier, and page value are currently hard-coded. The provider credential must be treated as exposed and rotated. Do not copy the credential into this guide or into `.env.example`.

## Local configuration

1. Copy `.env.example` to `.env`.
2. Supply credentials for an OAuth client you control.
3. Ensure `.env` remains ignored by Git.
4. Configure a redirect URI that matches the OAuth client. The current code uses the hosted app URI, so local flow needs a code change first.

## Proposed configuration design

A future implementation should validate configuration at startup and fail with a clear message when required settings are absent. Secret values should be injected by the hosting platform's secret manager. This is a recommendation; the current app does not implement the full configuration contract.

## Operational safeguards

Never print secrets, include them in exception text, serialize them into diagnostics, or expose them in query strings. Rotate exposed credentials and keep an inventory of their owner, scope, and expiration.

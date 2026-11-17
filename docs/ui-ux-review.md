# 🎨 UI and UX Review

## Current interface
The active Streamlit page includes a remote background image, inline consent/privacy copy, Google OAuth gate, résumé upload control, predicted category heading, and provider-generated job cards. `index.html` and `style.css` are a separate static landing-page attempt, not a working registration backend.

## Known experience gaps
- PDF is listed as an accepted extension, but the application does not parse PDF structure.
- Consent text describes practices and user rights not fully established by the code.
- Category output has no calibrated uncertainty.
- Job search uses a fixed geographic identifier.
- The app does not compare job requirements with a résumé.
- Provider failure and a successful empty response look alike.
- Provider-controlled text is interpolated into HTML.
- The remote background requires contrast and accessibility testing.

## Review checklist
- [ ] Prototype limitations are visible before upload.
- [ ] Accepted formats match actual parser behavior.
- [ ] Processing and third-party transfers are explained before file selection.
- [ ] Errors distinguish invalid input, inference failure, provider failure, and empty results.
- [ ] Provider output is escaped and URLs are validated.
- [ ] Keyboard, screen reader, zoom, narrow viewport, and focus states are usable.
- [ ] Text contrast remains sufficient over the background.
- [ ] No wording implies objective career fit or applicant ranking.

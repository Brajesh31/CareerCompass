# 🧭 Feature Scope and Product Boundaries

## Current capabilities visible in source

| Feature | Current state |
|---|---|
| Google sign-in gate | Present, callback is hard-coded |
| Text upload | Present for .txt bytes |
| PDF upload | Extension accepted, PDF parsing absent |
| Resume text cleanup | Regex helper in app.py |
| Category prediction | TF-IDF + serialized classifier |
| Category display | Hard-coded mapping, known ID mismatch |
| Job discovery | External provider query by category and fixed geography |
| Personalized ranking | Not implemented |
| Per-listing skill matching | Not implemented |
| User profile database | Not implemented |
| Saved résumé history | Not implemented |
| Export / deletion controls | Not implemented as a complete product flow |
| Admin console | Not implemented |
| Public REST API | Not implemented |

## Product language
Do not call the product a validated career advisor, candidate screening system, or personalized matching engine. Prefer “résumé text category demo” and “job listings retrieved for a predicted category.”

## Feature acceptance
Before adding a feature, define the user problem, data collected, privacy impact, accessibility behavior, failure states, test plan, and documentation update. Avoid features that encourage high-impact employment decisions.

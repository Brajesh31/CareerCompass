# 🧯 Known Issues Register

| ID | Priority | Issue | Evidence | Next action |
|---|---|---|---|---|
| CC-01 | Critical | Job provider credential embedded in app source | Literal key passed in `fetch_linkedin_jobs` call | Revoke/rotate; remove from code and history exposure |
| CC-02 | High | Class mapping mismatch | Notebook encoder order differs from app mapping for IDs 10–13 | Persist encoder and test all labels |
| CC-03 | High | TF-IDF leakage | Notebook fits vectorizer before split | Use Pipeline and split before fitting |
| CC-04 | High | PDF bytes treated as text | Upload path decodes raw bytes; no PDF parser | Restrict to TXT or implement hardened PDF extraction |
| CC-05 | High | External fields inserted as HTML | Provider job fields interpolated in `st.markdown` with unsafe HTML | Render escaped text |
| CC-06 | High | Provider request lacks timeout | `requests.get` has no timeout parameter | Add timeouts and bounded retries |
| CC-07 | High | Data provenance unclear | CSV and notebook lack clear rights/consent record | Establish provenance or remove/replace |
| CC-08 | Medium | Broad regex text cleaning | Removes RT/cc substrings and non-ASCII text | Define tested normalization behavior |
| CC-09 | Medium | OAuth callback fixed to hosted URL | Constant in app | Move redirect URI into validated config |
| CC-10 | Medium | NLTK downloads at app startup | `nltk.download` calls at import time | Package resources or provision explicitly |
| CC-11 | Medium | No declared Python compatibility | No runtime version declaration | Test and declare supported Python versions |
| CC-12 | Medium | Pickle artifacts lack manifest | No artifact build metadata/checksum file | Add trusted build manifest |

This register reflects a source review, not a formal penetration test or legal assessment. Close an item only with a linked change and evidence.

# 🧑‍💻 Current User Journey

```mermaid
journey
    title Current Career Compass demonstration
    section Entry
      Open Streamlit page: 4: Visitor
      Read consent text: 3: Visitor
      Continue with Google: 2: Visitor
    section Processing
      Upload TXT or PDF: 3: Visitor
      Decode bytes: 2: App
      Clean and vectorize: 3: App
      Predict category: 2: App
    section Discovery
      Request listings by category: 2: App
      View provider results: 3: Visitor
```

## Known journey gaps
The PDF extension is accepted without PDF parsing. No confidence estimate or correction flow is shown. Job search uses a fixed geography identifier and does not compare each listing with résumé content. Provider failures are not distinguished from empty results. Logout, token lifecycle, and deletion flows are incomplete.

## Future-state considerations
A safer design would explain processing before upload, validate file content/size, preview extracted text, make external lookup explicit, communicate uncertainty, distinguish provider errors, and provide an operational deletion/contact process. These are proposals, not implemented features.

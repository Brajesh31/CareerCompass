# ⚠️ Career Compass Disclaimer

Career Compass is an experimental educational software and machine-learning demonstration. It is provided for learning, prototyping, and controlled evaluation only.

## Not for employment decisions
Do not use this application or its outputs to screen, rank, accept, reject, shortlist, select, promote, compensate, or terminate applicants or employees. A category prediction is not a verified assessment of a person's skills, qualifications, potential, or suitability. Do not use the output as a proxy for a professional assessment.

## No guarantee of job recommendations
The application queries listings using a predicted category and fixed geography value. It does not validate each listing against an individual's skills or preferences. Listings may be incomplete, outdated, unavailable, or governed by external provider terms. No job availability or outcome is guaranteed.

## Data and privacy
Do not upload real, confidential, or identifying résumés. The app processes uploaded text on the Streamlit server and calls an external job-search service. Hosting-level logs and retention are not fully specified. Read [docs/privacy.md](docs/privacy.md) and [docs/data-retention.md](docs/data-retention.md).

## Security
The existing source has contained a hard-coded provider credential. Treat it as exposed and rotate it with the provider. Python pickle artifacts must only be loaded from trusted sources.

## No professional or legal advice
Repository documents are engineering notes, not legal advice, privacy certification, security certification, or a guarantee of regulatory compliance.

## License scope
The MIT license applies to original project code as stated in [LICENSE](LICENSE). It does not automatically grant rights to third-party datasets, notebook examples, model artifacts, or external assets.

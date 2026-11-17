# 🧹 Data Retention and Deletion

## Current code boundary
The app does not explicitly write uploaded résumé files or predictions into a project-owned database. It processes uploaded bytes in the Streamlit session and requests external jobs by category.

This does not prove that data is never persisted. Hosting logs, proxies, temporary storage, process memory, crash diagnostics, backups, and third-party services may have independent retention behavior not defined in this repository.

## Before accepting users
Document and verify:
- Data categories and purpose.
- Whether uploaded bytes or extracted text are written to disk.
- Session lifetime and temporary-file cleanup.
- Hosting, proxy, application, and provider log retention.
- Backup scope and expiration.
- Access rights and operational owners.
- User deletion request handling and evidence of completion.
- Incident notification and escalation procedures.

## Development rule
Use synthetic data only. Do not commit private examples or include personal information in issues, tests, notebooks, logs, or screenshots.

Do not promise deletion or confidentiality until the underlying process exists and has been tested. Use [privacy-impact-template.md](templates/privacy-impact-template.md) when adding retention or deletion functionality.

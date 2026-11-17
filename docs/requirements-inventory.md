# 📋 Requirements Inventory

## Packages imported by active app.py
The active script imports Streamlit, streamlit-oauth, streamlit-extras, NLTK, Requests, python-dotenv, and Python standard-library modules. The serialized artifacts also require compatible scikit-learn and numerical-library versions.

## Requirements snapshot
The existing `requirements.txt` contains a broad pinned environment snapshot, including notebook tooling and packages not directly imported by active app.py. Do not remove dependencies based only on a quick import scan. Review notebook usage and artifact compatibility first.

## Proposed cleanup
- Separate runtime, notebook, and test dependencies.
- Declare a tested Python version.
- Introduce a reproducible dependency lock.
- Record model artifact build versions.
- Scan dependency changes for security and license concerns.

This is a source-level inventory, not a complete SBOM or license audit.

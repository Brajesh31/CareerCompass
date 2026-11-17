# 🧪 Test Suite

The current suite uses synthetic inputs and isolated source parsing. It does not import `app.py`, load pickle artifacts, download NLTK resources, start Streamlit, or call external services.

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

Add focused tests for preprocessing, upload validation, label mapping, configuration, and mocked provider/OAuth adapters as those paths are refactored. See [testing strategy](../docs/testing.md).

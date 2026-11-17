# 📦 Dependency Management

## Current requirements
`requirements.txt` is a fully pinned environment snapshot and contains more packages than are imported directly by active `app.py`. It includes Streamlit, scikit-learn, NLTK, Requests, OAuth, notebook tooling, and unrelated frameworks. The repository does not declare a supported Python version.

## Update process
1. Explain why a dependency is needed.
2. Review maintenance activity, license, security advisories, and transitive dependencies.
3. Check compatibility with the selected Python runtime and serialized model artifacts.
4. Update pins or constraints with a clean-environment test.
5. Run unit tests and a synthetic startup/integration check where safe.
6. Update requirements inventory, README, and changelog.

## Development dependencies
`requirements-dev.txt` is separate and currently provides test tooling. Do not install it in production without a reason.

## Supply-chain rules
Avoid arbitrary package URLs, unverified wheels, and untrusted pickle files. Review dependency update pull requests before merging.

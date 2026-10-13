# Contributing

Thank you for considering a contribution to Career Compass. The repository is
an experimental résumé-category demonstration, not a validated hiring tool.
Contributions should improve correctness, privacy, security, accessibility,
reproducibility, or documentation without presenting the model as suitable for
employment decisions.

## Before starting

1. Read [README.md](README.md), [SECURITY.md](SECURITY.md), and the relevant
   guides in `docs/`.
2. Search existing issues for the same problem or proposal.
3. Open an issue before substantial changes to model behavior, data use, OAuth,
   external services, or deployment.
4. Never include real résumés, names, contact details, credentials, OAuth
   tokens, or private deployment configuration in an issue, commit, screenshot,
   test fixture, or pull request.

The project is maintained by Brajesh Kumar, GitHub account @brajesh31.

## Report a defect

Open a GitHub issue with a concise description, reproduction steps, expected
behavior, observed behavior, operating system, Python and dependency versions,
and sanitized error output. Use synthetic text to describe classification
problems. Do not attach a real résumé or personal information. Report a
suspected vulnerability through the private process in [SECURITY.md](SECURITY.md),
not a public issue.

## Data and model changes

Changes involving résumé data or model artifacts require particular care:

- Identify the dataset source, consent and collection basis, license, permitted
  uses, and redistribution terms before adding or republishing any data.
- Remove personal identifiers from examples and notebook outputs. Use
  synthetic fixtures for development and documentation.
- Document label definitions, class balance, preprocessing, training and test
  split strategy, dependency versions, and artifact provenance.
- Fit preprocessing only on training data and keep evaluation data isolated.
  The current notebook fits TF-IDF before the split, which leaks test-set text
  into feature construction; do not copy that procedure as a sound evaluation
  pattern.
- Derive category names from the same encoder used for training. Do not update
  the integer-to-label map by hand without checking every class against the
  training labels and saved model.
- Include suitable validation, limitations, and bias/fairness review before
  proposing any use that could affect a person's employment opportunities.
- Do not load or commit model artifacts from sources you do not trust; Python
  pickle deserialization can execute code.

Third-party job-search integrations must document their terms, rate limits,
data sent, error handling, timeouts, and secret-management approach. Never
hard-code an API token. Rotate credentials that have been committed or exposed.

## Prepare a change

1. Fork the repository or create a focused branch from `main`.
2. Keep the change small and describe the user impact.
3. Follow [installation.md](docs/installation.md) for the local environment.
4. Keep credentials in local untracked `.env` files or an appropriate platform
   secret manager; `.env.example` must contain placeholders only.
5. Update docs when behavior, data flow, model artifacts, dependencies,
   supported file formats, or deployment requirements change.
6. Do not include generated caches, virtual environments, private inputs, or
   editor state.

## Validation and review

The repository currently has no documented automated test suite or CI
workflow. The app uses external OAuth and job-search services, so contributions
should state what could be validated safely without real credentials or
personal data. For model changes, describe the dataset split, evaluation
method, class-level results, and limitations; do not report a single score as
proof of suitability for hiring.

Before opening a pull request, review the diff for secrets and personal data,
confirm category labels match the trained encoder, and update related
documentation. Do not run an evaluation on non-consented résumé data.

## Pull requests

Open a pull request against `main`. Include the reason for the change, the
implementation summary, data and dependency sources, privacy/security impact,
validation performed, and known limitations. Add screenshots only when useful
and ensure they contain no personal or confidential information.

## License and conduct

By submitting a contribution, you confirm that you have the right to submit it
and that its source and license are identified. Original project code is
offered under the MIT License in [LICENSE](LICENSE); the license status of the
résumé dataset, notebook example, trained model, and third-party assets has not
been established. Follow [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

### Training and evaluation detail

When revising training code, record the exact data version, class distribution, random seed, preprocessing, and model parameters. Keep the evaluation partition outside vocabulary fitting, threshold selection, and any other model decisions.

### Class labels

Treat the encoder and category names as one artifact. The current notebook's LabelEncoder and app.py's manual mapping disagree for IDs 10–13. A proposed fix should verify every label against the trained model rather than relying on the displayed category alone.

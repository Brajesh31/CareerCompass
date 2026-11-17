# 🧠 Model Card: Career Compass Classifier

> **Status: incomplete, experimental, not approved for employment decisions.**

## Model identity

| Field | Current evidence |
|---|---|
| Task | Multi-class classification of résumé-like text |
| Labels | 25 job-category labels |
| Feature extraction | scikit-learn TF-IDF transformer serialized as `tfidf.pkl` |
| Estimator | Serialized scikit-learn classifier in `clf.pkl`; notebook's final loop model appears to be one-vs-rest SVM |
| Training source | Notebook and tracked CSV |
| Training rows | Notebook loads 962 labeled examples |
| Evaluation | Notebook computes scores, but vectorization precedes the train/test split |
| Label mapping | App has a separate manual map; mapping is inconsistent for IDs 10–13 |
| Artifact provenance | No reproducible manifest or checksum record currently published |

## Intended use

Educational experimentation with text preprocessing, feature extraction, supervised classification, and Streamlit integration.

## Prohibited / unsupported use

- Hiring, screening, ranking, candidate selection, rejection, promotion, or compensation.
- Automated or human-assisted decisions about an identifiable person's employment.
- Claims that a predicted label represents ability, potential, suitability, or qualification.
- Use as a substitute for professional career counselling or verified job requirements.

## Data

The repository's CSV is described in the notebook as 962 résumé examples across 25 categories. The source, collection date, consent, representation, deduplication, personal-data handling, and redistribution license are not sufficiently documented. Do not infer that public Git access implies permission to reuse the content.

## Preprocessing

The application cleaner removes URLs, hashtags, mentions, punctuation, non-ASCII characters, repeated whitespace, and every occurrence matching the literal substrings `RT` and `cc`. This broad cleaning may remove meaningful words and identifiers. It must be tested against synthetic edge cases before change.

## Evaluation limitations

The notebook fits TF-IDF over all examples before splitting rows. This leaks information about test text into feature construction and invalidates a clean held-out evaluation interpretation. The repository does not publish a corrected reproducible split, per-class metrics, calibration, confidence intervals, subgroup performance, robustness tests, or independent validation.

## Fairness and impact

Résumé text can encode or proxy sensitive information. Category imbalance, language, formatting, career gaps, education access, and other variables can affect predictions. No fairness audit is provided. The model must not be used for consequential decisions.

## Known technical risks

1. App label IDs can be misnamed relative to the notebook encoder.
2. The vectorizer and classifier are separate pickle artifacts with no manifest.
3. Pickle loading is unsafe for untrusted files.
4. No model confidence or abstention policy is implemented.
5. Job retrieval is category-based, not a per-listing skills match.

## Required evidence before any broader claim

- Documented lawful data provenance and rights.
- Reproducible training pipeline with split before fitting preprocessing.
- Persisted label encoder and versioned pipeline artifact.
- Deduplication and leakage checks.
- Stratified per-class metrics and confusion matrix.
- Calibration and abstention analysis.
- Robustness testing across formatting and language variants.
- Independent fairness and impact review.
- Human oversight and a validated, narrow intended-use statement.

## Change history

Update this model card for every change to labels, data, preprocessing, estimator, evaluation, artifacts, or intended use. Use [model change template](templates/model-change-record-template.md).

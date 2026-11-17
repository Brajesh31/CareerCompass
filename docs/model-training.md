# 🏋️ Model Training and Artifact Lifecycle

## Current notebook behavior
`Resume Screening with Python.ipynb` loads the CSV, performs text cleaning and label encoding, constructs TF-IDF features, compares classifier candidates, and saves a vectorizer and classifier as pickle files.

The notebook fits TF-IDF before the train/test split. That leaks information from the eventual test partition into feature construction. Scores from that procedure must not be presented as unbiased held-out performance.

The notebook does not persist the label encoder beside the classifier. The app instead maintains a manual mapping that disagrees with notebook encoding for IDs 10–13.

## Current artifact contract

| Artifact | Runtime role | Missing metadata |
|---|---|---|
| `tfidf.pkl` | Converts cleaned text to feature vectors | Build commit, parameters, training data checksum |
| `clf.pkl` | Predicts numeric category ID | Artifact manifest and paired label encoder |
| Manual app mapping | Converts ID to display string | Provenance and full-class consistency test |

Pickle deserialization can execute code. Never load user-supplied or untrusted pickle artifacts.

## Recommended retraining sequence
1. Verify dataset rights and remove unauthorized personal information.
2. Inspect schema, label definitions, class balance, duplicates, and near-duplicates.
3. Split the data before fitting any vectorizer or preprocessing transformer.
4. Use a scikit-learn Pipeline so transformations are trained only on training folds.
5. Tune on training/validation data and preserve a final untouched test partition.
6. Save the estimator, vectorizer, label encoder, configuration, and versions as one versioned artifact bundle.
7. Evaluate per-class metrics, error patterns, robustness, calibration, and limitations.
8. Publish a model card and checksums before deploying an artifact.

## Reproducibility manifest
Record the dataset source, rights, checksum, split strategy and seed, preprocessing version, vectorizer parameters, estimator parameters, dependency versions, metrics, artifact checksums, build commit, and reviewer.

## Change control
A model artifact replacement changes behavior even when application code is unchanged. Require a documented evaluation and update [model-card.md](model-card.md) and [model-evaluation.md](model-evaluation.md).

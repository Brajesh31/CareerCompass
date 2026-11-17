# 🗃️ Dataset Card: UpdatedResumeDataSet.csv

> **Status: incomplete. Do not assume this dataset is consented, representative, or redistributable.**

## Identity and repository evidence

| Field | Evidence |
|---|---|
| File | `UpdatedResumeDataSet.csv` |
| Purpose | Notebook exploration and supervised résumé-category classification |
| Rows | 962 labeled examples loaded by the notebook |
| Labels | 25 job-category classes |
| Class sizes | Inspected repository notes report a range of 20 to 84 examples per category |
| Original source / owner | Not adequately documented |
| Retrieval / collection date | Not documented |
| Consent or lawful basis | Not documented |
| License / redistribution permission | Not documented |
| Personal information | Résumé text may contain identifying details |
| Version / checksum | No dataset manifest is maintained |

## Intended repository use
The notebook uses the data to demonstrate cleaning, label encoding, TF-IDF feature extraction, classifier experiments, and artifact serialization.

## Unsupported use
Do not use the dataset for hiring or employment decisions, infer sensitive traits, publish individual examples, or redistribute it until provenance, consent, and license terms have been confirmed.

## Known limitations
- Data origin, acquisition process, collection context, and permitted use are unknown.
- The sample count is modest for 25 classes and class sizes are imbalanced.
- Duplicates and near-duplicates are not documented as checked.
- Résumé content may contain personal or sensitive information.
- Representativeness across languages, geography, occupation, career stage, and formatting is not established.

## Required due diligence
Record owner, source URL, retrieval date, license, consent basis, collection purpose, schema, label definitions, preprocessing, exclusions, deduplication, retention, and redistribution rights. If rights cannot be established, remove the dataset from future distribution and replace it with synthetic or properly licensed material.

Use [data-source-review-template.md](templates/data-source-review-template.md) and [dataset-change-template.md](templates/dataset-change-template.md) for review.

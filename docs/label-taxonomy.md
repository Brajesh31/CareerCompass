# 🏷️ Current Label Taxonomy

## Important warning
This table transcribes the hand-written mapping in the current `app.py`. It is **not a verified canonical taxonomy**. The notebook's LabelEncoder uses its own ordering, and the application mapping is known to disagree for IDs 10–13. Do not use this list to infer the true class order or to repair predictions without verifying the saved encoder.

## Application mapping as currently written

| Predicted ID | Display label in app.py |
|---:|---|
| 0 | Advocate |
| 1 | Arts |
| 2 | Automation Testing |
| 3 | Blockchain |
| 4 | Business Analyst |
| 5 | Civil Engineer |
| 6 | Data Science |
| 7 | Database |
| 8 | DevOps Engineer |
| 9 | DotNet Developer |
| 10 | ETL Developer |
| 11 | Electrical Engineering |
| 12 | HR |
| 13 | Hadoop |
| 14 | Health and fitness |
| 15 | Java Developer |
| 16 | Mechanical Engineer |
| 17 | Network Security Engineer |
| 18 | Operations Manager |
| 19 | PMO |
| 20 | Python Developer |
| 21 | SAP Developer |
| 22 | Sales |
| 23 | Testing |
| 24 | Web Designing |

## Required correction design
Persist the LabelEncoder or the full estimator pipeline with the model artifact. Convert predicted class IDs through the persisted encoder. Remove the independent hard-coded mapping. Add a test that checks every class ID against the encoder's `classes_` property and fails if artifacts are mismatched.

## Change control
Any change to categories or labels requires data definition, class balance review, retraining, per-class evaluation, and a model-card update. Use [model-change-record-template.md](templates/model-change-record-template.md).

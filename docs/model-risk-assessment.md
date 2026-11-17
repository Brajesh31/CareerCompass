# ⚖️ Model Risk and Impact Assessment

## Summary
The model assigns résumé-like text to one of 25 occupational categories. Its training data rights, representativeness, evaluation quality, and fairness have not been established.

## Risk register

| Risk | Potential impact | Current evidence gap |
|---|---|---|
| Unclear data provenance | Unauthorized reuse or privacy harm | Source, consent, license unknown |
| Class imbalance | Uneven class performance | Category counts differ |
| Evaluation leakage | Inflated evaluation claims | TF-IDF fitted before split |
| Mapping mismatch | Wrong category displayed | IDs 10–13 conflict |
| Proxy discrimination | Unequal errors | No fairness assessment |
| Language/layout variation | Poor generalization | No robustness test |
| Automation overreliance | User treats output as objective | No calibration or abstention |
| Category-only job lookup | Irrelevant listing suggestions | No per-listing résumé match |

## Prohibited/unsupported impact
Do not use output to decide or support decisions about any person's employment. The current system is a text-classification demonstration, not a measurement of competence, ability, or career suitability.

## Review questions
- Are data rights and consent documented?
- Are labels defined and consistently encoded?
- Are duplicates and near-duplicates controlled?
- Is the test partition untouched by preprocessing and tuning?
- Are per-class results, uncertainty, and failure modes published?
- Have robustness, accessibility, and relevant bias risks been reviewed?
- Can a user understand, correct, or contest an incorrect result?
- Is the intended use non-consequential and clearly communicated?

Critical credential and data-rights risks must be remediated, not accepted for convenience. For residual risk, record owner, rationale, compensating controls, and expiry using [risk-acceptance-template.md](templates/risk-acceptance-template.md).

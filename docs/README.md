# 📚 Career Compass Documentation

This directory is the technical handbook for the current repository. It describes observed behavior and explicitly marks future designs as proposals.

## Start by task

| I need to... | Read |
|---|---|
| Understand the code flow | [Architecture](architecture.md), [project structure](project-structure.md) |
| Install and run locally | [Installation](installation.md), [configuration](configuration.md) |
| Change application code | [Development](development.md), [testing](testing.md) |
| Change the model or labels | [Model card](model-card.md), [evaluation plan](model-evaluation.md) |
| Use or update data | [Data governance](data-governance.md), [privacy](privacy.md) |
| Review a security issue | [Security review](security-review.md), [SECURITY.md](../SECURITY.md) |
| Deploy or operate | [Deployment](deployment.md), [operations runbook](operations-runbook.md) |
| Review user experience | [Accessibility](accessibility.md), [design and content guide](content-guide.md) |
| Diagnose a failure | [Troubleshooting](troubleshooting.md), [FAQ](faq.md) |
| Propose a structural change | [Decision records](decisions/README.md), [templates](templates/README.md) |

## Documentation rules

- Use present tense for behavior that exists in source.
- Label recommendations and future-state designs as proposed.
- Never document secrets, private résumé content, tokens, or personal records.
- Do not claim legal compliance, fairness, accuracy, accessibility conformance, or production readiness without evidence.
- Keep diagrams and file paths synchronized with the repository.
- Record methodology and data changes with provenance and review evidence.

## Current system boundary

Career Compass is a Streamlit prototype. It loads trusted pickle artifacts, processes uploaded résumé-like text in memory, predicts a category, and makes an external job-search request. There is no project-owned database or documented public API. Important issues are listed in [known issues](known-issues.md).


## Additional model, data, and operations guides

- [Dataset card](dataset-card.md), [model training](model-training.md), [model risk assessment](model-risk-assessment.md), and [prediction guide](prediction-guide.md).
- [External services](external-services.md), [data retention](data-retention.md), [monitoring](monitoring.md), and [backup/recovery](backup-recovery.md).
- [UI/UX review](ui-ux-review.md), [error handling](error-handling.md), [dependency management](dependency-management.md), and [quality gates](quality-gates.md).
- [Responsible use](responsible-use.md), [user journey](user-journey.md), [research notebook guide](research-notebook-guide.md), and [requirements inventory](requirements-inventory.md).
- Root-level [governance](../GOVERNANCE.md) and [disclaimer](../DISCLAIMER.md).

## Local validation commands

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
python scripts/check_repository.py
python -m compileall -q app.py session_state.py scripts
```

These checks verify only a limited set of code and repository hygiene properties. They do not establish model quality, data rights, or production security.


## Additional model, data, and operational references

- [Dataset card](dataset-card.md), [model training](model-training.md), [model risk assessment](model-risk-assessment.md), and [prediction guide](prediction-guide.md).
- [External services](external-services.md), [data retention](data-retention.md), [monitoring](monitoring.md), and [backup/recovery](backup-recovery.md).
- [UI/UX review](ui-ux-review.md), [error handling](error-handling.md), [dependency management](dependency-management.md), and [quality gates](quality-gates.md).
- [Responsible use](responsible-use.md), [user journey](user-journey.md), [research notebook guide](research-notebook-guide.md), and [requirements inventory](requirements-inventory.md).
- Root-level [governance](../GOVERNANCE.md) and [disclaimer](../DISCLAIMER.md).

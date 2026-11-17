# ✅ Quality Gates

## Automated checks

| Gate | Tool | Meaning |
|---|---|---|
| Python syntax | compileall | Selected files parse |
| Helper regression tests | pytest | Isolated tests pass |
| Markdown links | repository check script | Local linked paths exist |
| SVG assets | XML parser | SVG files are well-formed XML |
| Static code analysis | CodeQL workflow | Findings are surfaced for review |
| Dependency updates | Dependabot | Update proposals are created, not auto-approved |

## Not covered
Current automation does not validate full dependency installation, OAuth against Google, live job provider behavior, PDF parsing, upload safety, model accuracy, fairness, calibration, dataset rights, privacy compliance, accessibility conformance, load capacity, or disaster recovery.

A green CI run is a repository-quality signal only. It is not a scientific validation, security certification, privacy compliance statement, or approval for employment use.

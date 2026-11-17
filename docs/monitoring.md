# 📈 Monitoring and Observability

## Current state
The repository does not contain a dedicated metrics, tracing, alerting, or monitoring system. Standard Streamlit logs are not a production observability strategy.

## Suggested operational signals
A future deployment may measure app startup failures, upload validation errors by type/size band, model-load failures, inference exceptions, provider latency/status/timeouts, and dependency/runtime failures.

Do not collect full résumé text, extracted content, OAuth tokens, provider keys, or unnecessary personal identifiers as telemetry.

## Privacy-safe logging
Log safe event names, timestamps, correlation identifiers, and redacted error categories. Remove authorization headers, credential query parameters, request bodies, and user-submitted text. Define retention and access rules before deployment.

## Alerts and review
Each alert should have an owner, threshold, response action, retention period, and test. Alerts provide operational signals; they do not establish model accuracy or fairness.

# 🧭 Understanding a Career Compass Prediction

## What the prediction means
The application cleans decoded résumé-like text, transforms it using a saved TF-IDF vectorizer, and obtains a numeric class from a classifier. A manually maintained dictionary converts that ID into a displayed category.

The displayed category only reflects the class selected by the current experimental model. It does not prove skills, qualifications, experience, or interest.

## Important caveats
- The manual mapping conflicts with notebook label-encoder order for IDs 10–13.
- The app does not present calibrated confidence or an abstention decision.
- The notebook's TF-IDF fitting order introduces evaluation leakage.
- Data provenance, consent, and representativeness are not established.
- Job discovery uses the predicted category and fixed geography, not a validated comparison between a résumé and each listing.

## Demonstration guidance
Use fictional, non-identifying text. Interpret the label only as an example output of a traditional text-classification pipeline. Do not use it to make decisions about a real person's career or employment.

## What a responsible future design would need
A verified encoder, leakage-free evaluation, uncertainty communication, privacy controls, correction path, and strong intended-use restrictions would be prerequisites for broader exploration. This list is a target design, not implemented functionality.

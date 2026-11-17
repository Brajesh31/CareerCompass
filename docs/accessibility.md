# ♿ Accessibility Review

## Scope

The current interface is implemented in Streamlit with custom HTML and CSS. No formal accessibility audit is present. This document defines checks, not a claim of conformance.

## Review checklist

- [ ] Every upload and sign-in control has an accessible name.
- [ ] Instructions and errors are associated with the relevant control.
- [ ] All controls are reachable and usable by keyboard alone.
- [ ] Focus order follows the visual reading order.
- [ ] Focus indicator is visible against the background.
- [ ] Text/background contrast is measured for all states.
- [ ] Status and result changes are announced to assistive technology.
- [ ] Color is not the only way to communicate status.
- [ ] Headings are hierarchical and page content has a clear title.
- [ ] Job links have meaningful names and safe destinations.
- [ ] Layout remains usable at 200% zoom and narrow viewport widths.
- [ ] Custom HTML does not remove semantics or keyboard access.

## Current risk areas

The page uses a remote background image and inline HTML/CSS, while job results are inserted into HTML. These choices require contrast, semantics, and output-escaping review. No test results are currently published.

## Testing

Perform keyboard-only review, screen-reader spot checks, automated scanning, contrast measurement, zoom/reflow testing, and manual review of error and loading states. Record browser, assistive technology, tested routes, issues, and retest evidence.

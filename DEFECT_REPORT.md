# Defect Report

## BUG-001 — Navigation links skipped during WebKit Tab traversal

- Priority: P2; impact: keyboard navigation inconsistency.
- Environment: Windows 11, Playwright 1.57.0 WebKit 26.0.
- Reproduction: open checkout; focus store logo; press Tab.
- Expected: Your bag link receives focus before product controls.
- Observed: Your bag link was inactive; T43 failed.
- Historical evidence: evidence/webkit-run1.xml; screenshot evidence/webkit/test_T43.png may be overwritten by later runs.
- Fix: explicitly set tabindex="0" on store-logo and bag navigation links.
- Targeted verification: T43 passed after the change; full regression status is in TEST_RESULTS.md.

No other application defects are asserted here. During reporting integration, a missing request fixture argument caused teardown errors; this was a test-harness issue and was corrected before final regression. The mobile test was previously adjusted to exclude the intentionally hidden new-order button before receipt creation.

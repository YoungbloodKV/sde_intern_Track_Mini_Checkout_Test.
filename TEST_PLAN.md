# Test Plan

## Objective
Verify deterministic cart pricing, validation, discounts and single-order confirmation through user-visible browser assertions.

## Priorities

| Priority | Risks | Coverage |
|---|---|---|
| P0 | Incorrect totals, invalid checkout, duplicate orders, missing confirmation | T01–T05, T25–T40, D01–D09 |
| P1 | Cart editing/state loss, quantity boundaries, discount edge cases | T06–T24, T41–T42 |
| P2 | Keyboard/mobile usability, browser differences, console errors | T43–T47 |

## Execution
Run `run_tests.bat` or `python run.py test`. Each test uses a new browser context; a session-local HTTP server serves checked-in files. No external checkout services are used. Run Firefox/WebKit after installing them; `--headed` displays browser actions. Repeat complete suites for T48. Tests use retrying assertions, not fixed sleeps.

## Reporting
HTML and JUnit are generated automatically. Screenshots are saved per test; failed calls retain Playwright traces. See README for commands. Report actual failures; preserve original observations when recording a fix. TEST_CASES.md describes actions and assertions; TRACEABILITY_MATRIX.md maps requirements.

## Manual verification
Human execution of T04 empty cart and T05 physical double-click is required separately. Record date, browser, expected/actual behavior, status and evidence in MANUAL_TEST_LOG.md. Agent automation must not be labeled human testing.

## Scope limits
No payments, persistence, backend idempotency, authentication or inventory. Accessibility checks cover markup/focus only, not screen-reader certification. Mobile checks cover a 375px viewport. WebKit is not installed Safari on macOS. Assumptions are maintained in README.md.

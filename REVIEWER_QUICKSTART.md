# Reviewer Quick Start — Mini Checkout & Browser Test Suite

**Challenge:** FyndHacks Round 1 — SDET Intern  
**Application:** `little store.` — synthetic two-product checkout  
**Stack:** HTML, CSS, JavaScript; Python, pytest, Playwright

> This is an **index to the existing repository**, not a replacement for the detailed [README](README.md).

## 1. Run the application

On **Windows**, double-click **`start.bat`** (alias: `run_app.bat`). The standalone frontend opens in your default browser.

For a localhost server on any OS:

```bash
python run.py
```

## 2. Run the browser suite

On **Windows**, double-click **`test.bat`** (alias: `run_tests.bat`). The script prepares a local Python environment as needed; initial installation requires internet access.

Cross-platform equivalent:

```bash
python run.py test
```

To view browser actions instead of running headlessly:

```bash
python run.py test --headed
```

The tests start their own temporary local server; you **do not** need to launch the site first. Every test uses a clean browser context. The README explains optional Firefox/WebKit setup.

## 3. What to verify

| Requirement | Where to inspect |
|---|---|
| Successful order & unique confirmation | [`tests/test_checkout.py`](tests/test_checkout.py), [`evidence/01-successful-checkout.png`](evidence/01-successful-checkout.png) |
| Missing name blocks checkout | [`tests/test_checkout.py`](tests/test_checkout.py), [`evidence/02-missing-name.png`](evidence/02-missing-name.png) |
| Quantity changes exact totals | [`tests/test_checkout.py`](tests/test_checkout.py), [`evidence/03-quantity-total.png`](evidence/03-quantity-total.png) |
| Empty-cart behavior | [`evidence/04-empty-cart.png`](evidence/04-empty-cart.png), [`MANUAL_TEST_LOG.md`](MANUAL_TEST_LOG.md) |
| Duplicate-submit protection | [`evidence/05-double-submit.png`](evidence/05-double-submit.png), [`MANUAL_TEST_LOG.md`](MANUAL_TEST_LOG.md) |
| `SAVE10` discount and receipt | [`tests/test_discounts.py`](tests/test_discounts.py), [`docs/media/showcase-receipt.png`](docs/media/showcase-receipt.png) |
| Browser compatibility | [`TEST_RESULTS.md`](TEST_RESULTS.md) |
| Reproduced keyboard-focus defect | [`DEFECT_REPORT.md`](DEFECT_REPORT.md) |

Browse the [screenshot gallery](docs/SCREENSHOT_GALLERY.md), [test plan](TEST_PLAN.md), [full cases](TEST_CASES.md), and [traceability matrix](TRACEABILITY_MATRIX.md).

## 4. Recorded results vs. new execution

**Archived reports provided with the participant's project** record **59/59 passing** in Chromium, Firefox and WebKit, and another **59/59** passing Chromium run. These are saved outcomes from 21 November 2026, not a claim that a new evaluator's environment will necessarily reproduce them or that GitHub CI has already passed.

- [Chromium results](evidence/chromium-current.xml)
- [Firefox results](evidence/firefox-current.xml)
- [WebKit results](evidence/webkit-current.xml)
- [Repeated Chromium results](junit-results.xml)

**Manual test status:** Automated checks for empty cart and duplicate submit passed, but the organizer separately requires the participant's *manual* observations. See [`MANUAL_TEST_LOG.md`](MANUAL_TEST_LOG.md) for the current status and eventual records.

## 5. Scope / limitations

The app uses only synthetic products and in-memory state. There is no backend, database, real payment, account, shipping integration or persistence. Cross-browser results refer to Playwright browser engines, not every native browser/device. See [README — Assumptions, gaps and submission steps](README.md#-assumptions-gaps-and-submission-steps).

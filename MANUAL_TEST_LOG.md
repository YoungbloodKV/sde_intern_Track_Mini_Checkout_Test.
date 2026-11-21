# Manual Test Log — Complete Before Submission

**Important:** The included Playwright browser checks exercised both scenarios and passed. They were automated, **not human manual testing**. The participant should execute the actions below manually in a visible browser and record honest observations.

## T04 / M01 — Empty-cart validation

- Date/time (participant to fill): __________________
- Browser and version: __________________
- Steps: Reload checkout; leave cart empty; type `Alex Example`; click **Place order**.
- Expected: Cart-empty validation shown; no order confirmation; name still entered.
- Observed result: **PENDING MANUAL EXECUTION**
- Pass/Fail: **NOT YET RECORDED**
- Evidence (local screenshot filename/link): __________________
- Any defect ID: __________________

Automated cross-check available at `evidence/04-empty-cart.png`.

## T05 / M02 — Rapid double-click

- Date/time (participant to fill): __________________
- Browser and version: __________________
- Steps: Reload checkout; add Canvas Tote; enter `Alex Example`; rapidly double-click **Place order** using a mouse.
- Expected: Exactly one **Order placed!** confirmation and one reference; button disabled after success.
- Observed result: **PENDING MANUAL EXECUTION**
- Pass/Fail: **NOT YET RECORDED**
- Evidence (local screenshot filename/link): __________________
- Any defect ID: __________________

Automated cross-check available at `evidence/05-double-submit.png`. This automated case dispatches two synchronous submit events, which is a stronger event-level stress check but is not a substitute for the physical mouse test.

## Defect record template (use only for a real reproduced defect)

**ID:** BUG-___  
**Title:** __________________  
**Severity:** __________________  
**Environment:** __________________  
**Steps to reproduce:** __________________  
**Expected:** __________________  
**Actual:** __________________  
**Evidence:** __________________  
**Reproducibility:** __________________

If no defect is found during manual execution, state: **No defects observed in the executed manual scenarios.**

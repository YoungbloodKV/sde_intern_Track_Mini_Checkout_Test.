# FyndHacks — Paste-ready Submission Information

Use this as a **draft** for the FyndHacks entry fields. Adapt it to the actual field labels, completed manual results and published links. Do not submit unfilled placeholders.

## Project title

**Mini Checkout & Cross-Browser Test Suite | SDET Intern**

## Short description

A single-page, dependency-free checkout for two synthetic products, built alongside an automated Playwright + pytest browser test suite. The app includes cart/quantity controls, exact line and order totals, `SAVE10` promotional discounts, validation for empty carts and missing names, an itemized order receipt, and protection against duplicate confirmations.

Tests cover checkout, cart arithmetic and boundaries, discounts, validation, order safety, and browser behavior using isolated browser contexts and assertions on visible UI results. Source code, setup steps, test plan/cases, archived test reports, reproducible evidence, and a documented WebKit keyboard-focus defect are included in the repository.

## Technologies

HTML · CSS · JavaScript · Python · Playwright · pytest · pytest-html · GitHub Actions

## Saved test evidence

The uploaded project's **archived 21 November 2026 results** record 59 passing checks in each of Playwright Chromium, Firefox and WebKit, plus a second 59-check passing Chromium run. Results are included as HTML/JUnit reports. This is not a claim of a fresh CI run.

## Deliverables

- Repository: `PASTE_GITHUB_REPOSITORY_URL_HERE`
- Demo video (7–10 minutes, Unlisted): `PASTE_YOUTUBE_URL_HERE`
- Entry point: [`README.md`](README.md)
- Reviewer instructions: [`REVIEWER_QUICKSTART.md`](REVIEWER_QUICKSTART.md)
- Actual test results: [`TEST_RESULTS.md`](TEST_RESULTS.md)
- Manual test observations: [`MANUAL_TEST_LOG.md`](MANUAL_TEST_LOG.md) **— fill with real observations before submission**
- Defect report: [`DEFECT_REPORT.md`](DEFECT_REPORT.md)

## Assumptions and known limitations

Synthetic products and client-only, in-memory order state; no backend, payment processing, database, authentication or persistent orders. Results are Playwright engine-based; physical mobile devices and full accessibility audits are outside the tested scope. Refer to the README and test plan for details.

## Before pasting

- Update the manual test log after actually performing the two organizer-required human checks.
- Replace placeholders with accessible links, confirm the video is Unlisted (not Private), and verify the submitted status in FyndHacks.
- If additional testing changes the results, update this summary to match the actual reports.

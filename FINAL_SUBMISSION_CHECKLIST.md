# Final FyndHacks Submission Checklist

**Use this checklist after pushing the final version to GitHub.** Check boxes only after performing the actions. Nothing in this file is proof that a step has already happened.

## Application & automated testing

- [ ] Open the app with `start.bat` and confirm cart, `SAVE10`, validation, totals and receipt are functional on the **final** committed code.
- [ ] Run `test.bat` / `python run.py test` locally after the last code change.
- [ ] Confirm `TEST_RESULTS.md` accurately describes the saved execution reports; update only with **real** new results.
- [ ] Confirm screenshots in README and `docs/SCREENSHOT_GALLERY.md` correspond to the committed UI.
- [ ] Ensure `.venv/`, `__pycache__/`, `.pytest_cache/`, credentials and unnecessary machine-generated data are not in the commit.

## Organizer-required manual observations (outstanding in supplied upload)

- [ ] **T04 / M01:** Manually attempt checkout with an empty cart. Record environment, steps, observed result, Pass/Fail, and screenshot in [`MANUAL_TEST_LOG.md`](MANUAL_TEST_LOG.md).
- [ ] **T05 / M02:** Manually perform a rapid **physical mouse double-click** on Place Order with a valid cart/name. Record whether exactly one confirmation/reference appears, with evidence in the same log.
- [ ] Report any **new real defect** with steps, expected vs. actual, and evidence; do **not** invent a defect. Historical BUG-001 is already described in `DEFECT_REPORT.md`.

## GitHub repository

- [ ] Make a repository containing **the contents of this project folder** (not `.venv/`).
- [ ] Open the repository in a signed-out/private browser tab; verify judges can view it.
- [ ] Check all README image links, source-code links and evidence links.
- [ ] Check **Actions** for the new `browser-tests` workflow. If it fails, investigate and record the real result; do not represent the workflow as passing before it has run.
- [ ] Copy the exact GitHub repository URL for the submission form.

## Required video and portal submission

- [ ] Record a **7–10 minute** walkthrough of your *own* app and tests. Use `VIDEO_WALKTHROUGH.md` for an outline.
- [ ] Upload to YouTube as **Unlisted**; verify the video link works in a private browser window.
- [ ] Supply the repository URL or ZIP, video link, description, results and evidence in the FyndHacks **personal Round 1 submission** form.
- [ ] Check the **personal 24-hour deadline** shown on FyndHacks. Do not assume the public announcement timestamp is the deadline.
- [ ] Verify the portal explicitly says **Submitted** rather than Draft, and retain any confirmation for your records.

## Final links (fill after publishing)

- GitHub repository: `PASTE_PUBLIC_REPOSITORY_URL_HERE`
- YouTube (Unlisted): `PASTE_UNLISTED_VIDEO_URL_HERE`
- FyndHacks submission state / date: `FILL_AFTER_SUBMISSION`

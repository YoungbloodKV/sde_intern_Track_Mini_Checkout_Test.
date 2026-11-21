"""Isolated browser contexts and a temporary local server. No external services."""
import os
import threading
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass


@pytest.fixture(scope="session")
def base_url():
    handler = partial(QuietHandler, directory=str(ROOT))
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}"
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)


@pytest.fixture(scope="session")
def browser(request):
    with sync_playwright() as playwright:
        options = {"headless": not request.config.getoption("--headed")}
        # Optional: use locally installed Chromium when offline.
        if path := os.environ.get("PLAYWRIGHT_CHROMIUM_EXECUTABLE"):
            options["executable_path"] = path
        engine = request.config.getoption("--engine")
        if engine != "chromium": options.pop("executable_path", None)
        browser = getattr(playwright, engine).launch(**options)
        try:
            yield browser
        finally:
            browser.close()


@pytest.fixture
def page(browser, base_url, request):
    # A brand-new browser context gives each test its own clean cart/form state.
    context = browser.new_context(viewport={"width": 1280, "height": 920})
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    if os.environ.get("PLAYWRIGHT_INLINE_ASSETS") == "1":
        # Sandbox-only fallback for environments that block ALL local browser URLs.
        # Load the actual checked-in app files; normal developer runs use HTTP above.
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        html = html.replace('<link rel="stylesheet" href="styles.css" />', "")
        html = html.replace('<script defer src="app.js"></script>', "")
        page.set_content(html, wait_until="domcontentloaded")
        page.add_style_tag(content=(ROOT / "styles.css").read_text(encoding="utf-8"))
        page.add_script_tag(content=(ROOT / "app.js").read_text(encoding="utf-8"))
    else:
        page.goto(base_url, wait_until="domcontentloaded")
    try:
        yield page
    finally:
        target = ROOT / 'evidence' / request.config.getoption('--engine')
        target.mkdir(parents=True, exist_ok=True)
        name = request.node.name
        failed = getattr(request.node, 'rep_call', None)
        if failed and failed.failed:
            context.tracing.stop(path=str(target / (name + '-trace.zip')))
        else:
            context.tracing.stop()
        context.close()


def pytest_addoption(parser):
    parser.addoption("--headed", action="store_true", help="Show the browser")
    parser.addoption('--engine', default='chromium', choices=['chromium', 'firefox', 'webkit'])


@pytest.fixture(autouse=True)
def evidence(request, page):
    yield
    target = ROOT / 'evidence' / request.config.getoption('--engine')
    target.mkdir(exist_ok=True)
    screenshot = page.screenshot(path=str(target / (request.node.name + '.png')), full_page=True)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, 'rep_' + report.when, report)
    if report.when == 'call' and report.failed and 'page' in item.funcargs:
        import base64
        import pytest_html
        screenshot = item.funcargs['page'].screenshot(full_page=True)
        report.extras = [*getattr(report, 'extras', []), pytest_html.extras.png(base64.b64encode(screenshot).decode())]

"""Serve the demo or set up and run its browser tests, without activation."""
import argparse
import os
from pathlib import Path
import subprocess
import sys
import webbrowser
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

ROOT = Path(__file__).resolve().parent
VENV = ROOT / ".venv"
PYTHON = VENV / ("Scripts/python.exe" if os.name == "nt" else "bin/python")


def run(*args):
    subprocess.run([str(arg) for arg in args], cwd=ROOT, check=True)


def test(args):
    if sys.version_info < (3, 10):
        raise RuntimeError("Install Python 3.10 or newer to run the tests.")
    if not PYTHON.exists():
        print("Creating the test environment...", flush=True)
        run(sys.executable, "-m", "venv", VENV)
    requirements = (ROOT / "requirements.txt").read_bytes()
    stamp = VENV / ".checkout-requirements"
    if not stamp.exists() or stamp.read_bytes() != requirements:
        print("Installing test dependencies (first run needs internet)...", flush=True)
        run(PYTHON, "-m", "pip", "install", "-r", ROOT / "requirements.txt")
        stamp.write_bytes(requirements)
    if not os.environ.get("PLAYWRIGHT_CHROMIUM_EXECUTABLE"):
        probe = subprocess.run(
            [str(PYTHON), "-c", "from pathlib import Path; "
             "from playwright.sync_api import sync_playwright; "
             "p = sync_playwright().start(); "
             "exists = Path(p.chromium.executable_path).is_file(); "
             "p.stop(); raise SystemExit(0 if exists else 1)"],
            cwd=ROOT, check=False,
        )
        if probe.returncode:
            print("Installing Chromium (first run needs internet)...", flush=True)
            run(PYTHON, "-m", "playwright", "install", "chromium")
    if args == ["--setup-only"]:
        return
    run(PYTHON, "-m", "pytest", "-v", "tests", *args)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command")
    serve = sub.add_parser("serve", help="Start the checkout in your browser (default)")
    serve.add_argument("--port", type=int, default=0, help="Port; default picks a free port")
    serve.add_argument("--no-browser", action="store_true")
    sub.add_parser("test", help="Set up dependencies and run browser tests")
    args, extra = parser.parse_known_args()
    if args.command == "test":
        test(extra)
        return
    if extra:
        parser.error("unrecognized arguments: " + " ".join(extra))
    handler = partial(SimpleHTTPRequestHandler, directory=str(ROOT))
    with ThreadingHTTPServer(("127.0.0.1", getattr(args, "port", 0)), handler) as server:
        url = f"http://127.0.0.1:{server.server_port}"
        print(f"Checkout: {url}\nPress Ctrl+C to stop.", flush=True)
        if not getattr(args, "no_browser", False):
            webbrowser.open(url)
        server.serve_forever()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nStopped.")
    except subprocess.CalledProcessError as error:
        print(f"Command failed (exit {error.returncode}). Fix the error above and retry.", file=sys.stderr)
        sys.exit(error.returncode)
    except (OSError, RuntimeError) as error:
        print(f"Could not run: {error}", file=sys.stderr)
        sys.exit(1)

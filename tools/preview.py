"""Serve the built site the way GitHub Pages serves it.

`python -m http.server` answers a missing path with its own error page, so the
site's `404.html` -- the one page a reader is most likely to meet by accident --
could not be looked at before it was deployed. Pages serves that file for any
missing path under the site; so does this.
"""

from __future__ import annotations

import sys
from functools import partial
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent / "build" / "quarto" / "_site"


class PagesHandler(SimpleHTTPRequestHandler):
    def send_error(self, code: int, message: str | None = None, explain: str | None = None) -> None:
        page = SITE / "404.html"
        if code != 404 or not page.exists():
            super().send_error(code, message, explain)
            return
        body = page.read_bytes()
        self.send_response(404)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def main() -> None:
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    print(f"serving {SITE} at http://127.0.0.1:{port}")
    HTTPServer(("127.0.0.1", port), partial(PagesHandler, directory=str(SITE))).serve_forever()


if __name__ == "__main__":
    main()

"""Publish the rendered working tree to the canonical local preview URL.

`just preview` owns one preview location on this machine:

    http://new-qual-site-preview.localhost/

The build itself is produced by the recipe before this script runs. This step
only mirrors `build/quarto/_site` into the nginx-served preview directory. It
does not start an ad-hoc HTTP server on a new port: multiple preview URLs made
it too easy to inspect a stale render by accident.
"""

from __future__ import annotations

import shutil
import subprocess
from http.client import HTTPConnection
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent / "build" / "quarto" / "_site"
PREVIEW_ROOT = Path("/var/www/static-sites/new-qual-site-preview")
DEFAULT_NGINX_ROOT = Path("/var/www/html")
PREVIEW_URL = "http://new-qual-site-preview.localhost/"


def _ensure_default_root() -> None:
    """Make the canonical hostname work with the currently loaded nginx config."""
    if DEFAULT_NGINX_ROOT.is_symlink():
        if DEFAULT_NGINX_ROOT.resolve() != PREVIEW_ROOT.resolve():
            raise RuntimeError(f"{DEFAULT_NGINX_ROOT} points somewhere other than {PREVIEW_ROOT}")
        return
    if DEFAULT_NGINX_ROOT.exists():
        raise RuntimeError(f"{DEFAULT_NGINX_ROOT} already exists and is not the preview symlink")
    DEFAULT_NGINX_ROOT.symlink_to(PREVIEW_ROOT, target_is_directory=True)


def _publish() -> None:
    if not (SITE / "index.html").is_file():
        raise RuntimeError(f"rendered site is missing: {SITE}")
    PREVIEW_ROOT.parent.mkdir(parents=True, exist_ok=True)
    PREVIEW_ROOT.mkdir(parents=True, exist_ok=True)
    rsync = shutil.which("rsync")
    if rsync is None:
        raise RuntimeError("rsync is required to publish the local preview")
    subprocess.run([rsync, "-a", "--delete", f"{SITE}/", f"{PREVIEW_ROOT}/"], check=True)
    _ensure_default_root()


def _verify() -> None:
    connection = HTTPConnection("127.0.0.1", 80, timeout=5)
    connection.request(
        "GET",
        "/",
        headers={"Host": "new-qual-site-preview.localhost", "Cache-Control": "no-cache"},
    )
    response = connection.getresponse()
    try:
        if response.status != 200:
            raise RuntimeError(f"preview returned HTTP {response.status}: {PREVIEW_URL}")
    finally:
        response.close()
        connection.close()


def main() -> None:
    _publish()
    _verify()
    print(PREVIEW_URL)


if __name__ == "__main__":
    main()

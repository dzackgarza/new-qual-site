#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = ["httpx>=0.27"]
# ///
"""Extract a PDF to Markdown with the Mistral OCR API and record its provenance.

Transport only: the PDF is uploaded, OCR'd page by page, and the pages are written
in order to the checked-in extraction path, with a provenance file beside it. The
output is a transcription source for intake, not a card.

Reads `MISTRAL_API_KEY` from the environment; `just ocr-pdf` loads it from ~/.envrc.
"""

import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
from typing import Any

import httpx

API = "https://api.mistral.ai/v1"
MODEL = "mistral-ocr-latest"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def ocr(pdf: Path, key: str) -> dict[str, Any]:
    headers = {"Authorization": f"Bearer {key}"}
    with httpx.Client(headers=headers, timeout=httpx.Timeout(900.0)) as client:
        with pdf.open("rb") as fh:
            upload = client.post(
                f"{API}/files",
                data={"purpose": "ocr"},
                files={"file": (pdf.name, fh, "application/pdf")},
            )
        upload.raise_for_status()
        file_id = upload.json()["id"]
        try:
            signed = client.get(f"{API}/files/{file_id}/url", params={"expiry": 1})
            signed.raise_for_status()
            response = client.post(
                f"{API}/ocr",
                json={
                    "model": MODEL,
                    "document": {"type": "document_url", "document_url": signed.json()["url"]},
                    "include_image_base64": False,
                },
            )
            response.raise_for_status()
            result: dict[str, Any] = response.json()
            return result
        finally:
            client.delete(f"{API}/files/{file_id}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("markdown", type=Path)
    args = parser.parse_args()

    key = os.environ["MISTRAL_API_KEY"]
    result = ocr(args.pdf, key)
    pages = sorted(result["pages"], key=lambda page: page["index"])
    body = "\n\n".join(f"<!-- page {page['index'] + 1} -->\n\n{page['markdown'].strip()}" for page in pages)
    args.markdown.parent.mkdir(parents=True, exist_ok=True)
    args.markdown.write_text(body + "\n")

    provenance = {
        "source_pdf": str(args.pdf),
        "source_pdf_sha256": sha256(args.pdf),
        "extracted_markdown": str(args.markdown),
        "extracted_markdown_sha256": sha256(args.markdown),
        "extractor": "mistral-ocr",
        "extractor_model": result["model"],
        "pages": len(pages),
        "command": f"just ocr-pdf {args.pdf} {args.markdown}",
        "generated_at": datetime.date.today().isoformat(),
    }
    args.markdown.with_suffix(".provenance.json").write_text(json.dumps(provenance, indent=2) + "\n")
    print(f"{args.markdown}: {len(pages)} pages")


if __name__ == "__main__":
    main()

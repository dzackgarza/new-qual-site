"""Provenance checks report empty lists, unresolved hrefs, shared hrefs, markdown hrefs, and image hrefs."""

from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread

from qualc.provenance_hrefs import ALL, collection_provenance_hrefs, main, run


def _collection(
    path: Path,
    card_id: str,
    provenance: list[str] | None,
    *,
    areas: list[str] | None = None,
    source_area: str | None = None,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "---",
        f"id: {card_id}",
        "kind: collection",
        "title: Test",
        "review: draft",
    ]
    if areas is not None:
        lines.append("classification:")
        lines.append("  areas:")
        lines.extend(f"  - {area}" for area in areas)
        lines.append("  topics: []")
    if provenance is not None:
        lines.append("provenance:")
        lines.extend(f"  - {href}" for href in provenance)
    if source_area is not None:
        lines.append("source:")
        lines.append("  source_kind: university-exam")
        lines.append("  institution: test")
        lines.append(f"  area: {source_area}")
        lines.append("  problems: []")
        lines.append("  date:")
        lines.append("    kind: unknown")
    lines.extend(["---", ""])
    path.write_text("\n".join(lines))


def _problem(
    path: Path, card_id: str, *, areas: list[str], kind: str = "problem"
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "---",
        f"id: {card_id}",
        f"kind: {kind}",
        "title: Test",
        "review: draft",
        "solved: false",
        "classification:",
        "  areas:",
        *[f"  - {area}" for area in areas],
        "  topics: []",
        "---",
        "",
    ]
    path.write_text("\n".join(lines))


def _findings(root: Path, name: str, *, timeout: float = 2.0) -> list[str]:
    [check] = run([name], root=root, timeout=timeout)
    return check.findings


class _Handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path.startswith("/live"):
            self.send_response(206 if self.headers.get("Range") else 200)
            self.send_header("Content-Type", "application/pdf")
            self.send_header("Content-Range", "bytes 0-0/8")
            self.end_headers()
            self.wfile.write(b"%")
            return
        self.send_response(404)
        self.end_headers()

    def log_message(self, format: str, *args: object) -> None:
        return


def _serve() -> tuple[ThreadingHTTPServer, str]:
    server = ThreadingHTTPServer(("127.0.0.1", 0), _Handler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    host, port = server.server_address[:2]
    assert isinstance(host, str)
    return server, f"http://{host}:{port}"


def test_empty_provenance_is_a_missing_or_empty_list(tmp_path: Path) -> None:
    _collection(tmp_path / "corpus" / "SRC-MISSING.md", "SRC-MISSING", None)
    _collection(tmp_path / "corpus" / "SRC-EMPTY.md", "SRC-EMPTY", [])
    _collection(
        tmp_path / "corpus" / "SRC-HAS.md",
        "SRC-HAS",
        ["assets/attachments/paper.pdf"],
    )
    assert _findings(tmp_path, "empty-provenance") == ["SRC-EMPTY", "SRC-MISSING"]


def test_dead_path_is_not_a_file_under_the_repo(tmp_path: Path) -> None:
    pdf = tmp_path / "assets" / "attachments" / "paper.pdf"
    pdf.parent.mkdir(parents=True)
    pdf.write_bytes(b"%PDF-1.4\n")
    _collection(
        tmp_path / "corpus" / "SRC-LIVE.md",
        "SRC-LIVE",
        ["assets/attachments/paper.pdf"],
    )
    _collection(
        tmp_path / "corpus" / "SRC-DEAD.md",
        "SRC-DEAD",
        ["assets/attachments/missing.pdf"],
    )
    assert _findings(tmp_path, "dead-provenance-hrefs") == [
        "SRC-DEAD: assets/attachments/missing.pdf -> not a file"
    ]
    assert _findings(tmp_path, "empty-provenance") == []


def test_dead_http_href_is_the_get_status_code(tmp_path: Path) -> None:
    href = "https://example.invalid/file with space.pdf"
    _collection(tmp_path / "corpus" / "SRC-SPACE.md", "SRC-SPACE", [href])
    [finding] = _findings(tmp_path, "dead-provenance-hrefs")
    assert finding.startswith(f"SRC-SPACE: {href} -> error:")


def test_http_status_is_the_get_status_code(tmp_path: Path) -> None:
    server, origin = _serve()
    try:
        _collection(
            tmp_path / "corpus" / "SRC-OK.md",
            "SRC-OK",
            [f"{origin}/live.pdf"],
        )
        _collection(
            tmp_path / "corpus" / "SRC-GONE.md",
            "SRC-GONE",
            [f"{origin}/missing.pdf"],
        )
        assert _findings(tmp_path, "dead-provenance-hrefs") == [
            f"SRC-GONE: {origin}/missing.pdf -> 404"
        ]
        assert _findings(tmp_path, "empty-provenance") == []
    finally:
        server.shutdown()
        server.server_close()


def test_origin_remark_is_not_an_href(tmp_path: Path) -> None:
    (tmp_path / "corpus").mkdir()
    (tmp_path / "corpus" / "SRC-ART.md").write_text(
        "\n".join(
            [
                "---",
                "id: SRC-ART",
                "kind: collection",
                "title: Compilation",
                "review: draft",
                "source:",
                "  source_kind: compilation",
                "  area: algebra",
                "  date:",
                "    kind: unknown",
                "---",
                "",
                "::: remark",
                "Neil's notes, origin unrecorded",
                ":::",
                "",
            ]
        )
    )
    assert collection_provenance_hrefs(tmp_path) == []
    assert _findings(tmp_path, "empty-provenance") == ["SRC-ART"]
    assert _findings(tmp_path, "dead-provenance-hrefs") == []


def test_problem_cards_are_not_measured(tmp_path: Path) -> None:
    (tmp_path / "corpus").mkdir()
    (tmp_path / "corpus" / "PRB.md").write_text(
        "\n".join(
            [
                "---",
                "id: PRB",
                "kind: problem",
                "title: A problem",
                "review: draft",
                "solved: false",
                "provenance:",
                "  - https://example.invalid/not-a-collection.pdf",
                "---",
                "",
            ]
        )
    )
    assert collection_provenance_hrefs(tmp_path) == []
    assert _findings(tmp_path, "empty-provenance") == []


def test_duplicate_http_hrefs_are_fetched_once(tmp_path: Path) -> None:
    hits = {"n": 0}

    class CountingHandler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:
            hits["n"] += 1
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"%")

        def log_message(self, format: str, *args: object) -> None:
            return

    server = ThreadingHTTPServer(("127.0.0.1", 0), CountingHandler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        addr = server.server_address
        assert isinstance(addr[0], str)
        origin = f"http://{addr[0]}:{addr[1]}"
        href = f"{origin}/shared.pdf"
        _collection(tmp_path / "corpus" / "SRC-A.md", "SRC-A", [href])
        _collection(tmp_path / "corpus" / "SRC-B.md", "SRC-B", [href])
        assert _findings(tmp_path, "dead-provenance-hrefs") == []
        assert hits["n"] == 1
    finally:
        server.shutdown()
        server.server_close()


def test_shared_provenance_href_is_the_same_string_on_two_collections(
    tmp_path: Path,
) -> None:
    pdf = "assets/attachments/packet.pdf"
    _collection(tmp_path / "corpus" / "SRC-A.md", "SRC-A", [pdf])
    _collection(tmp_path / "corpus" / "SRC-B.md", "SRC-B", [pdf])
    _collection(
        tmp_path / "corpus" / "SRC-C.md",
        "SRC-C",
        ["assets/attachments/other.pdf"],
    )
    assert _findings(tmp_path, "shared-provenance-hrefs") == [f"{pdf}: SRC-A, SRC-B"]


def test_markdown_provenance_href_is_an_href_whose_path_ends_in_md(
    tmp_path: Path,
) -> None:
    _collection(
        tmp_path / "corpus" / "SRC-MD.md",
        "SRC-MD",
        ["assets/ws9/make-me-a-qual/Questions/Algebra/sheet.md"],
    )
    _collection(
        tmp_path / "corpus" / "SRC-MD-HTTP.md",
        "SRC-MD-HTTP",
        ["https://example.invalid/notes.MD?raw=1"],
    )
    _collection(
        tmp_path / "corpus" / "SRC-PDF.md",
        "SRC-PDF",
        ["assets/attachments/paper.pdf"],
    )
    _collection(
        tmp_path / "corpus" / "SRC-YAML.md",
        "SRC-YAML",
        ["assets/ws9/make-me-a-qual/Combined_Questions.yaml"],
    )
    assert _findings(tmp_path, "markdown-provenance-hrefs") == [
        "SRC-MD-HTTP: https://example.invalid/notes.MD?raw=1",
        "SRC-MD: assets/ws9/make-me-a-qual/Questions/Algebra/sheet.md",
    ]


def test_forbidden_provenance_href_is_under_a_forbidden_source_tree(
    tmp_path: Path,
) -> None:
    _collection(
        tmp_path / "corpus" / "SRC-MMAQ.md",
        "SRC-MMAQ",
        ["assets/ws9/make-me-a-qual/Combined_Questions.yaml"],
    )
    _collection(
        tmp_path / "corpus" / "SRC-ATTACH.md",
        "SRC-ATTACH",
        ["assets/attachments/paper.pdf"],
    )
    _collection(
        tmp_path / "corpus" / "SRC-GH.md",
        "SRC-GH",
        ["https://github.com/dzackgarza/make-me-a-qual/blob/main/foo.pdf"],
    )
    assert _findings(tmp_path, "forbidden-provenance-hrefs") == [
        "SRC-GH: https://github.com/dzackgarza/make-me-a-qual/blob/main/foo.pdf (dzackgarza repository)",
        "SRC-MMAQ: assets/ws9/make-me-a-qual/Combined_Questions.yaml (dzackgarza repo copy)",
    ]


def test_image_provenance_href_is_an_href_whose_path_ends_in_an_image_suffix(
    tmp_path: Path,
) -> None:
    _collection(
        tmp_path / "corpus" / "SRC-PNG.md",
        "SRC-PNG",
        [
            "sources/qualbot-question-images/QualbotQuestions/Complex Analysis/Conformal map 1.png"
        ],
    )
    _collection(
        tmp_path / "corpus" / "SRC-JPG-HTTP.md",
        "SRC-JPG-HTTP",
        ["https://example.invalid/figures/map.JPG?raw=1"],
    )
    _collection(
        tmp_path / "corpus" / "SRC-PDF.md",
        "SRC-PDF",
        ["assets/attachments/paper.pdf"],
    )
    assert _findings(tmp_path, "image-provenance-hrefs") == [
        "SRC-JPG-HTTP: https://example.invalid/figures/map.JPG?raw=1",
        "SRC-PNG: sources/qualbot-question-images/QualbotQuestions/Complex Analysis/Conformal map 1.png",
    ]


def test_one_collection_listing_an_href_twice_is_not_shared(tmp_path: Path) -> None:
    pdf = "assets/attachments/packet.pdf"
    _collection(tmp_path / "corpus" / "SRC-A.md", "SRC-A", [pdf, pdf])
    assert _findings(tmp_path, "shared-provenance-hrefs") == []


def test_collection_area_without_problem_cards_is_the_area_on_no_problem(
    tmp_path: Path,
) -> None:
    _collection(
        tmp_path / "corpus" / "SRC-STAT.md",
        "SRC-STAT",
        [],
        areas=["statistics"],
        source_area="statistics",
    )
    _collection(
        tmp_path / "corpus" / "SRC-ALG.md",
        "SRC-ALG",
        [],
        areas=["algebra"],
        source_area="algebra",
    )
    _problem(tmp_path / "corpus" / "P-ALG.md", "P-ALG", areas=["algebra"])
    _problem(
        tmp_path / "corpus" / "E-ALG.md",
        "E-ALG",
        areas=["algebra"],
        kind="exercise",
    )
    assert _findings(tmp_path, "collection-area-without-problem-cards") == [
        "SRC-STAT: statistics"
    ]


def test_exits_zero_with_findings_and_is_not_a_gate(tmp_path: Path) -> None:
    _collection(tmp_path / "corpus" / "SRC-EMPTY.md", "SRC-EMPTY", [])
    _collection(
        tmp_path / "corpus" / "SRC-DEAD.md",
        "SRC-DEAD",
        ["assets/missing.pdf"],
    )
    assert main(["--root", str(tmp_path), "--json"]) == 0
    payload = [
        {
            "check": check.name,
            "ok": check.ok,
            "findings": check.findings,
            "measured": check.measured,
        }
        for check in run(ALL, root=tmp_path, timeout=2.0)
    ]
    dumped = json.dumps(payload)
    assert "empty-provenance" in dumped
    assert "dead-provenance-hrefs" in dumped
    assert "shared-provenance-hrefs" in dumped
    assert "markdown-provenance-hrefs" in dumped
    assert "image-provenance-hrefs" in dumped
    assert "collection-area-without-problem-cards" in dumped
    empty = next(item for item in payload if item["check"] == "empty-provenance")
    dead = next(item for item in payload if item["check"] == "dead-provenance-hrefs")
    shared = next(
        item for item in payload if item["check"] == "shared-provenance-hrefs"
    )
    markdown = next(
        item for item in payload if item["check"] == "markdown-provenance-hrefs"
    )
    image = next(item for item in payload if item["check"] == "image-provenance-hrefs")
    no_problems = next(
        item
        for item in payload
        if item["check"] == "collection-area-without-problem-cards"
    )
    assert empty["findings"] == ["SRC-EMPTY"]
    assert empty["ok"] is False
    assert empty["measured"] == 2
    assert dead["findings"] == ["SRC-DEAD: assets/missing.pdf -> not a file"]
    assert dead["ok"] is False
    assert dead["measured"] == 1
    assert shared["findings"] == []
    assert shared["ok"] is True
    assert shared["measured"] == 1
    assert markdown["findings"] == []
    assert markdown["ok"] is True
    assert markdown["measured"] == 1
    assert image["findings"] == []
    assert image["ok"] is True
    assert image["measured"] == 1
    assert no_problems["findings"] == []
    assert no_problems["ok"] is True
    assert no_problems["measured"] == 2

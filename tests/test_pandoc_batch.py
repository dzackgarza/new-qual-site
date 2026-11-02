"""Batched Pandoc reads preserve each card's independent document semantics."""

from __future__ import annotations

import json
import subprocess
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import pytest

from qualc import emit, model
from qualc import pandoc_batch as pb
from qualc.pandoc_batch import (
    PandocBatchError,
    PandocFailure,
    PandocServer,
    pandoc_executable,
    write_html_parallel,
    write_markdown_parallel,
)


def _card(path: Path, card_id: str, footnote: str) -> Path:
    path.write_text(
        f"""---
schema: qual/card@1
id: {card_id}
kind: problem
title: Problem {card_id}
classification:
  areas: [algebra]
  topics: [groups]
relations: []
review: draft
---

# Shared heading {{#shared}}

::: problem
Dr. Example states {card_id}.[^local]

[^local]: {footnote}
:::
"""
    )
    return path


def _isolated_ast(path: Path) -> dict:
    _, body = model.split_front_matter(path.read_text(), path)
    result = subprocess.run(
        [
            str(pandoc_executable()),
            "--from",
            model.MARKDOWN,
            "--to",
            "json",
            "--standalone",
            "--fail-if-warnings",
        ],
        input=body,
        capture_output=True,
        text=True,
        check=True,
    )
    payload: object = json.loads(result.stdout)
    assert isinstance(payload, dict)
    return payload


def test_batch_parse_matches_isolated_pandoc(tmp_path: Path) -> None:
    paths = [
        _card(tmp_path / "P-FIRST.md", "P-FIRST", "First local footnote."),
        _card(tmp_path / "P-SECOND.md", "P-SECOND", "Second local footnote."),
    ]

    parsed, errors = model.parse_cards(paths)

    assert errors == []
    assert [json.loads(item.ast) for item in parsed] == [_isolated_ast(path) for path in paths]


def test_batch_inline_parse_keeps_titles_inline() -> None:
    """A title is inline text. The batch cache must return inlines, not a
    block wrapper, and must not leak the boundary sentinel into the page."""
    title = "Uniform limits of continuous functions are continuous"
    with PandocServer() as pandoc:
        cache = emit.build_inline_cache(pandoc, [title])
    inlines = cache[title]
    assert type(inlines[0]).__name__ == "Str"
    assert all(emit.INLINE_SENTINEL not in str(inline) for inline in inlines)


def test_parallel_writers_preserve_serial_result_order() -> None:
    documents = [
        json.dumps(
            {
                "pandoc-api-version": [1, 23],
                "meta": {},
                "blocks": [{"t": "Para", "c": [{"t": "Str", "c": f"item-{index}"}]}],
            }
        )
        for index in range(24)
    ]
    with PandocServer() as pandoc:
        serial_markdown = pandoc.write_markdown(documents, model.MARKDOWN)
        serial_html = pandoc.write_html(documents)

    parallel_markdown = write_markdown_parallel(documents, model.MARKDOWN)
    parallel_html = write_html_parallel(documents)

    assert parallel_markdown == serial_markdown
    assert parallel_html == serial_html


def test_wikilink_text_typesets_dashes(tmp_path: Path) -> None:
    path = tmp_path / "P-LINK.md"
    path.write_text(_card(tmp_path / "P-LINK.md", "P-LINK", "Note.").read_text().replace("Dr. Example states", "See [[FF-CSABG|Artin--Rees lemma]];"))

    parsed, errors = model.parse_cards([path])

    assert errors == []
    assert "Artin–Rees" in parsed[0].ast
    assert "Artin--Rees" not in parsed[0].ast


def test_citation_keeps_its_locator() -> None:
    source = "A [@DF04, Section 10.1, Exercise 8]. B [@DF04, p. 5].\n"
    vocabularies = Path(__file__).resolve().parent.parent / "vocabularies"
    result = subprocess.run(
        [
            str(pandoc_executable()),
            "--citeproc",
            "--bibliography",
            str(vocabularies / "references.yaml"),
            "--csl",
            str(vocabularies / "citation-style.csl"),
            "--to",
            "plain",
            "--wrap",
            "none",
        ],
        input=source,
        capture_output=True,
        text=True,
        check=True,
    )
    assert "[DuFo04, Section 10.1, Exercise 8]" in result.stdout
    assert "[DuFo04, p. 5]" in result.stdout


def test_corporate_author_citation_renders_its_label() -> None:
    """A corporate author has no family name to build a label from, so the
    bibliography gives `Har07` an explicit `citation-label`, and the server's
    citeproc read of the committed bibliography renders it."""
    with PandocServer() as pandoc:
        (result,) = pandoc.read_markdown(["See [@Har07].\n"], model.MARKDOWN, model.load_citations(model.VOCABULARIES))
    text = json.dumps(json.loads(result.output)["blocks"][0])
    assert '"Har07"' in text


class _DeadlineServer:
    """A loopback stand-in for `pandoc server`, refusing batches over a size.

    Pandoc's `server --timeout` is a deadline on one request: a request that
    outlives it gets an empty 503 and the server stays healthy. This fake
    reproduces that refusal without any load, so the recovery path can be tested
    deterministically.
    """

    def __init__(self, refuse_over: int | None) -> None:
        self.refuse_over = refuse_over
        self.accepted: list[int] = []
        self.refused: list[int] = []
        outer = self

        class Handler(BaseHTTPRequestHandler):
            def do_POST(self) -> None:  # noqa: N802 - the stdlib name
                length = int(self.headers.get("Content-Length", "0"))
                batch = json.loads(self.rfile.read(length))
                if outer.refuse_over is not None and len(batch) > outer.refuse_over:
                    outer.refused.append(len(batch))
                    self.send_response(503)
                    self.send_header("Content-Length", "0")
                    self.end_headers()
                    return
                outer.accepted.append(len(batch))
                body = json.dumps(
                    [
                        {"output": f"doc-{item['text']}", "base64": False, "messages": []}
                        for item in batch
                    ]
                ).encode()
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

            def log_message(self, *args: object) -> None:
                pass

        self.httpd = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        self.thread = threading.Thread(target=self.httpd.serve_forever, daemon=True)

    def __enter__(self) -> _DeadlineServer:
        self.thread.start()
        return self

    def __exit__(self, *exc: object) -> None:
        self.httpd.shutdown()
        self.httpd.server_close()
        self.thread.join()

    @property
    def port(self) -> int:
        return int(self.httpd.server_address[1])


def _requests(count: int) -> list[dict[str, object]]:
    return [{"text": str(index), "from": "markdown", "to": "html", "standalone": False} for index in range(count)]


def test_a_batch_that_outruns_the_server_deadline_is_halved_and_completes() -> None:
    with _DeadlineServer(refuse_over=2) as fake:
        server = PandocServer()
        server._port = fake.port
        results = server._convert(_requests(8))

    assert [result.output for result in results] == [f"doc-{index}" for index in range(8)]
    assert fake.refused == [8, 4, 4], "the oversized attempts should have been the batch and then its halves"
    assert all(size <= 2 for size in fake.accepted), "every accepted batch should fit the deadline"
    assert sum(fake.accepted) == 8, "each document should be converted exactly once, not duplicated by the splits"


def test_a_single_document_over_the_deadline_is_raised_not_swallowed() -> None:
    with _DeadlineServer(refuse_over=0) as fake:
        server = PandocServer()
        server._port = fake.port
        with pytest.raises(PandocBatchError) as raised:
            server._convert(_requests(3))

    message = str(raised.value)
    assert "request 0" in message and "cannot help" in message
    assert "HTTP 503" in message, "the observed failure must be reported, not only the inference"


def test_a_response_truncated_by_the_deadline_is_recovered_too() -> None:
    """The server does not always answer 503: it can also die mid-response.

    Reproduced against the pinned Pandoc 3.10.2 while fixing this: with a short
    deadline the server began a 200 response and abandoned it, and the client
    saw `http.client.IncompleteRead` from `json.load` rather than an HTTP error.
    """

    class Handler(BaseHTTPRequestHandler):
        def do_POST(self) -> None:  # noqa: N802 - the stdlib name
            length = int(self.headers.get("Content-Length", "0"))
            batch = json.loads(self.rfile.read(length))
            if len(batch) > 2:
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", "1000")
                self.end_headers()
                self.wfile.write(b'[{"output"')  # truncate in flight
                self.wfile.flush()
                self.close_connection = True
                return
            body = json.dumps(
                [{"output": f"doc-{item['text']}", "base64": False, "messages": []} for item in batch]
            ).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, *args: object) -> None:
            pass

    httpd = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    try:
        server = PandocServer()
        server._port = int(httpd.server_address[1])
        results = server._convert(_requests(4))
    finally:
        httpd.shutdown()
        httpd.server_close()
        thread.join()

    assert [result.output for result in results] == [f"doc-{index}" for index in range(4)]


def test_conversion_failures_are_not_retried() -> None:
    calls: list[int] = []

    class Handler(BaseHTTPRequestHandler):
        def do_POST(self) -> None:  # noqa: N802 - the stdlib name
            length = int(self.headers.get("Content-Length", "0"))
            batch = json.loads(self.rfile.read(length))
            calls.append(len(batch))
            body = json.dumps([{"error": "not a card"} for _ in batch]).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, *args: object) -> None:
            pass

    httpd = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    try:
        server = PandocServer()
        server._port = int(httpd.server_address[1])
        results = server._convert(_requests(4))
    finally:
        httpd.shutdown()
        httpd.server_close()
        thread.join()

    assert calls == [4], "a conversion failure in the payload must not be retried or halved"
    assert all(isinstance(result, PandocFailure) and result.error == "not a card" for result in results)


def test_parallel_workers_stays_within_its_bounds(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv(pb.PARALLEL_WORKERS_ENV, raising=False)
    for cpus in (1, 2, 4, 12, 64):
        for load in (0.0, 0.5, 1.0, 3.7, 29.0, 1000.0):
            workers = pb.parallel_workers(load=load, cpus=cpus)
            assert pb.PARALLEL_WORKERS_FLOOR <= workers <= pb.PARALLEL_WORKERS_CEILING
            assert workers <= max(1, cpus)


def test_parallel_workers_shrinks_under_load(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv(pb.PARALLEL_WORKERS_ENV, raising=False)
    assert pb.parallel_workers(load=0.0, cpus=12) == 8, "an idle 12-core machine reaches the ceiling"
    assert pb.parallel_workers(load=29.0, cpus=12) == 1, "the case issue #100 recorded collapses to one worker"
    assert pb.parallel_workers(load=3.0, cpus=4) == 1
    assert pb.parallel_workers(load=1.0, cpus=4) == 2
    # One core is reserved for the rest of the machine, so an idle two-core box
    # leaves a single worker rather than both.
    assert pb.parallel_workers(load=0.0, cpus=2) == 1
    assert pb.parallel_workers(load=0.0, cpus=1) == 1


def test_parallel_workers_honours_the_documented_override(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv(pb.PARALLEL_WORKERS_ENV, "2")
    assert pb.parallel_workers(load=29.0, cpus=64) == 2
    monkeypatch.setenv(pb.PARALLEL_WORKERS_ENV, " 8 ")
    assert pb.parallel_workers(load=0.0, cpus=1) == 8


@pytest.mark.parametrize("value", ["", "two", "0", "-1", "9", "3.5"])
def test_parallel_workers_rejects_an_unusable_override(value: str, monkeypatch: pytest.MonkeyPatch) -> None:
    if not value.strip():
        monkeypatch.delenv(pb.PARALLEL_WORKERS_ENV, raising=False)
        assert pb.parallel_workers(load=0.0, cpus=4) >= 1  # empty means "no override", not an error
        return
    monkeypatch.setenv(pb.PARALLEL_WORKERS_ENV, value)
    with pytest.raises(pb.PandocBatchError) as raised:
        pb.parallel_workers(load=0.0, cpus=4)
    assert pb.PARALLEL_WORKERS_ENV in str(raised.value)


def test_parallel_workers_falls_back_when_no_load_average_is_reported(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv(pb.PARALLEL_WORKERS_ENV, raising=False)
    monkeypatch.setattr(pb, "_one_minute_load", lambda: None)
    assert pb.parallel_workers(cpus=12) == 8
    assert pb.parallel_workers(cpus=3) == 3
    assert pb.parallel_workers(cpus=1) == 1

"""One build-scoped Pandoc process with independent batched conversions."""

from __future__ import annotations

import base64
import json
import socket
import subprocess
import time
import urllib.request
from dataclasses import dataclass
from types import TracebackType
from typing import Self

BATCH_SIZE = 256
SERVER_START_ATTEMPTS = 500
SERVER_START_INTERVAL_SECONDS = 0.01
SERVER_REQUEST_TIMEOUT_SECONDS = 60


class PandocBatchError(RuntimeError):
    """The persistent Pandoc boundary failed or returned an invalid response."""


@dataclass(frozen=True)
class PandocMessage:
    message: str
    verbosity: str


@dataclass(frozen=True)
class PandocOutput:
    output: str
    messages: tuple[PandocMessage, ...]


@dataclass(frozen=True)
class PandocFailure:
    error: str


PandocResult = PandocOutput | PandocFailure


def _free_port() -> int:
    with socket.socket() as listener:
        listener.bind(("127.0.0.1", 0))
        return int(listener.getsockname()[1])


class PandocServer:
    """Own one native Pandoc server for a compiler invocation."""

    def __init__(self) -> None:
        self._process: subprocess.Popen[str] | None = None
        self._port: int | None = None
        self._abbreviations: str | None = None

    def __enter__(self) -> Self:
        abbreviations = subprocess.run(
            ["pandoc", "--print-default-data-file=abbreviations"],
            check=True,
            capture_output=True,
        ).stdout
        port = _free_port()
        process = subprocess.Popen(
            ["pandoc", "server", "--port", str(port), "--timeout", "30"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        for _ in range(SERVER_START_ATTEMPTS):
            returncode = process.poll()
            if returncode is not None:
                stderr = process.stderr.read() if process.stderr is not None else ""
                raise PandocBatchError(
                    f"pandoc server exited during startup ({returncode}): {stderr.strip()}"
                )
            with socket.socket() as probe:
                if probe.connect_ex(("127.0.0.1", port)) == 0:
                    self._process = process
                    self._port = port
                    self._abbreviations = base64.b64encode(abbreviations).decode()
                    return self
            time.sleep(SERVER_START_INTERVAL_SECONDS)
        process.terminate()
        process.wait()
        raise PandocBatchError("pandoc server did not accept connections")

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        process = self._require_process()
        process.terminate()
        process.wait()
        self._process = None
        self._port = None
        self._abbreviations = None

    def read_markdown(
        self, texts: list[str], markdown_format: str
    ) -> list[PandocResult]:
        abbreviations = self._require_abbreviations()
        requests = [
            {
                "text": text,
                "from": markdown_format,
                "to": "json",
                "standalone": True,
                "abbreviations": "abbreviations",
                "files": {"abbreviations": abbreviations},
            }
            for text in texts
        ]
        return self._convert(requests)

    def write_markdown(
        self, documents: list[str], markdown_format: str
    ) -> list[PandocResult]:
        abbreviations = self._require_abbreviations()
        requests = [
            {
                "text": document,
                "from": "json",
                "to": markdown_format,
                "standalone": False,
                "wrap": "preserve",
                "abbreviations": "abbreviations",
                "files": {"abbreviations": abbreviations},
            }
            for document in documents
        ]
        return self._convert(requests)

    def write_html(self, documents: list[str]) -> list[PandocResult]:
        abbreviations = self._require_abbreviations()
        requests = [
            {
                "text": document,
                "from": "json",
                "to": "html",
                "standalone": False,
                "html-math-method": "mathjax",
                "syntax-highlighting": "none",
                "abbreviations": "abbreviations",
                "files": {"abbreviations": abbreviations},
            }
            for document in documents
        ]
        return self._convert(requests)

    def _convert(self, requests: list[dict[str, object]]) -> list[PandocResult]:
        results: list[PandocResult] = []
        for offset in range(0, len(requests), BATCH_SIZE):
            results.extend(self._request(requests[offset : offset + BATCH_SIZE]))
        if len(results) != len(requests):
            raise PandocBatchError(
                f"pandoc batch returned {len(results)} results "
                f"for {len(requests)} requests"
            )
        return results

    def _request(self, requests: list[dict[str, object]]) -> list[PandocResult]:
        request = urllib.request.Request(
            f"http://127.0.0.1:{self._require_port()}/batch",
            data=json.dumps(requests).encode(),
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
        )
        with urllib.request.urlopen(
            request, timeout=SERVER_REQUEST_TIMEOUT_SECONDS
        ) as response:
            payload: object = json.load(response)
        if not isinstance(payload, list):
            raise PandocBatchError("pandoc batch response is not a JSON array")
        return [self._decode_result(item) for item in payload]

    @staticmethod
    def _decode_result(item: object) -> PandocResult:
        if not isinstance(item, dict):
            raise PandocBatchError("pandoc conversion result is not a JSON object")
        if "error" in item:
            error = item["error"]
            if not isinstance(error, str):
                raise PandocBatchError("pandoc conversion error is not text")
            return PandocFailure(error)
        output = item["output"]
        encoded = item["base64"]
        raw_messages = item["messages"]
        if not isinstance(output, str) or encoded is not False:
            raise PandocBatchError("pandoc conversion returned an invalid text output")
        if not isinstance(raw_messages, list):
            raise PandocBatchError("pandoc conversion messages are not an array")
        messages: list[PandocMessage] = []
        for raw_message in raw_messages:
            if not isinstance(raw_message, dict):
                raise PandocBatchError("pandoc conversion message is not an object")
            message = raw_message["message"]
            verbosity = raw_message["verbosity"]
            if not isinstance(message, str) or not isinstance(verbosity, str):
                raise PandocBatchError("pandoc conversion message fields are invalid")
            messages.append(PandocMessage(message=message, verbosity=verbosity))
        return PandocOutput(output=output, messages=tuple(messages))

    def _require_process(self) -> subprocess.Popen[str]:
        if self._process is None:
            raise PandocBatchError("pandoc server is not running")
        return self._process

    def _require_port(self) -> int:
        if self._port is None:
            raise PandocBatchError("pandoc server has no active port")
        return self._port

    def _require_abbreviations(self) -> str:
        if self._abbreviations is None:
            raise PandocBatchError("pandoc server has no abbreviations resource")
        return self._abbreviations

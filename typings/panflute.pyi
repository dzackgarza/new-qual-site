"""Typing boundary for Panflute, which does not publish PEP 561 metadata.

Panflute's element model is intentionally dynamic and the project already
narrows its runtime objects explicitly before use.  Declare that upstream
boundary as dynamic so mypy continues checking the surrounding project code
instead of rejecting the third-party import itself.
"""

from typing import Any

def __getattr__(name: str) -> Any: ...

import pytest
import yaml
from qualc.model import load_front_matter


def test_repeated_top_level_key_is_rejected() -> None:
    with pytest.raises(yaml.constructor.ConstructorError, match="duplicate key 'audit'"):
        load_front_matter("id: P-1\naudit: [a]\naudit: [b]\n")


def test_repeated_nested_key_is_rejected() -> None:
    with pytest.raises(yaml.constructor.ConstructorError, match="duplicate key 'by'"):
        load_front_matter("id: P-1\naudit:\n  - by: x\n    by: y\n")


def test_distinct_keys_load_intact() -> None:
    assert load_front_matter("id: P-1\naudit:\n  - by: x\n    at: 2026\n") == {"id": "P-1", "audit": [{"by": "x", "at": 2026}]}

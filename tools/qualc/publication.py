"""Validated publication manifests.

Cards own mathematical content and stable identity. A publication manifest owns
only reading order, hierarchy, connective prose, and appearances of those cards.
"""

from __future__ import annotations

from pathlib import Path
from typing import Literal

import yaml
from pydantic import BaseModel, ConfigDict, Field, model_validator

from .model import Review


class Strict(BaseModel):
    model_config = ConfigDict(extra="forbid")


class PublicationQuery(Strict):
    kind: Literal[
        "problem",
        "solution",
        "hint",
        "definition",
        "theorem",
        "proposition",
        "corollary",
        "lemma",
        "proof",
        "example",
        "exercise",
        "remark",
        "strategy",
        "concept",
        "fact",
        "claim",
        "warning",
        "slogan",
    ]
    topics: list[str]
    limit: int = Field(gt=0)
    review: list[Review] | None = None


class ReferenceItem(Strict):
    ref: str


class QueryItem(Strict):
    query: PublicationQuery


PublicationItem = ReferenceItem | QueryItem


class PublicationSection(Strict):
    slug: str = Field(pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
    title: str = Field(min_length=1)
    parent: str = Field(min_length=1)
    lede: str = Field(min_length=1)
    items: list[PublicationItem]


class PublicationManifest(Strict):
    schema_name: Literal["qual/publication@2"] = Field(alias="schema")
    id: str = Field(min_length=1)
    kind: Literal["study-guide"]
    title: str = Field(min_length=1)
    lede: str = Field(min_length=1)
    sections: list[PublicationSection] = Field(min_length=1)

    @model_validator(mode="after")
    def validate_hierarchy(self) -> PublicationManifest:
        known = {self.id}
        for section in self.sections:
            if section.slug in known:
                raise ValueError(f"duplicate publication node: {section.slug}")
            if section.parent not in known:
                raise ValueError(
                    f"publication parent must precede its child: "
                    f"{section.slug} -> {section.parent}"
                )
            known.add(section.slug)
        return self


def load_publications(directory: Path) -> list[PublicationManifest]:
    return [
        PublicationManifest.model_validate(yaml.safe_load(path.read_text()))
        for path in sorted(directory.glob("*.yaml"))
    ]

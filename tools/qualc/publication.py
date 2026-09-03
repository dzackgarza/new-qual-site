"""Validated publication manifests.

Cards own mathematical content and stable identity. A publication manifest owns
only reading order, hierarchy, connective prose, and appearances of those cards.
"""

from __future__ import annotations

from pathlib import Path
from typing import Literal

import yaml
from pydantic import BaseModel, ConfigDict, Field, model_validator


class Strict(BaseModel):
    model_config = ConfigDict(extra="forbid")


class PublicationQuery(Strict):
    # A guide is authored mathematics, not a projection of the card database.
    # Queries exist only to hand a topic family to the canonical problem browser;
    # reference material enters the guide by an explicit `ref:` chosen by the
    # author and is transcluded where the exposition needs it. Sampling and
    # runtime filters belong to the browser, so the manifest stores neither a
    # build-time limit nor a source-appearance category such as “exercise”.
    topics: list[str] = Field(min_length=1)


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

    @property
    def area(self) -> str:
        """The subject every query in this guide is scoped to.

        A study guide's id names its subject -- `GUIDE-COMPLEX-ANALYSIS` is the
        complex-analysis guide -- so the scope is already recorded and does not
        become a field a manifest author can forget. An optional `areas` key on
        the query would default to unscoped, and unscoped is the defect: topic
        terms are shared between subjects, so `integrals` carries 19
        real-analysis problems as well as 7 complex-analysis ones.

        The value is carried directly into each problem-browser deep link. The guide
        does not resolve the query against the catalog at build time.
        """
        return self.id.removeprefix("GUIDE-").lower()

    @model_validator(mode="after")
    def validate_hierarchy(self) -> PublicationManifest:
        known = {self.id}
        for section in self.sections:
            if section.slug in known:
                raise ValueError(f"duplicate publication node: {section.slug}")
            if section.parent not in known:
                raise ValueError(f"publication parent must precede its child: {section.slug} -> {section.parent}")
            known.add(section.slug)
        return self


def load_publications(directory: Path) -> list[PublicationManifest]:
    return [PublicationManifest.model_validate(yaml.safe_load(path.read_text())) for path in sorted(directory.glob("*.yaml"))]

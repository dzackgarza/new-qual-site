# Workshops cross-subject branch: build proof

Manifest: `publications/workshops-guide.yaml`. Built and inspected at `825c835b`.

Built in a private worktree at that revision, so the build tools are committed state and
nothing could delete the output mid-inspection:

```
git worktree add <scratchpad>/ws-proof3 825c835b
uv run qualc build   # exit 0, 8,213 cards and 327 wiki pages OK
```

`artifacts/issue-17/validate-site` over the whole rendered site:

```
html_pages: 5824
html_parse_errors: 0
local_references: 82811
missing_local_targets: 0
missing_fragments: 0
qmd_links: 0
```

## What the branch was missing

There are two workshop corpora in this repository, and the branch covered one of them.

The **wiki week pages**, twelve under `wiki/Workshops`, cite 98 canonical cards that the
subject branches already own. Those were the manifest's four sections.

The **extracted worksheets**, 22 sitting cards under `corpus/ws9` with 249 occurrences and
the 217 problems and theorems behind them, were absent from the branch entirely. They are
the "extracted card" half of issue #29's criterion, and they are a different set of
mathematics from the week pages, not a second copy of it.

| | |
| --- | ---: |
| sections, before / after | 4 / 6 |
| items, before / after | 98 / 140 |
| workshop sittings named | 22 |
| occurrences reached through them | 247 |
| canonical problems reached through them | 240 |
| cards reachable from the branch | 625 |
| WORKSHOP-prefixed cards reachable | 467 of 467 |

## Classification

One card and its occurrence were the only Workshops cards without topics:
`P-RA-WORKSHOP-D3-SEQ-15` and `O-RA-WORKSHOP-D3-SEQ-15`, now `series-of-numbers`,
`sequences-of-numbers`, `convergence`. Every other extracted workshop card was already
classified by the Real Analysis and Topology lanes.

22 source cards carry no topics, which is the convention in every subject: a sitting is an
institution, an area and a date.

## Routes

7 emitted, one root and 6 sections:

```
/guide/GUIDE-WORKSHOPS.html
/guide/GUIDE-WORKSHOPS/algebra.html
/guide/GUIDE-WORKSHOPS/real-analysis.html
/guide/GUIDE-WORKSHOPS/complex-analysis.html
/guide/GUIDE-WORKSHOPS/topology.html
/guide/GUIDE-WORKSHOPS/real-analysis-sittings.html
/guide/GUIDE-WORKSHOPS/topology-sittings.html
```

The four subjects hang off the guide root and each sittings section off its own subject,
so the tree is two deep. They were a linear chain until `97632608`, which made the Real
Analysis sittings breadcrumb read `Workshops / Algebra / Real Analysis / ...`; no workshop
in one subject is a prerequisite for a workshop in another.

## How reachability is achieved

Each sitting is one ref, not an inlined copy of its problem list. `emit.source_page`
renders every occurrence of a sitting on that sitting's own route, in the order they
appeared, each linked to its canonical problem, and `audit.py`'s orphan check draws the
same edge — so naming the sitting reaches its occurrences and their problems. The
screenshot `sitting-exam-page.png` is that page for Day 1: "12 problems, in the order they
appeared", every one a link.

That page is also where issue #29's other requirement is visible. Its warm-up 3 links to
`P-T11A1`, item 1 to `P-AISD5`, item 3 to `P-T05A2`, item 6 to `P-T11A4`: canonical cards
in the Topology branch, not workshop-only duplicates minted to give a workshop item a
route, which the issue forbids.

The nineteen theorems and one definition of the Real Analysis worksheets are the exception
and are named directly. They carry no occurrence, so no sitting page lists them and the
closure above does not reach them.

## What was inspected

Headless Chromium at 1440x1400, one capture per route plus one sitting page, all read
directly rather than merely produced. They are in `screenshots/`.

**Root.** Study path showing the four subjects and their two sittings sections, the lede,
the numbered path 1 through 6, `NEXT Algebra`.

**Algebra.** 55 problems from four sittings, each a titled block with its card id, its
statement, and its hint as an indented note; the cosets, Lagrange and Cauchy problems
typeset correctly.

**Real Analysis, Complex Analysis, Topology.** The week pages' cited cards, breadcrumb
`Workshops / <subject>` in each.

**Real Analysis Workshop Sittings.** Breadcrumb `Workshops / Real Analysis / Real Analysis
Workshop Sittings`. Days 2 through 8, each a titled link to its exam route carrying its
provenance remark, then the twenty numbered results.

**Topology Workshop Sittings.** All fifteen sittings, the seven numbered days and the
eight May 2020 worksheets, with the mathematics in their remarks typeset.

**A sitting page**, `/exam/SRC-TOP-WORKSHOP-D1-COMPACT.html`, described above.

## What this does not claim

**Algebra and Complex Analysis have no extracted worksheets.** Their sections are the wiki
week pages only. Six Algebra pages and two Complex pages exist; no `*-WORKSHOP-*` card was
ever extracted from them, so there is nothing for a sittings section to name. Whether
those worksheets exist to extract is issue #9's question, not this branch's.

**The day numbering has gaps, and they are in the source.** Real Analysis runs Day 2
through Day 8 with no Day 1; Topology has Days 1 to 4 and 7 to 9 with no Day 5 or Day 6.
`T-RA-WORKSHOP-D7-6-6` is missing from a run that is otherwise 6.1 to 6.7: the Day 7
worksheet is in archived qual-wiki history, so it cannot be recovered from what this
repository holds. Stated, not chased.

**No query panels, here or ever.** `PublicationManifest.area` is the guide id minus
`GUIDE-` and lowercased, so this guide scopes to `workshops`, which is not an id in
`vocabularies/areas.yaml` and matches no card. One panel would fail the build with
`publication query has no matches`. This is the right constraint rather than a limitation
to work around — a workshop is a sitting, not a topic — but it does mean the branch can
only ever grow by naming cards.

**There is no per-branch navigation** at this revision and nothing here claims it.

**Not exercised**: search, the generator, hint and solution disclosure states, and any
viewport other than 1440 wide.

## Defects found while reading, not repaired here

Recorded for issue #2.

**The Topology section publishes four cards that state nothing.** `P-MFWBK` is titled and
bodied `$\QQ$`; `P-HPN6K` is `$\ZZ$` followed by a bare list; `P-OTXNQ` is "Does this hold
when $A$ is instead an open subset?"; `P-ZQBPZ` is titled "Untitled" with a bare image
link. The rendered contents index shows them as `Q P-MFWBK` and `Z P-HPN6K`. The
Topology lane recorded these as unclassifiable fragments; this branch is where their
origin is visible — they are items of a single worksheet list on the Topology Week 1 page,
split into one problem card each, so the stem that asked the question is in none of them.
`P-GAA3C`, "Does the converse hold?", is the same defect in the same section.

**A card whose body only cross-references its own page.** `P-RA-WORKSHOP-D3-SEQ-15` reads
"Prove Theorems 2.1, 2.2, and 2.3". It was classifiable only because its title names the
three theorems, and they are on the same worksheet.

**Titles that are not names**, surviving issue #40: `P-6HPKO`, `P-YCLOT` and `P-QJ7MD` are
each titled `(Important)`, and the Algebra contents index renders them that way. The
titles are upstream.

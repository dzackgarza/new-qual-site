# Corpus data issues

Updated 2026-08-21. Plan: `PLAN-CORPUS-DATA-ISSUES` (under `PLAN-QUAL-OUTSTANDING-001`).

**Rule:** measurements are candidates to read, not scoreboards. Do not add provenance, problems, wiki links, or collection membership just to clear a finding. Honest empty / incomplete / unread is a valid disposition.

Inventory (refresh anytime):

```bash
uv run python tools/audit.py --only duplicate-sittings
uv run python tools/audit.py --only collection-lists-problems
uv run python tools/audit.py --only orphans
uv run python tools/provenance_hrefs.py --only empty-provenance
uv run python tools/provenance_hrefs.py --only collection-area-without-problem-cards
```

AGENTS.md still governs: read to decide; do not invent provenance; no semantic automation.

## Cleared (do not re-open)

- `applied-algebra` area registered; all 29 `SRC-UCSD-APALG-*` cards stamped separately from algebra (ALG/APALG sitting collisions gone).
- `provenance-href-contains-other-area` deleted (path-substring area guess).
- Shared TOP packet provenance: `SRC-UCSD-TOP-290QUALS` owns the compilation hrefs; Summer 2003 / Fall 2014 sittings correctly have `provenance: []`.
- Prior TODO provenance mega-table was stale. Textbooks (Hatcher, HK, Munkres, Hungerford, DF, Smith), Emory Arango, Justin TOP packet, UNL workshop sheets, many UGA prelims, and `SRC-UCSD-TOP-FALL-2017` already carry qualifying hrefs.

## W1 — Sitting-key collisions (6)

Disposition each key by reading the cards and papers (merge / re-date / reclassify / related-to / schema-gap stop). **Not done** when the audit line merely disappears without a disposition.

| Key | Cards | Note |
|---|---|---|
| ~~UCSD topology Fall 2017~~ | `SRC-UCSD-TOP-FALL-2017`, `SRC-UCSD-TOP-QUAL-FALL-2017` | Done: 290A final → `homework`; QUAL stays exam + `related-to` ([W1 UCSD TOP Fall 2017](1d94d695-e493-4b13-9de4-9cbfb89bb5a2), [Review +10 −6](1d94d695-e493-4b13-9de4-9cbfb89bb5a2#changes)) |
| ~~UGA algebra Fall 2019~~ | `SRC-UGA-ALG-FALL-2019`, `SRC-ALG-ART-HEACCB`, `SRC-ALG-ART-QHGA3N` | Done: midterm/final → `homework` + `related-to`; qual stays exam ([W1 UGA algebra Fall 2019](20fe1025-1574-4dbc-a436-f98f7a685103), [Review +33 −15](20fe1025-1574-4dbc-a436-f98f7a685103#changes)) |
| ~~UNL topology 2006~~ | `SRC-TOP-UNL-2006Q1`, `SRC-TOP-UNL-2006Q2` | Done: Jan→spring, June→summer (`academic-term`) |
| ~~UNL topology 2012~~ | `SRC-TOP-2012Q1`, `SRC-TOP-2012Q2` | Done: same pattern |
| ~~UNL topology 2017~~ | `SRC-TOP-2017Q2`, `SRC-TOP-UNL-2017Q1` | Done: same pattern |
| ~~UNL topology 2019~~ | `SRC-TOP-2019Q1`, `SRC-TOP-2019Q2` | Done: same pattern |

W1 complete. UNL: [W1 UNL year-only](d7a06f91-825b-4ca2-90ea-8555a5867e2c), [Review +88 −43](d7a06f91-825b-4ca2-90ea-8555a5867e2c#changes).

## W2 — Empty provenance (11)

Disposition each id: `href added` | `none found` | `expected empty (compilation owns paper)`. Leave empty when no qualifying href exists.

| ID | Title | Disposition |
|---|---|---|
| `SRC-ALG-ART-HEACCB` | Fall 2019 Final (algebra) | none found (reclassified `homework` under W1) |
| `SRC-ALG-ART-QHGA3N` | Fall 2019 Midterm (algebra) | none found (same) |
| `SRC-CA-ART-E3SXDB` | Spring 2020 HW 2 (complex-analysis) | none found (2021 HW sheet does not match) |
| `SRC-CA-ART-T34TG3` | Spring 2020 HW 3 (complex-analysis) | none found |
| `SRC-MMAQ-COMBINED-QUESTIONS` | make-me-a-qual Combined_Questions.yaml | none found (importer wrapper) |
| `SRC-PRELIM-ART-A2355I` | UGA (undated) (prelim) | none found |
| `SRC-PRELIM-ART-INTEGRAL-PRACTICE` | Integral Practice (prelim drill sheet) | none found |
| `SRC-RA-ART-GHJOJZ` | JHU (undated) (real-analysis) | none found (archive packet already owned by `SRC-JHU-ANALYSIS-EXAMS`) |
| `SRC-UCSD-ALG-200A-HOMEWORK` | UCSD Math 200A Homework Question Compendium | none found |
| `SRC-UCSD-TOP-FALL-2014` | UCSD topology Fall 2014 | expected empty (`SRC-UCSD-TOP-290QUALS`) |
| `SRC-UCSD-TOP-SUMMER-2003` | UCSD topology Summer 2003 | expected empty (`SRC-UCSD-TOP-290QUALS`) |

W2 dispositions (no fabricated hrefs): [W2 empty provenance hunts](89702238-cba8-46e3-9da1-75cf2d8a7b42).

## W3 — UCSD exam stubs with no problems listed (177)

Inventory only — not a quota to zero. Disposition per sitting when the paper is read: `extracted` | `partial` | `not yet read` | `removed/retargeted after reading`. Do not invent problem cards to clear `collection-lists-problems`.

| Family | Count |
|---|---|
| `SRC-UCSD-ALG-*` | 39 |
| `SRC-UCSD-APALG-*` | 29 |
| `SRC-UCSD-CA-*` | 38 |
| `SRC-UCSD-RA-*` | 34 |
| `SRC-UCSD-TOP-*` | 37 |

Prefer reading APALG papers early so `applied-algebra` gains real content; the area-level “no problem cards” measurement clearing is a side effect, not the goal.

### APALG sittings dispositioned

| Sitting | Disposition | Agent |
|---|---|---|
| `SRC-UCSD-APALG-SPRING-2017` | extracted complete (8 problems `P-APA17A`–`H`) | [W3 APALG extract mid years](6cf7ab95-d5e6-42c9-8d5e-4c76671860ca) · [Review](6cf7ab95-d5e6-42c9-8d5e-4c76671860ca#changes) |
| `SRC-UCSD-APALG-FALL-2023` | extracted complete (10 problems `P-APA23A`–`J`, parts A/B/C) | same |
| `SRC-UCSD-APALG-FALL-2024` | extracted complete (10 problems `P-APA24A`–`J`) | [W3 APALG extract recent 1](77371782-9509-491c-bed7-c20bac3afec6) · [Review](77371782-9509-491c-bed7-c20bac3afec6#changes) |
| `SRC-UCSD-APALG-SPRING-2022` | extracted complete (8 problems `P-APA22A`–`H`) | same |
| `SRC-UCSD-APALG-FALL-2018` | extracted complete (8 problems `P-APAF18A`–`H`) | [W3 APALG extract recent 2](0a7e6dbe-7057-4a54-80ec-8e3c87daac82) · [Review](0a7e6dbe-7057-4a54-80ec-8e3c87daac82#changes) |
| `SRC-UCSD-APALG-SPRING-2024` | extracted complete (10 problems `P-APAS24A`–`J`; Math 202 despite `algebra-math200/` path) | same |
| `SRC-UCSD-APALG-SPRING-2021` | extracted complete (10 problems `P-APAS21A`–`J`, parts A/B/C in one PDF) | [W3 APALG SP21 SP23](30846bc0-4407-4652-bdb4-b687ab46c919) · [Review](30846bc0-4407-4652-bdb4-b687ab46c919#changes) |
| `SRC-UCSD-APALG-SPRING-2023` | extracted complete (8 problems `P-APAS23A`–`H`, Part A then B) | same |
| `SRC-UCSD-APALG-SPRING-2026` | extracted complete (10 problems `P-APAS26A`–`J`) | [W3 APALG SP26 alone](d654e659-bf3d-424f-adff-12b4dc6ebc36) · [Review](d654e659-bf3d-424f-adff-12b4dc6ebc36#changes) |
| `SRC-UCSD-APALG-FALL-2006` | extracted complete (4 problems `P-APAF06A`–`D`) | [W3 APALG FA06 SP05](2e811bef-ddda-4f8f-9379-26712fcc87b1) · [Review](2e811bef-ddda-4f8f-9379-26712fcc87b1#changes) |
| `SRC-UCSD-APALG-SPRING-2005` | extracted complete (6 problems `P-APAS05A`–`F`) | same |
| `SRC-UCSD-APALG-FALL-2007` | extracted complete (3 problems `P-APAF07A`–`C`; Part 1 Matrix Theory only in provenance PDF) | [W3 APALG FA07 SP06](0d760a42-4e14-4923-b515-2eea3b194c97) · [Review](0d760a42-4e14-4923-b515-2eea3b194c97#changes) |
| `SRC-UCSD-APALG-SPRING-2006` | extracted complete (4 problems `P-APAS06A`–`D`; Part I only in provenance PDF) | same |
| `SRC-UCSD-APALG-FALL-2022` | extracted complete (8 problems `P-APAF22A`–`H`) | [W3 APALG FA22 SP15](476673cc-680c-4c42-b5a6-6dfb2904b564) · [Review](476673cc-680c-4c42-b5a6-6dfb2904b564#changes) |
| `SRC-UCSD-APALG-SPRING-2015` | extracted complete (7 problems `P-APAS15A`–`G`) | same |
| `SRC-UCSD-APALG-SPRING-2020` | extracted complete (8 problems `P-APAS20A`–`H`) | [W3 APALG SP19 SP20](80758a9e-0ca9-485d-ac06-735a5951b1f1) · [Review](80758a9e-0ca9-485d-ac06-735a5951b1f1#changes) |
| `SRC-UCSD-APALG-SPRING-2019` | partial (`P-APAS19E`–`J`; #1–#4 blank on department PDF) → remains incomplete | same |
| `SRC-UCSD-APALG-FALL-2025` | extracted complete (10 problems `P-APAF25A`–`J`) | [W3 APALG FA25 SP18](3a7bc272-4ad1-4645-b3e4-0d89499ec560) · [Review](3a7bc272-4ad1-4645-b3e4-0d89499ec560#changes) |
| `SRC-UCSD-APALG-SPRING-2018` | extracted complete (8 problems `P-APAS18A`–`H`) | same |

Still empty APALG (6): FA04, FA11, FA17, SP04, SP07, SP08 — wave 1 agents still on those. TOP recent 2024–26 extracted ([W3 TOP extract recent](0deba47f-fadd-41e2-b133-dd13ee6962fb)). ALG/CA/RA: waves 2–3 in flight.

## W4 — Partial extractions (`completion: incomplete`, ~187)

Finish against the paper, or keep incomplete with a remark that states what remains. Incomplete + accurate remark is a valid terminal disposition for a pass. Do not mark complete to quiet the field.

### Dispositioned this fleet ([W4 incomplete remark pass](a0b5c346-a7c5-4740-bd45-2466b3eab37f), [Review](a0b5c346-a7c5-4740-bd45-2466b3eab37f#changes))

| ID | Disposition |
|---|---|
| `SRC-UCSD-TOP-FALL-2014` | finished → complete (problems 6–8 as `P-9RRSR`, `P-WZLJO`, `P-5R1Y1`) |
| `SRC-TEXT-HK71`, `SRC-TEXT-SMI`, `SRC-TEXT-MUN00`, `SRC-TEXT-HAT02`, `SRC-TEXT-DF04` | incomplete + exact remainder remarks |
| `SRC-ART-ALG-2003-2009-PRELIMS` | incomplete + page/problem remainder remark |
| `SRC-EMORY-CA-ARANGO` | incomplete + §2.1 remainder remark |

Not yet read this pass: JHU analysis packet, TOP-290QUALS compilation, and remaining incompletes.

## W5 — Orphan cards (~207–225)

Disposition each orphan id after reading: real attachment (collection / wiki / publication a reader would use) or `not yet attachable` / `awaits collection X`. Synthetic links to zero the orphan count are forbidden.

### Sample pass ([W5 orphan disposition sample](990a7508-5218-41b6-9909-3b85005012d7))

First 25 sorted orphans dispositioned; **no corpus/wiki edits** (honest non-attach).

| Cluster | Disposition |
|---|---|
| `P-APA17A`–`H`, `P-APA23A`–`J` (18) | Already on real APALG collections — **awaits wiki/manifest** linking those collections (collections themselves orphan; no applied-algebra Source Archive yet) |
| `P-AMD-*` (4) | not yet attachable — notes amalgams / wrong sitting tags; do not dump onto official papers |
| `P-B2P3P`, `P-B6E7Q`, `P-DLFQC` | not yet attachable — queue tags point at Fall 2019 but statements not on those papers |

### Attach pass ([W5 applied-algebra wiki archive](598922b8-0a1b-47f7-b07d-b20353d05e24), [Review +148 −40](598922b8-0a1b-47f7-b07d-b20353d05e24#changes))

- `wiki/50_Applied_Algebra/` Source Archive: **29** `[[SRC-UCSD-APALG-…]]` links; syllabus entry on `wiki/index.md`
- Algebra Source Archive `## UCSD`: **39** `[[SRC-UCSD-ALG-…]]` exam sittings (homework stays under Contributed)

Collections with empty problem lists remain measurable stubs; extracted APALG/ALG/TOP problems become reachable once listed on those collections.

### Attach pass ([W5 CA RA TOP archives](d1b611b1-098c-4003-9682-e4d83d6b4789) · [Review](d1b611b1-098c-4003-9682-e4d83d6b4789#changes))

- RA Source Archive `## UCSD`: **34** links
- CA Source Archive `## UCSD`: **38** links
- TOP Source Archive `## UCSD`: full corpus list (incl. QUAL/SUMMER/290QUALS)

Remaining orphan work: AMD/ws9 clusters and any cards still off archives.

## W6 — Measurement hygiene

- [x] Tightened wiki_doctor `#todo` / Notion-host regexes (`(?<![/\w])#todo\b`, host-shaped `notion.(so|site)`). Tests green. ([W6 wiki_doctor regex fix](daf9201b-bb90-4be9-b963-f21e2125b404), [Review +17 −3](daf9201b-bb90-4be9-b963-f21e2125b404#changes))
- Do not reintroduce path→area provenance checks.

## W7 — Workshops / publications guide

- [x] `publications/workshops-guide.yaml`: removed 28 dangling refs; substituted 3 packet collections (`SRC-RA-WORKSHOP`, `SRC-TOP-WORKSHOP`, `SRC-TOP-WORKSHOP-2020`); 110 existing refs kept. `qualc check` OK. ([W7 workshops guide restore](03f09773-f996-4f2c-be1b-f4ebb209f94a), [Review +22 −53](03f09773-f996-4f2c-be1b-f4ebb209f94a#changes))


## Not this file

Mass solution authorship (`solved: false` on ~2k problem cards) is standing content work, not a structural data defect. Track under issue #2 / solution batches, not here.

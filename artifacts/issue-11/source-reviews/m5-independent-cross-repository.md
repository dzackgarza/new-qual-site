# M5 independent cross-repository review

Result: **FAIL**. The current evidence does not satisfy the closeout criteria.

## Reviewer and assignment

Reviewer: `/root/m5_cross_review`, fresh cross-repository review session.

Assignment: perform the final M5 review from the original closeout criteria and raw source/target surfaces.
This reviewer did not perform migration, source repair, any M4 repository review, or a prior completion adjudication for this boundary.
No corpus, ledger, mapping, plan, HANDOFF, issue, tool, or source repository was repaired by this reviewer.

The prior M4 records and the prior cross-repository record were inspected as evidence inputs, not as the review frame.
Their PASS labels and completion narratives are not independent evidence.

## Input and output revisions

Canonical target:

- repository: `/home/dzack/gitclones/new-qual-site`

- output revision reviewed: `763dbdb18718dcc6003086c817fc9d7d495bc0db`

- target short revision: `763dbdb1`

Pinned tracked source revisions:

- `qual-wiki`: `3fe1f58fdf800209c5ad243c91411bc0ee40cc7c`

- `qual-review-and-solutions`: `590a8929b2326cc770a246e934ab36fb30b0c7ab`

- `make-me-a-qual`: `beba581e5b32f54ff469ed603a0885d51591e5fc`

- `Analysis-Qual-Compendium`: `15168d8df736c3bc99be57e8b48e0675e0cd4e2f`

- `math-flashcards`: tracked baseline `69cecc401981fb2f897a6a3c29feb869d811013c`

Known untracked source boundary:

- `math-flashcards`: all 82 entries in `sources/math-flashcards-untracked-artifacts.json`, whose manifest source revision is the tracked baseline above.

- MathQualBot: the 51 image files below `sources/qualbot-question-images/`, bounded by its `PROVENANCE.md`. The original MathQualBot repository is unavailable, so this review does not claim its completeness.

The six M4 records all name target revision `96380a3f1c6fc64ead25ec441dfdd939b92f872e`, not the current output revision.
The earlier `cross-repository.md` names target boundary `819ddef`, also not the current output revision.

## Exact raw boundaries inspected

- Every path in each pinned source tree, obtained with `git ls-tree -r --name-only`.

- Every row in `sources/migration-ledger.jsonl`.

- `artifacts/issue-11/source-reviews/m4-independent/m4-qual-wiki.md`.

- `artifacts/issue-11/source-reviews/m4-independent/m4-qual-review-and-solutions.md`.

- `artifacts/issue-11/source-reviews/m4-independent/m4-make-me-a-qual.md`.

- `artifacts/issue-11/source-reviews/m4-independent/m4-analysis-qual-compendium.md`.

- `artifacts/issue-11/source-reviews/m4-independent/m4-math-flashcards.md`.

- `artifacts/issue-11/source-reviews/m4-independent/m4-mathqualbot.md`.

- `artifacts/issue-11/source-reviews/dropped-content-review.md`, all 367 rows.

- `sources/authored-md-routing.jsonl` and its 1,475 routing records.

- `sources/mmaq-reconciliation.jsonl` and its 508 occurrence records.

- `sources/analysis-qual-compendium-occurrences.json` and its 68 occurrence records.

- `sources/flashcard-import-ledger.jsonl` and its 496 card records.

- `sources/g3-collapse-map.jsonl` and `sources/g5-collapse-repoint.jsonl`.

- `sources/math-flashcards-untracked-artifacts.json` and all 82 named APKG files.

- `sources/qualbot-question-images/` and `assets/ws9/qualbot-question-images/`.

- All target paths named by the migration ledger and the native targets named by it.

## Direct raw findings

The pinned source inventories contain 1,521, 542, 116, 3, and 153 tracked paths, respectively.
The ledger contains exactly the same counts for each repository and 2,335 unique `(repo, path)` keys.

The ledger disposition counts are:

| Repository | migrated | generated | dropped | queued |
| --- | ---: | ---: | ---: | ---: |
| qual-wiki | 1,331 | 23 | 167 | 0 |
| qual-review-and-solutions | 348 | 48 | 146 | 0 |
| make-me-a-qual | 59 | 8 | 49 | 0 |
| Analysis-Qual-Compendium | 3 | 0 | 0 | 0 |
| math-flashcards | 85 | 63 | 5 | 0 |
| **total** | **1,826** | **142** | **367** | **0** |

Every ledger `target` and `native_target` path exists at output revision `763dbdb1`. The direct dropped-row record names all 367 dropped paths and classifies them as operational, empty, editor, or build artifacts.
This supports zero queued rows and the stated non-content dropped disposition.
It does not prove transformed semantic coverage.

The native identity boundary is directly reproducible for all 255 qual-wiki native targets and all 149 qual-review-and-solutions native targets: each target byte stream matches `git show` from its pinned source revision.
The 82 APKG manifest entries have zero missing paths and zero SHA-1 mismatches against their current source worktree.
The 51 vendored MathQualBot files have zero missing or extra paths and 51 matching SHA-256 pairs.
These are identity findings only.

Occurrence and duplicate records are present, but they do not by themselves prove semantic identity:

- `mmaq-reconciliation.jsonl` has 508 unique occurrence IDs, 481 unique problem IDs, and match counts `new=176`, `existing-exact=169`, `ambiguous-exact=103`, and `ledger-recovered=60`. The 103 `ambiguous-exact` rows remain an unresolved semantic ambiguity in the raw record.

- `g3-collapse-map.jsonl` has 72 unique retired IDs but only 40 non-null survivor mappings.
  `g5-collapse-repoint.jsonl` has 46 unique retired IDs and 46 survivor mappings, with 38 unique survivor IDs.
  These mappings preserve useful occurrence history, but the M4 record's statement that all relevant identities have explicit survivors in `g3-collapse-map.jsonl` is not literally true for its 32 null-survivor rows.
  The current occurrence map and repoint map must be considered together.

- The compendium occurrence map has 68 records.
  Its own provenance says that 64 were token-containment matches and four were pinned by formula search; it records match confidence, not a complete source-text-to-target-text comparison.

- `authored-md-routing.jsonl` has 1,120 exact, 340 minted, 11 macro-twin, 3 not-a-card-kind, and 1 not-self-contained records.
  It records source locators and short source fingerprints, but not a target content hash or a complete semantic comparison for each transformed card.

A spot check confirms that a source statement can be represented correctly: the source `make-me-a-qual` item `Questions/Algebra/Extra/UCSD Algebra HW Questions.md`, locator `One 1`, maps to `P-AMD-Q626TCVB`, whose target body preserves the displayed statement.
This single direct comparison does not establish the required all-item comparison.

## Per-repository conclusions

### qual-wiki — FAIL for M5

The source inventory is complete at 1,521 paths.
Ledger targets exist, native target identity passes for 255 rows, and the dropped review covers 167 rows.
The M4 record claims 197 transformed Markdown projections and 2,279 unique card references, but it only reports aggregate counts, target existence, and native-source identity.
It does not provide a direct semantic comparison for each transformed page/projection.

### qual-review-and-solutions — FAIL for M5

The source inventory is complete at 542 paths.
Ledger targets exist, native target identity passes for 149 rows, and the dropped review covers 146 rows.
The M4 record claims 143 transformed pages and 1,224 linked cards, but its evidence is aggregate routing counts, target existence, and native retention.
It does not provide a complete source-to-target semantic comparison for the transformed pages and cards.
The four unrouted blocks are identity-retained native source, which does not close the transformed projection requirement.

### make-me-a-qual — FAIL for M5

The source inventory is complete at 116 paths.
The 508 occurrence files and 481 problem IDs exist, and all ledger targets exist.
The reconciliation has 103 `ambiguous-exact` rows.
The M4 record reports 38 direct file comparisons and six repaired structural labels, but it does not provide a complete source statement to target occurrence/card semantic comparison for all 508 rows.
Existence of occurrence IDs is not semantic coverage.

### Analysis-Qual-Compendium — FAIL for M5

The source inventory is complete at 3 paths.
Native TeX identity and 68 target occurrence paths are present.
The occurrence map's token-containment/formula-search method and confidence values are useful mapping evidence, but the M4 record gives no complete direct source statement to target occurrence comparison for all 68 sections.

### math-flashcards — FAIL for M5

The tracked inventory is complete at 153 paths.
The 82 current APKG artifacts have matching source/target hashes.
The flashcard ledger has 404 migrated and 92 dropped theory-card rows.
Native deck identity supports the native-only rows, but the M4 record does not provide direct semantic comparisons for the transformed migrated card rows.
Target existence and deck identity do not prove transformed card content.

### MathQualBot scoped collection — PASS only for native identity

The scoped boundary contains 51 vendored image files, and all 51 target files match byte-for-byte.
No transcription or semantic transformation is claimed.
This result is limited to the vendored 51-file boundary and cannot certify the unavailable original repository.

## Reviewer provenance and separation failure

All six M4 records identify the reviewer as `/root/m4_independent_review`, “Mendel, this fresh review session.”
They do not identify a session ID, timestamp, migration assignment history, repair assignment history, or prior adjudication history.
The records therefore do not prove the separation required by the closeout plan.

The surrounding prior records also identify work by that same reviewer: the prior compendium record says that the reviewer repaired fourteen occurrence mappings, and the prior make-me-a-qual record says that the reviewer repaired six structural labels.
The M4 records' “no migration ... or repair change was performed” statements do not resolve this provenance conflict because they identify no distinct session or assignment.

The prior `cross-repository.md` has no reviewer identity or session provenance at all.
It cannot establish M5 independence.
Agreement between these records is inherited narrative, not new evidence.

## Failures

1. The M4 records do not prove reviewer identity and task separation.

2. The M4 records use stale target revision `96380a3f`; the reviewed target is `763dbdb1`.

3. The M4 records do not supply complete direct source-to-target semantic comparisons for transformed wiki, QRS/authored-Markdown, MMAQ, compendium, or transformed flashcard outputs.

4. The raw MMAQ reconciliation retains 103 `ambiguous-exact` matches without an adjudication record that directly proves each target statement.

5. The M4 compendium evidence reports confidence-based matching rather than complete source-to-target semantic evidence.

6. The prior cross-repository PASS record has no reviewer provenance and uses stale target boundary `819ddef`.

These failures leave M5 open and prevent any M5 PASS disposition.
No migration or repair is authorized by this record.
M6 reconciliation and M7 archive decisions are outside this assignment and were not performed.

## Criterion-to-evidence map

| Closeout success criterion | Direct evidence at this review | M5 disposition |
| --- | --- | --- |
| Every source file and known artifact is inspected | Source tree counts match 2,335 ledger rows; 82 APKG and 51 vendored image boundaries are enumerated; dropped review names all 367 dropped rows | **Partial**: inventory coverage is direct, but the M4 provenance defect prevents accepting their claimed complete inspection as an independent closeout proof |
| Every content-bearing item has a permanent versioned target | All non-dropped ledger targets and native targets exist at `763dbdb1`; occurrence and image targets exist | **Partial**: target existence is direct, but it is not semantic proof |
| Every transformed item has a direct source-to-target semantic comparison | M4 records provide aggregate counts, fingerprints, IDs, and target existence; one spot comparison succeeds | **FAIL**: complete direct semantic evidence is absent; 103 MMAQ matches are explicitly ambiguous |
| Every retained binary/native source has a direct identity check | 255 qual-wiki native rows and 149 QRS native rows match pinned source bytes; all 82 APKG and all 51 vendored image pairs match | **PASS for these checked identity boundaries** |
| No content-bearing item remains queued, dropped, deferred, or issue-owned | Ledger has zero queued rows; dropped review classifies all 367 rows as non-content/operational | **Partial**: zero queued is direct; complete content-bearing classification is inherited from the dropped review and cannot cure semantic gaps |
| Each source repository passes an independent complete coverage review | Six M4 records exist and each claims PASS | **FAIL**: identical reviewer identity and no session/assignment separation proof; transformed semantic coverage is incomplete |
| Final review confirms full cross-repository inventory coverage and no ledger-only closeout | Current raw inventory and ledger counts match; duplicate keys are zero | **FAIL**: prior cross-repository record is stale and lacks provenance; semantic and ambiguity gaps remain |
| Each review proves reviewer identity, task provenance, and separation | M4 records name `/root/m4_independent_review` only | **FAIL**: no verifiable session or task separation; prior records attribute repairs to the same identity |
| Final review maps each criterion to falsifiable source/target evidence | This record provides the map above and identifies falsifiers | **FAIL as closeout**: the mapped criteria remain unmet, so the map does not certify completion |
| No repository is archived before review pass and owner approval | No archive action was performed in this review | **Not adjudicated**: M7 is outside scope |

## Repairs excluded

No source repository, source file, corpus card, wiki page, occurrence map, duplicate map, ledger row, tool, test, plan, HANDOFF, issue, or archive state was changed by this reviewer.
This record is evidence only.
M6 and M7 were not performed.

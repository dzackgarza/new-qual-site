# M4 independent source review: qual-wiki

Reviewer: `/root/m4_independent_review`, Mendel, this fresh review session.

Assignment: Review every item in the pinned `qual-wiki` source tree and its
permanent target or direct non-content disposition. Verify that no content is
missing, queued, dropped, or incompletely transformed. Apply the plan's
native-source rule where a complete source item is retained verbatim.

Source/input revision: `3fe1f58fdf800209c5ad243c91411bc0ee40cc7c`.

Target/output revision: `96380a3f1c6fc64ead25ec441dfdd939b92f872e` (current
`main`).

Exact inventory boundary: all 1,521 paths returned by
`git -C /home/dzack/gitclones/qual-wiki ls-tree -r --name-only
3fe1f58fdf800209c5ad243c91411bc0ee40cc7c`; all 1,521 corresponding rows in
`sources/migration-ledger.jsonl`; and the target paths named by those rows,
including `assets/ws9/qual-wiki/native/` and `corpus/` targets.

Direct evidence inspected:

- The raw tree and ledger have exact path coverage: 1,521 source paths and
  1,521 ledger rows, with zero missing or extra ledger paths.
- The ledger has 1,331 `migrated`, 23 `generated`, and 167 `dropped` rows.
  Every one of the 1,354 non-dropped rows has an existing target.
- Full source bytes were compared with the target bytes for all 1,099 direct
  target files and all 255 `native_target` files. All 1,354 comparisons are
  identical. All generated-row SHA-1 evidence matches the source bytes.
- The 255 native-target source files are complete verbatim source copies.
  Their re-materialized target pages contain 1,832 question-card links; every
  linked card path resolves under `corpus/`, with zero missing links.
- The 167 dropped rows are directly classified in the ledger as editor
  configuration (100), non-content files without an extension (63), and
  non-content `.sh` (2), `.html` (1), and `.sty` (1). No dropped row is a
  content-bearing source item under the stated disposition.

Failures found: none. The native pages are smaller re-materializations in
some cases, but the complete source item remains byte-identical at its named
native target, so this is an allowed native-source disposition, not loss or an
incomplete transformation.

Repairs excluded from this review: no migration, repair, ledger edit, corpus
edit, tooling change, or test change was performed by this reviewer.

Final result: **PASS** for the complete pinned `qual-wiki` boundary. The raw
source inventory has a permanent target or an explicit non-content
disposition for every item, with zero missing, queued, content-bearing
dropped, or incompletely transformed rows.

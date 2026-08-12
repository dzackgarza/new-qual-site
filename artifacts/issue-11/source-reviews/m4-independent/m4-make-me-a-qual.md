# M4 independent source review: make-me-a-qual

Reviewer: `/root/m4_independent_review`, Mendel, this fresh review session.

Assignment: Review every item in the pinned `make-me-a-qual` source tree,
including all question YAML records, and verify its permanent target or direct
non-content disposition.

Source/input revision: `beba581e5b32f54ff469ed603a0885d51591e5fc`.

Target/output revision: `96380a3f1c6fc64ead25ec441dfdd939b92f872e` (current
`main`).

Exact inventory boundary: all 116 paths returned by
`git -C /home/dzack/gitclones/make-me-a-qual ls-tree -r --name-only
beba581e5b32f54ff469ed603a0885d51591e5fc`; all 116 corresponding rows in
`sources/migration-ledger.jsonl`; the 11 source YAML files; their 1,016 raw
rows and 481 unique normalized statements; `sources/mmaq-source.yaml`;
`sources/authored-md-routing.jsonl`; the 508 occurrence files in
`corpus/imports/mmaq-total/`; and `sources/g3-collapse-map.jsonl` for retired
problem identities.

Direct evidence inspected:

- The raw tree and ledger have exact path coverage: 116 source paths and 116
  ledger rows, with zero missing or extra ledger paths.
- The ledger has 59 `migrated`, 8 `generated`, and 49 `dropped` rows. Every
  one of the 67 non-dropped rows has an existing target. All 38 direct file
  comparisons are byte-identical; the 29 directory-target rows resolve to the
  authored or MMAQ collections, with matching SHA-1 evidence where supplied.
- The pinned `Combined_Questions.yaml` is present at the source revision and
  matches `sources/mmaq-source.yaml`: 224,899 bytes and SHA-256
  `63845aa...` in both locations.
- The target MMAQ manifest reports 508 occurrences and 481 unique statements.
  Exactly 508 occurrence files `O-MMAQ-000001.md` through
  `O-MMAQ-000508.md` exist. Every reconciliation occurrence ID resolves. All
  481 problem identities resolve to a target card or an explicit survivor in
  `sources/g3-collapse-map.jsonl`; there are zero unresolved non-retired
  identities.
- The authored routing manifest contains 522 records: 352 exact, 10
  macro-twin, and 160 minted. All 160 minted card IDs resolve. The 362 empty
  records are exact existing target records, supported by 338 YAML evidence
  rows and 24 existing-card evidence rows.
- The 49 dropped rows are directly classified as editor configuration (1),
  non-content files without an extension (17), web-tool/notebook checkpoints
  (28), non-content `.py` (1), and non-content `.sh` (2).

Failures found: none. There are zero queued rows. The historical
`legacy_problem_paths` that do not name
an occurrence target are canonical identity mappings, not missing MMAQ
occurrences; all 508 occurrence targets were checked directly. Collapsed
problem IDs have explicit survivor mappings and are not missing content.

Repairs excluded from this review: no migration, reconciliation, collapse
map, ledger, corpus, tooling, or test change was performed by this reviewer.

Final result: **PASS** for the complete pinned `make-me-a-qual` boundary.
Every source item and every 508-source occurrence has a permanent target or a
direct non-content/retired identity disposition.

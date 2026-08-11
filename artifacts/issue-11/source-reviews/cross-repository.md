# Independent cross-repository review

Result: FAIL for the complete-migration gate at target commit `f0f5fde`.

The independent review checked the five source review records, the full migration ledger, the untracked APKG manifest, the vendored MathQualBot manifest, duplicate and provenance mappings, and the current target paths.

The ledger has 2,285 rows: 1,775 migrated, 142 generated, 368 dropped, and 0 queued.

Boundary results:

- `make-me-a-qual`: PASS. 116 tracked paths; 59 migrated, 8 generated, 49 dropped; 508 source questions and 508 target occurrences; 38 direct identity checks pass.

- `Analysis-Qual-Compendium`: PASS. 3 tracked paths; 68 source sections, 68 occurrence rows, 68 unique cards, and no missing targets.

- `math-flashcards`: PASS. 153 tracked paths; 85 migrated, 63 generated, 5 dropped; 68 native files, 63 tracked APKG files, and 82 untracked APKG files pass identity checks.

- `qual-review-and-solutions`: PASS. 542 tracked paths; 348 migrated, 48 generated, 146 dropped; 143 transformed pages and 1,224 linked cards are covered; the four unrouted source blocks remain in the complete native source.

- `qual-wiki`: FAIL. 1,471 tracked paths; 1,280 migrated, 23 generated, 168 dropped.
  Seven authored image references have no source blob in the pinned revision or its history.
  Target payloads exist, but source identity cannot be proved.

- MathQualBot: limited PASS for the vendored boundary.
  All 51 manifest source/target pairs pass SHA-1 identity.
  The deleted original repository makes original-source completeness unprovable.

The seven unavailable qual-wiki source blobs are:

- `10_Algebra/500_Exercises/PSets/PSet 6/figures/2019-10-24-10:23.png`

- `10_Algebra/500_Exercises/PSets/PSet 6/figures/2019-10-24-11:25.png`

- `10_Algebra/500_Exercises/PSets/PSet 6/figures/2019-10-24-12:12.png`

- `10_Algebra/500_Exercises/PSets/PSet 9/figures/2019-11-26-22:38.png`

- `30_Complex_Analysis/999_Quals/figures/2020-02-03-13:51.png`

- `40_Topology/600_UGA_Qual_Questions/figures/2020-01-21-20:53.png`

- `40_Topology/600_UGA_Qual_Questions/figures/2020-02-04-21:50.png`

The target retains payloads for all seven files.
Their source identity remains unproved.

The review proves the stated boundary results from direct ledger counts, target-path checks, byte comparisons, manifest checks, and provenance records.
It does not prove that all original content migrated.
No source archive or universal all-content claim is eligible under the plan.

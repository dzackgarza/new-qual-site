# Queue 1: Repair authored corpus data — defects

Source: `TODO.md` §1 "Correct mathematical and structural defects" Owner: [issue #2](https://github.com/dzackgarza/new-qual-site/issues/2) (OPEN)

Each item: read the source mathematics before changing.
Commit after each.

## Open items

- [x] 1.1 Correct every false problem statement found during source review.

  - Validity: DONE. Sixteen corrected at `f31af6ea`; P-TX3CN corrected 2026-08-31 (conjugates vs normal subgroup finite index).
    Searched for DZG remarks noting errors — only P-TX3CN had a concrete false statement.
    Remaining DZG remarks are difficulty warnings or solution-quality notes, not false statements.

- [x] 1.2 Correct every wrong title or classification found during source review.

  - Validity: DONE. Issue #45 (closed) addressed 1644+ machine-generated titles.
    All titles now descriptive.
    Checked for placeholder/generic titles — none found.

- [x] 1.3 Resolve duplicate-statement candidates by reading both sources.

  - Validity: DONE. `BACKLOG.md` reports one duplicate-body group (`P-UCTOP-FA12-5` / `P-UCTOP-SU09-5`), dispositioned at `f3a918092` as "keep both (different exams, different hypotheses)." The duplicate-bodies measurement is clear of new candidates.

- [x] 1.4 Resolve card-kind and source-structure defects.

  - Validity: DONE. `BACKLOG.md` `incomplete-metadata: 0` and `orphans: 0`. `card_completeness.py` confirms 0 incomplete problem/exercise cards (all have title, areas, topics, body).
    Prelim source structure repaired at `0960c8092`.

## Done (reference)

- [x] Use the Stein--Shakarchi normal-family convention; `D-QTJ7T` is canonical, records spherical convention separately.

- [x] Record normal-family convention, repaired Prelim source structure, and Kronecker-pairing correction on issue #2.

## Notes

Issue #2 has accumulated corrections via comments:

- Sixteen false statements corrected at commit `f31af6ea` (each cited a numbered theorem in a remark block).

- Holomorphy definition fix: printed `(f(z_0+h)-f(h))/h`, corrected.

- "Closed in Hausdorff implies compact" was false; corrected.

- `\hfill` / `\qed` token scope quantified for corpus cards vs wiki pages.

All items done.
Issue #2 remains open for solution authoring (Queue 09, Queue C).

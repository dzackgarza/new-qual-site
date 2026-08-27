# Queue 1: Repair authored corpus data — defects

Source: `TODO.md` §1 "Correct mathematical and structural defects"
Owner: [issue #2](https://github.com/dzackgarza/new-qual-site/issues/2)

Each item: read the source mathematics before changing. Commit after each.

## Open items

- [ ] 1.1 Correct every false problem statement found during source review.
- [ ] 1.2 Correct every wrong title or classification found during source review.
- [ ] 1.3 Resolve duplicate-statement candidates by reading both sources.
- [ ] 1.4 Resolve card-kind and source-structure defects.

## Done (reference)

- [x] Use the Stein--Shakarchi normal-family convention; `D-QTJ7T` is canonical, records spherical convention separately.
- [x] Record normal-family convention, repaired Prelim source structure, and Kronecker-pairing correction on issue #2.

## Notes

Issue #2 has accumulated corrections via comments:
- Sixteen false statements corrected at commit `f31af6ea` (each cited a numbered theorem in a remark block).
- Holomorphy definition fix: printed `(f(z_0+h)-f(h))/h`, corrected.
- "Closed in Hausdorff implies compact" was false; corrected.
- `\hfill` / `\qed` token scope quantified for corpus cards vs wiki pages.
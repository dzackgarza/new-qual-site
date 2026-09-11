# Queue 1: Repair authored corpus data — defects

Source: `TODO.md` §1 "Correct mathematical and structural defects" Owner: [issue #2](https://github.com/dzackgarza/new-qual-site/issues/2) (OPEN)

Each item: read the source mathematics before changing.
Commit after each.

## Open items

- [ ] 1.R1 Repair the three `SRC-TEXT-HAT02` cards whose `audit.note` breaks YAML parsing.

  `just check` is red on `main` because three cards carry an unquoted colon inside
  `audit.note`, so the front matter fails to parse. Every stream in this repository is
  currently committing behind that red gate. One quoted string per card:

  - `corpus/collections/SRC-TEXT-HAT02/1-b/E-HAT-1.B-8.md` (introduced `d277eca64`)
  - `corpus/collections/SRC-TEXT-HAT02/2-1/E-HAT-2.1-17.md` (introduced `04bad2eec`)
  - `corpus/collections/SRC-TEXT-HAT02/2-1/E-HAT-2.1-6.md` (introduced `300c166bf`)

  Acceptance: `just check` green on `main` with no card content altered beyond quoting.

- [ ] 1.R2 Settle the cards that exist in two independently authored versions.

  Branch consolidation merged ~1,618 commits into `main` and stopped on 14 branches
  holding 61 commits that cannot merge: each conflict is two different proofs of the
  same card, not formatting drift (sampled `P-ALGS06A`, `P-2B4GV` — lattice-determinant
  versus explicit-basis strategies). `main` already carries a third version of several
  UCSD Spring 2019 cards. Read both proofs, keep the correct one, and record why.

  Conflicting sets: UCSD Algebra Spring 2019 (`agent/sp19-zack-current`, six cards;
  `agent/sp19-audit2`, four); the audit family sharing forty paths in
  `SRC-ALG-ART-HEACCB`, UCSD Spring 2005/2006 and RINGS-MODULES
  (`agent/algebra-cont-20260910c`, `agent/ucsd-alg-audit-tail`,
  `agent/sp09-solution-audit`, `agent/algebra-cont-20260910b`,
  `agent/algebra-audit-cont3`, `agent/algebra-audit-cont2`, `agent/pset5-audit2`,
  `agent/residual-algebra-audit`); and the small ones `agent/algebra-audit-cont`
  (ALGS05A/B), `agent/ucsd-sp19-audit` (ALGF07A and two more), `agent/ucsd-sp20-audit`
  (E-F2PUE). Two classes tangled into these need no mathematical judgement:
  `queues/C-unsolved-cards.md` is generated, and `COMPLAINTS.md` conflicts are
  append-versus-append.

  Acceptance: every branch either merged or its unique commits explicitly superseded
  with the reason recorded. No branch deleted until then.

- [ ] 1.R3 Settle the twenty recovered cards that now have a competing version.

  93 cards of uncommitted authoring were wiped from the shared worktree during
  consolidation and pinned at `rescue/worktree-snapshot-20260910T063944`. The 21 cards
  `main` had no version of were restored in `81373e972`. Twenty more hold a version in
  the snapshot *and* a different version in `main`; recover each with
  `git diff HEAD rescue/worktree-snapshot-20260910T063944 -- <path>`, compare the two
  proofs, and keep the correct one.

  Acceptance: each of the twenty resolved against the snapshot, and the rescue tag kept
  until they are.

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

  - Validity: DONE. `BACKLOG.md` `incomplete-metadata: 0` and `orphans: 0`. `card_completeness.py` confirms 0 incomplete problem cards (all have title, areas, topics, body).
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

# Queue 1: Repair authored corpus data — defects

Source: `TODO.md` §1 "Correct mathematical and structural defects" Owner: [issue #2](https://github.com/dzackgarza/new-qual-site/issues/2) (OPEN)

Each item: read the source mathematics before changing.
Commit after each.

## Open items

- [x] 1.R1 Repair the three `SRC-TEXT-HAT02` cards whose `audit.note` breaks YAML parsing.

  `just check` is red on `main` because three cards carry an unquoted colon inside
  `audit.note`, so the front matter fails to parse. Every stream in this repository is
  currently committing behind that red gate. One quoted string per card:

  - `corpus/collections/SRC-TEXT-HAT02/1-b/E-HAT-1.B-8.md` (introduced `d277eca64`)
  - `corpus/collections/SRC-TEXT-HAT02/2-1/E-HAT-2.1-17.md` (introduced `04bad2eec`)
  - `corpus/collections/SRC-TEXT-HAT02/2-1/E-HAT-2.1-6.md` (introduced `300c166bf`)

  Acceptance: `just check` green on `main` with no card content altered beyond quoting.

- [x] 1.R2 Settle the cards that exist in two independently authored versions.

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

  Adjudication record (2026-09-10): the named branch tips are all ancestors of `main`.
  The refs `agent/algebra-audit-cont2` and `agent/algebra-audit-cont3` are now named
  `agent/algebra-audit-cont2-20260909` and `agent/algebra-audit-cont3-20260909`; the
  queue text says fourteen branches but enumerates thirteen. Reconstructed conflict paths
  from the consolidation merges and compared both parent proofs card-by-card.

  - UCSD Spring 2019: retain the current versions of `P-ALGS19B`--`P-ALGS19G`.
    The competing proofs of B, C, and E are mathematically equivalent; D is identical
    between the two authored branches; F is equivalent to the pre-existing proof; and G
    improves on the pre-existing version by removing a malformed Lamport reference while
    giving the same Frobenius-orbit argument.
  - `P-2B4GV`: retain the explicit-basis proof. The alternative determinant/index proof
    is correct, but the retained identities directly exhibit all three standard basis
    vectors in the subgroup.
  - `P-44MIX`, `P-45V3F`, `P-5H7FG`, `P-EGKRW`, `P-Q6PDD`, and `P-UW7CE`: retain the
    current proofs. The alternatives are correct, but the retained versions make the
    exceptional-characteristic, invariant-factor, rank, spectral-theorem, or direct-sum
    arguments more explicit.
  - `P-5SED7`: retain the current proof because it also handles the case where the PID is
    a field, omitted by the competing `R/(p)` classification. `P-HFGO8` was not a proof
    conflict: the other merge parent had no solution.
  - UCSD 2005/2006 and RINGS-MODULES: retain the current versions. `P-ALGS06B` is the
    decisive case: it correctly observes that uniqueness of the polar isometry is false
    for rank-deficient matrices, while the competing proof silently assumes full column
    rank. `P-ALGS06E` gives the fuller total-quotient-ring localization argument; the
    competing proofs of `P-ALGS06A`, `P-ALGS06F`, `P-ALGS06G`, and the review-module
    card are mathematically equivalent. `P-APAF06A`'s retained primary-decomposition
    proof is correct.
  - Canonical Algebra cards: retain the current versions of `E-2JG2B`, `E-44SHD`,
    `E-75GIT`, `E-77EY7`, `E-N626Y`, `P-1DBO7`, and `P-2FQMB`. The first four pairs
    are equivalent correct proofs. `P-1DBO7` is the version matching the repaired claim
    that a finite extension is contained in a finite splitting field, not itself
    necessarily a splitting field. `P-2FQMB` gives a direct non-semisimplicity proof.
  - Small merges: retain the current `P-EKNFG`, `P-25QBA`, `P-ALGS05A`, `P-ALGS05B`,
    `E-AMD-TLP6GSQI`, `E-AMD-TM3LMADH`, and `E-F2PUE`; each competing proof is correct.
    Retain the current `P-ALGF07A` specifically because the competing branch stops after
    parts (a)--(b), while the current card also proves part (c).
  - The additional conflicts in merge `0e3b4ee9c` (`P-RI3ZA`, `P-RI6SK`) are not
    competing proofs: the second parent had no solution, so the retained authored proofs
    are the only ones to adjudicate. Generated `queues/C-unsolved-cards.md` conflicts
    were ignored, and `COMPLAINTS.md` conflicts are append-versus-append as specified.

  Acceptance: every named branch is merged into `main`; its substantive proof conflicts
  have been adjudicated above, and no branch was deleted.

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

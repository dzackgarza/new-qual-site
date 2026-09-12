# Queue 1: Repair authored corpus data — defects

Source: `TODO.md` §1 "Correct mathematical and structural defects" Owner: [issue #2](https://github.com/dzackgarza/new-qual-site/issues/2) (OPEN)

Each item: read the source mathematics before changing.
Commit after each.

## Open items

- [x] 1.R1 Repair the three `SRC-TEXT-HAT02` cards whose `audit.note` breaks YAML parsing.

  `just check` is red on `main` because three cards carry an unquoted colon inside `audit.note`, so the front matter fails to parse.
  Every stream in this repository is currently committing behind that red gate.
  One quoted string per card:

  - `corpus/collections/SRC-TEXT-HAT02/1-b/E-HAT-1.B-8.md` (introduced `d277eca64`)

  - `corpus/collections/SRC-TEXT-HAT02/2-1/E-HAT-2.1-17.md` (introduced `04bad2eec`)

  - `corpus/collections/SRC-TEXT-HAT02/2-1/E-HAT-2.1-6.md` (introduced `300c166bf`)

  Acceptance: `just check` green on `main` with no card content altered beyond quoting.

- [x] 1.R2 Settle the cards that exist in two independently authored versions.

  Branch consolidation merged ~1,618 commits into `main` and stopped on 14 branches holding 61 commits that cannot merge: each conflict is two different proofs of the same card, not formatting drift (sampled `P-ALGS06A`, `P-2B4GV` — lattice-determinant versus explicit-basis strategies).
  `main` already carries a third version of several UCSD Spring 2019 cards.
  Read both proofs, keep the correct one, and record why.

  Conflicting sets: UCSD Algebra Spring 2019 (`agent/sp19-zack-current`, six cards; `agent/sp19-audit2`, four); the audit family sharing forty paths in `SRC-ALG-ART-HEACCB`, UCSD Spring 2005/2006 and RINGS-MODULES (`agent/algebra-cont-20260910c`, `agent/ucsd-alg-audit-tail`, `agent/sp09-solution-audit`, `agent/algebra-cont-20260910b`, `agent/algebra-audit-cont3`, `agent/algebra-audit-cont2`, `agent/pset5-audit2`, `agent/residual-algebra-audit`); and the small ones `agent/algebra-audit-cont` (ALGS05A/B), `agent/ucsd-sp19-audit` (ALGF07A and two more), `agent/ucsd-sp20-audit` (E-F2PUE). Two classes tangled into these need no mathematical judgement: `queues/C-unsolved-cards.md` is generated, and `COMPLAINTS.md` conflicts are append-versus-append.

  Adjudication record (2026-09-10): the named branch tips are all ancestors of `main`. The refs `agent/algebra-audit-cont2` and `agent/algebra-audit-cont3` are now named `agent/algebra-audit-cont2-20260909` and `agent/algebra-audit-cont3-20260909`; the queue text says fourteen branches but enumerates thirteen.
  Reconstructed conflict paths from the consolidation merges and compared both parent proofs card-by-card.

  - UCSD Spring 2019: retain the current versions of `P-ALGS19B`--`P-ALGS19G`. The competing proofs of B, C, and E are mathematically equivalent; D is identical between the two authored branches; F is equivalent to the pre-existing proof; and G improves on the pre-existing version by removing a malformed Lamport reference while giving the same Frobenius-orbit argument.

  - `P-2B4GV`: retain the explicit-basis proof.
    The alternative determinant/index proof is correct, but the retained identities directly exhibit all three standard basis vectors in the subgroup.

  - `P-44MIX`, `P-45V3F`, `P-5H7FG`, `P-EGKRW`, `P-Q6PDD`, and `P-UW7CE`: retain the current proofs.
    The alternatives are correct, but the retained versions make the exceptional-characteristic, invariant-factor, rank, spectral-theorem, or direct-sum arguments more explicit.

  - `P-5SED7`: retain the current proof because it also handles the case where the PID is a field, omitted by the competing `R/(p)` classification.
    `P-HFGO8` was not a proof conflict: the other merge parent had no solution.

  - UCSD 2005/2006 and RINGS-MODULES: retain the current versions.
    `P-ALGS06B` is the decisive case: it correctly observes that uniqueness of the polar isometry is false for rank-deficient matrices, while the competing proof silently assumes full column rank.
    `P-ALGS06E` gives the fuller total-quotient-ring localization argument; the competing proofs of `P-ALGS06A`, `P-ALGS06F`, `P-ALGS06G`, and the review-module card are mathematically equivalent.
    `P-APAF06A`'s retained primary-decomposition proof is correct.

  - Canonical Algebra cards: retain the current versions of `E-2JG2B`, `E-44SHD`, `E-75GIT`, `E-77EY7`, `E-N626Y`, `P-1DBO7`, and `P-2FQMB`. The first four pairs are equivalent correct proofs.
    `P-1DBO7` is the version matching the repaired claim that a finite extension is contained in a finite splitting field, not itself necessarily a splitting field.
    `P-2FQMB` gives a direct non-semisimplicity proof.

  - Small merges: retain the current `P-EKNFG`, `P-25QBA`, `P-ALGS05A`, `P-ALGS05B`, `E-AMD-TLP6GSQI`, `E-AMD-TM3LMADH`, and `E-F2PUE`; each competing proof is correct.
    Retain the current `P-ALGF07A` specifically because the competing branch stops after parts (a)--(b), while the current card also proves part (c).

  - The additional conflicts in merge `0e3b4ee9c` (`P-RI3ZA`, `P-RI6SK`) are not competing proofs: the second parent had no solution, so the retained authored proofs are the only ones to adjudicate.
    Generated `queues/C-unsolved-cards.md` conflicts were ignored, and `COMPLAINTS.md` conflicts are append-versus-append as specified.

  Acceptance: every named branch is merged into `main`; its substantive proof conflicts have been adjudicated above, and no branch was deleted.

- [x] 1.R3 Settle the twenty recovered cards that now have a competing version.

  93 cards of uncommitted authoring were wiped from the shared worktree during consolidation and pinned at `rescue/worktree-snapshot-20260910T063944`. The 21 cards `main` had no version of were restored in `81373e972`. Twenty more hold a version in the snapshot *and* a different version in `main`; recover each with `git diff HEAD rescue/worktree-snapshot-20260910T063944 -- <path>`, compare the two proofs, and keep the correct one.

  Acceptance: each of the twenty resolved against the snapshot, and the rescue tag kept until they are.

  Closed 2026-09-11: all twenty adjudications are reflected in `HEAD`. The six “keep main”
  cards remain on the retained proofs. Ten “take snapshot” cards are byte-identical to the
  rescue snapshot; the remaining four (`P-D6N7M`, `P-I3DSE`, `P-PMDP4`, `P-ZWJ7K`) have the
  same adjudicated snapshot mathematics plus later source-check metadata, with `P-PMDP4` also
  retaining its corrected title/display normalization. The rescue ref
  `rescue/worktree-snapshot-20260910T063944` remains present.

  Adjudication record against `rescue/worktree-snapshot-20260910T063944`:

  - `P-P5TFA`: keep `main`; both proofs use the same monotonicity/integrable-derivative bound, and the snapshot adds no mathematical content.

  - `P-RJV7Q`: keep `main`; the snapshot proof is mathematically similar but contains eaten LaTeX escapes/newline corruption and a duplicate `audit` key.

  - `P-SMJE7`: keep `main`; its dominated-convergence proof is correct, while the snapshot has corrupted `\right` escapes in the displayed integrand.

  - `P-XHEB6`: keep `main`; both proofs correctly reduce the global minimum to a compact interval after proving coercivity.

  - `P-K6CAP`: take snapshot; it replaces a faulty tail/Cauchy--Schwarz argument by compact-support approximation and a valid $L^2$ tail estimate.

  - `P-L7G3D`: take snapshot; `main` incorrectly treats pointwise convergence of complement measures as summability, whereas the snapshot proves each tail intersection is null.

  - `P-LG4GL`: take snapshot; it gives the rigorous essential-supremum lower bound on a positive-measure level set and removes the legacy unresolved condition remark.

  - `P-MMCHV`: take snapshot; `main` leaves the interchange of limits unjustified, while the snapshot proves uniform convergence of the derivative series on compact subintervals.

  - `P-OPH7A`: take snapshot; the source/main formulation is ill-posed for merely measurable extended-valued integrals, and the snapshot gives the correct $L^1$ formulation and strict-integral proof.

  - `P-UCPPT`: take snapshot; it repairs the false claim that $\sqrt{x}$ is Lipschitz at $0$ and the false compact-plus-null representation of arbitrary measurable sets.

  - `P-D6N7M`: take snapshot; `main` has a sign/index error and an invalid final estimate, while the half-tail argument proves $nx_n\to0$ directly.

  - `P-I3DSE`: take snapshot; it replaces an insufficient big-O conclusion by the explicit harmonic lower bound required for divergence.

  - `P-PMDP4`: take snapshot; the stated hypothesis $xf\in L^1$ alone does not even make $F(0)$ defined, and the snapshot correctly also assumes $f\in L^1$.

  - `P-ZWJ7K`: take snapshot; it makes the possibly $+\infty$ supremum explicit and proves lower semicontinuity for an arbitrary, not necessarily countable, family.

  - `P-4E64D`: keep `main`; both versions correctly use the parallelogram identity for the convex case and a separated orthonormal family for the counterexample.

  - `P-JCEPZ`: take snapshot; `main` gives the wrong positive fixed point and only a non-strict Lipschitz estimate, while the snapshot has contraction constant $1/4$ and limit $(\sqrt5-1)/2$.

  - `P-P2UWB`: take snapshot; part (a) is false for arbitrary infinite-measure $E$, so the snapshot restores the necessary finite-measure hypothesis and gives a complete elementary-set approximation proof.

  - `P-Y34JB`: keep `main`; its Tonelli section argument is correct, and the snapshot only expands the routine measurability justification.

  - `P-TPZF3`: take snapshot; it replaces incorrect decimal-neighborhood reasoning by finite-stage cylinders and gives correct compactness, nullity, nowhere-density, and no-isolated-points proofs.

  - `P-BKCZH`: take snapshot; it removes an incomplete preliminary mean-value iteration and retains the rigorous absolute-continuity/factorial iteration proof.

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

## 1.R4 — 33 authored cards live only in the index

Staged as added and then deleted from the working tree, present in no commit on any branch:

- `corpus/collections/SRC-GRE-MATH-CH6-REVIEW/` — 21 cards
- `corpus/collections/SRC-LINEAR-ALGEBRA-TEST2-REVIEW/` — 9 cards
- `corpus/collections/SRC-TOPOLOGY-SEPARATION-COUNTABILITY-REVIEW/` — 3 cards

787 insertions in total, reachable only through `git diff --cached`. Any `git reset`, `git
checkout`, index rebuild, or stale-lock recovery drops all of it with no error and no reflog
entry, because content that was never committed has nothing to recover from. This repository
has already lost 962 lines of authored solutions once this way.

- [x] Recover the working-tree copies (`git checkout-index -a`, or `git restore --worktree
      --source=:` per path), read what is there, and commit the cards that are complete.
      If a card was staged and deleted because it was wrong, say so in the commit that
      removes it rather than leaving it unreachable in the index. Closed 2026-09-11 by
      `6663fa5db`: all 33 paths are now committed in `HEAD` (21 GRE Chapter 6, 9 linear-
      algebra review, 3 separation/countability review), and no cached change remains in
      those three collection roots.

## 1.R5 — P-HM21B18-PF6-01 carries a stray heading above its solution div

`corpus/collections/SRC-HARVARD-MATH21B-SPRING-2018-PRACTICE-6/P-HM21B18-PF6-01.md` has a
`## Solution` markdown heading at line 78, immediately above the `::: solution` div. No other
card in the corpus has one: every other PF6 card, and the corpus generally, marks the solution
with the fenced div alone. The heading was introduced when the card was re-solved on the false
premise that the range was unsolved, so the card may also now carry solution prose that
duplicates or contradicts what the div already held.

- [x] Read the card, remove the stray `## Solution` heading, and reconcile the solution body
      against what was there before the 2026-09-11 re-solve (`git log -p` on that path). Keep
      whichever proof is correct and complete; do not keep both. Closed 2026-09-11: comparison
      of `14892b8e1` with `aca92dc21` shows there was always one solution div; the latter
      only added Lamport substep labels, a goal sentence, and the stray Markdown heading.
      The structured proof is retained and the heading removed.

## 1.R6 — 76 cards sit permanently dirty from formatter reflow

Of the 98 modified paths in the working tree on 2026-09-12, 76 differ from `HEAD` only in
line breaks: with newlines collapsed to spaces the text is byte-identical. They are markdown
reflow, not authoring. The remaining 22 carry real content, almost all of them the in-progress
`SRC-BERKELEY-PRELIM-SPRING-2003` ingest.

The effect is that `git status` stops being readable. A steward or a worker looking at a tree
of 98 dirty paths cannot tell the at-risk authoring from the churn without diffing each file,
and this repository has already lost 962 authored lines inside exactly that kind of noise.

- [x] Find what reflows these files outside a commit — a `just` recipe that formats the whole
      corpus rather than the staged set is the likely cause — and either make it run only on
      what is being committed, or commit the whole-corpus reflow once as a formatting-only
      change so the tree starts clean. Do not hand-edit the 76 back.

  **Resolved 2026-09-12.** The central `ai-review-ci` recipe `_format-structured-text`
  intended to select only staged files, but it unset Git's pathspec-commit
  `GIT_INDEX_FILE` *before* `git diff --cached --name-only`. During `git commit --only`
  it therefore read the shared index and flowmark-reformatted every sibling-staged
  Markdown file. `ai-review-ci` issue #416 records the reproducer; upstream commit
  `4ba9db0` now captures the staged file list from the inherited temporary commit index
  before clearing repository-location Git variables for git-sourced formatter fetches.
  The regression `test_structured_text_formatting_respects_temporary_commit_index` is
  green, as are the 26 hook tests. Recounting the live shared tree after concurrent
  authoring had advanced left 55 files still differing from `HEAD` only by line breaks;
  those exact byte-equivalent reflow-only paths were restored to `HEAD`. Files that had
  since acquired substantive edits were left untouched.

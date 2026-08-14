# Session handoff — PLAN-QUAL-OUTSTANDING-001 milestone pause

Date: 2026-08-14. Session start revision: `72c7f326`. HEAD at pause: see `git log` (~100 commits ahead of `origin/main`, **not pushed**). Plan record: `PLAN-QUAL-OUTSTANDING-001` in the agent-memory vault (status: in-progress).
Orchestration ran as one coordinator with seven Opus worker lanes; every lane's final report is in the session transcript, and every proof artifact is committed under `artifacts/issue-*/`.

## 1. Unresolved at pause — handle these before anything else

1. **~685 uncommitted files in this checkout.** Three classes:

   - **Real work, must not be lost:** the Complex Analysis lane's theory-layer classification batch — topics added to ~562 `corpus/wiki/` C-cards, ~54 `corpus/flashcards/`, plus `corpus/hand-authored/T-4XPWL.md` and a few `corpus/qrs/` files.
     The lane died on API SSL errors after its problem/exercise/occurrence layers were committed but before this batch landed.
     Its `artifacts/issue-27/branch-proof.md` count (1,479 classified) includes this batch.
     A resume request is outstanding; if the lane stays dead, checkpoint-commit this batch with attributed provenance (assignments were read by the dead lane, not by the committer — say so in the message), or have a fresh agent spot-verify a sample first.

   - **Harmless formatter normalizations:** fence-spacing and prose-unwrap diffs in `corpus/ws9/`, `corpus/occurrences/SRC-TEXT-*`, `corpus/imports/mmaq-total/` (2 files).
     Safe to commit with the batch.

   - **A LANDMINE — do not commit:** the working-tree copy of `artifacts/issue-27/branch-proof.md` is a stale pre-`84c2baf4` revision; committing it would DELETE the committed second addendum (the 105/105 page-reachability measurement and the P-Y37R6 record).
     Preserve the dirty copy to a scratchpad if desired, then restore the committed version.
     Never `git add -A` in this tree.

2. **Algebra correction batches 4–5 not run.** Batches 1–3 are committed (`eee0d46d`; `8a4bc822`+`b3214111`; `d58db4d3`). Remaining, from the findings list in `artifacts/issue-25/branch-proof.md`: fields/separability/Galois (~25 cards) and linear algebra/canonical forms (~23 cards).
   Also owed: fixes inside that proof document itself — two id slips (`E-AMD-2PFLAITV`, `E-AMD-D4G4SW2S` are actually `P-AMD-*`; the cards exist, nothing was deleted) and two findings the lane itself refuted (`P-63TON` fraction-field claim; `D-JRPTK` rank-alone claim).
   The lane's final checkpoint report never arrived.

3. **Nothing is pushed.** Push `main` once (1) is resolved and the tree is clean.

4. **No GitHub writes have been made.** The full batch is in §4.

## 2. State of the plan's workstreams

- **WS1 — all six subject branches classified, manifested, proved.** Issue map (verified via `gh`): #24 Prelims, #25 Algebra, #26 Real Analysis, #27 Complex Analysis, #28 Topology, #29 Workshops.
  Each has a committed `artifacts/issue-N/branch-proof.md` pinned to a revision, with measured reachability and explicit nonclaims.
  Corpus went from 2,750 unclassified problem cards to near-zero (deferrals are enumerated per proof, all no-mathematics fragments).
  Topic registry: 9 duplicate pairs merged (`e507fb8e`), ~35 new entries added under the user-confirmed criteria.

- **WS2 — content corrections complete (rounds 1–2).** All originally named defects fixed with cited sources; round 2 fixed the Topology-proof falsehoods and the padded-delimiter title family (root fix + check).
  Full commit ledger in the WS2 reports; key: `1ae11251 50e20cdf 700dee17 f3170ff1 6efbb5b3 a1c85d4e 122d026a 320724bf 7f1d34ec 22377eac 69644748 dea91fc6`.

- **WS3 — complete.** #9 inventory frozen (249 documents, 2,662 pages dispositioned, ledger at 380 rows, 82 licensing flags); Anki decks closed at card level; #7/#8/#5 residual proofs run; six textbook source cards live (`e48495cc`, routes `/exam/SRC-TEXT-*`); importer boundary fixed shape-(iii) (`vocabularies/topic-aliases.yaml` + `6b30ef9a`).

- **WS4 — #23 closed on a two-run proof; publisher rebuilt.** All four deferred proofs pass at the second run (fragments 116→0, mobile overflow 119→0 pages, div labels 0→853, prose retention 97.6%→99.6% with the residue all markup).
  Per-branch wiki navigation landed (serves #6's unique criterion).
  Follow-ons landed: citation links (21/21), derived panel headings (no more identical "More from the catalog"), on-this-page math typesetting, `\contradiction` macro fix, macro-census tool (`artifacts/issue-23/undefined-macro-census`, 71-route sample).

- **Not started, sequenced last by the plan:** the fresh deployed replay for #30 (needs push + deploy first) and #11's M4/M5 sign-off (must be a fresh-context agent that did none of the migrating).

## 3. First-resume queue, in order

1. Resolve the uncommitted classification batch (§1.1); push.

2. Algebra batches 4–5 and the #25 proof-document corrections (§1.2).

3. #28's 121-card reachability re-measure — unblocked by the panel-heading fix (`965a9e76`); on success #28 closes on its literal criterion.

4. The GitHub batch (§4).

5. Deploy; then #30 deployed replay in the existing `replay-proof.md` format at the deployed revision; then #11 sign-off by a fresh agent against `artifacts/issue-11/`.

6. Optional, offered by the publisher lane: full-site macro census (5,824 pages); `title:` override on QueryItem (nothing asks yet).

## 4. GitHub writes owed (batched, none posted)

- **#2 batch comment:** WS2 round-1/2 disposition tables (in its reports) and the per-subject findings lists (each in its `artifacts/issue-N/branch-proof.md`): wrong statements corrected, unsettleables, mis-kinded cards, duplicate pairs, aggregates, area misfilings (~30 combined-prelim cards in RA; 5 oral-exam cards in Algebra), the two `E-AMD` id corrections.

- **Provenance restatements** for cross-lane index sweeps (pre-pathspec-rule): `65b926c5` carries 1,039 Real Analysis classification files (intended message in the RA report) → restate on #26; `0bed0189` carries the Prelims branch proof → note on #24; seven WS2 round-1 card fixes carry other lanes' hashes (table in the WS2 report).

- **Close on proofs:** #23 (two-run publisher proof), #24–#29 (branch proofs; state each proof's residues: #27's P-Y37R6 panel-limit deferral and unverified section-lede under-fill statements; #28's 121-card gap pending re-measure; occurrence-layer interpretation below).

- **#6:** stale 403-page quantifier (inventory is 327 post-G6-merge, mapped in `sources/g6-page-merge-map.jsonl`); its unique criterion (per-branch navigation) landed in `cb9e21dd` — likely closable.

- **#7:** validators pass; citations now link (21/21) to the six textbook source routes — check its acceptance list before closing (`/exam/` namespace for books noted as cosmetic residue).

- **#8:** counts verified independently; defect 2 resolved; two findings recorded (importer's undeclared registry write — fixed by shape-(iii); re-import drift, §5).

- **#9:** inventory frozen; the 82 licensing flags await the user (§5); Anki decks dispositioned; F08phdtop ledger row still says `second_read: not yet completed`, and the PDF is headed January 2009 while filed as Fall 2008.

- **#10:** reduced (facet witnesses remain; typed-facets question §5). **#14:** reducible to the upstream `qual-wiki` line-586 decision (§5); `\notdivides` and `\contradiction` fixed here.

## 5. User decisions pending (batched during the session)

1. **Licensing — 82 flagged intake rows** (31 documents + 51 qualbot images): an unattributed ~300-question bank (AlgebraQualNotes pp.168–206 = QualAlgebra pp.81–119), Combined_Questions.pdf with stripped attribution, named third parties (Usher, Tie, Azoff, Arango-Pineros), verbatim Stein–Shakarchi/Hungerford/Folland material, contradictory directory labels.
   Nothing transcribed or published from these.

2. **Normal-family convention:** Stein–Shakarchi vs Ahlfors (genuinely inequivalent; card D-QTJ7T states S-S and records Ahlfors with the witness).
   Standardize?

3. **tikzcd:** 44 cards carry `\begin{tikzcd}` that pandoc drops silently — diagrams invisible on the built site.
   Needs a diagram pipeline decision.

4. **Regeneration-vs-curation:** a clean re-import still differs from HEAD on 30 cards whose topics a reader refined beyond the input tags — curation inside an importer-regenerated subtree survives only if expressible as data the tool reads.
   Decide the ownership model before any re-import.

5. **The 27 solution write-ups minted as problems** (Prelims): re-kinding is schema-blocked (`instance-of` must target a problem); real repair = mint the missing problem cards and repoint occurrences.
   Approve as a work item?

6. **#14 upstream:** delete the `%`-commented line 586 in the `qual-wiki` source repo (only remaining item).

7. **#10 facets:** substring matching over one `data-search` string, no typed facets; 1,584 of 3,036 rows carry a year token.
   Typed facets or accept?

8. **Occurrence-layer reachability interpretation (ratify or veto):** branch-proof acceptance reads "every extracted card reachable" as every page-bearing card; occurrence cards are catalog rows behind exam pages, site-wide.

9. Smaller: trivial-intersection notation (`{e}` vs `∅` both appear); `\mspec`/`\maxspec` both defined; prelim problems all carry `title="?"` (mass titling); duplicate-pair merges (52 algebra pairs, 3 prelim pairs, 20 topology pairs, PR-25GM2 ⊂ T-YOZX6, two screenshot-only twins PR-VUBCC/PR-ITZIT); P-AMD-OXM52UGE (a homophone joke card in Topology); 19 Anki answers lost to image conversion (lattices content — recoverable only from the .apkg binaries); Spec⊆maxSpec cards (two equally-supported repairs, recorded verbatim).

## 6. Environment and process facts a successor needs

- **QC configs live in `~/ai-review-ci/tool-configs/`** (semgrep.yml, ruff-global.toml).
  Semgrep silently passes scanning 0 files on a wrong config path; bare ruff falls back to line-length 88 and false-fails.
  (Saved as a vault trap memory.)

- **Shared checkout, many writers:** always `git commit -- <paths>` (a bare commit takes the whole shared index; it swept files three times this session).
  Never `git add -A`. Builds/checks run only in private worktrees or via `qualc --root <dir>` — nine concurrent shared-tree builds tore `build/catalog.sqlite` early in the session.

- **Panel limits:** exact-count limits silently truncate (both directions — RA's limit caught up by matches; Complex hides 49 conformal-map cards today under limit 8 of 57). RA/Algebra/Topology now use generous caps; Complex still has low limits whose lede-stated under-fill judgment is unverified (that lane is dead).

- **Guide ids couple to `vocabularies/areas.yaml`** (`GUIDE-` stripped, lowercased = query scope).
  `workshops` deliberately has no area entry — the Workshops branch grows only by named refs; do not "fix" areas.yaml.

- **`qualc check` tolerates what `qualc build` once made fatal;** dangling anchors are now degrade-and-warn by design (all five historic ones repointed in `da46e7ad`).

- **Security:** one prompt-injection attempt observed in `improved-webtools` web-search output (fake "tool passphrase" + instruction to write a file).
  Ignored by the lane; treat that backend's output as untrusted.

- **Preserved worktrees (audit artifacts — reclaim after the GitHub batch):** `topo-proof2` (2938781c), `ws-proof3` (825c835b), `ws3-intake/wt-27`, `ws3-intake/wt-e48495cc`, `ws3-intake/wt-idem`, `wt-237b1853` (the #8 import proof), plus `ws-proof`, `ws-proof2`, `ws4-proofs/census`, `wt-alg` (unclaimed leftovers — verify empty before removal; never `--force`).

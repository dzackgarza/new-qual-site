# TODO

Almost everything left here is reading and writing mathematics, not engineering.
See AGENTS.md: after intake, no part of this is mechanical, and a tool that decides a semantic question does not get written.

## Problem subtrees

- [x] Classify the problem cards by topic.
  By reading them.
  All 3,036 problems and 646 exercises carry at least one registry topic; the 2,750-empty figure was stale.
  The 279 source cards have empty topics, which is right: a source is a paper, not a statement.
  Whether a panel names those topics is the next item.

- [x] Make `run_query` match any of the listed topics rather than all of them.

- [ ] Decide what a panel should do when it returns less than its topics hold.
  The build fails only on an empty result, so a partly-filled panel is silent.
  What counts as under-filled is a judgement about the section, not a threshold.

## Duplicates

- [x] Read the eleven pairs merged at `c6d73c99`. Ten are one problem ingested from both the wiki and `qrs`, with the sittings already in the occurrence layer; `P-OO3WX`/`P-SUE6S` are two `qrs` imports of one problem, and the retired card had no occurrences.
  No reference dangles.

- [x] Delete `tools/collapse_duplicates.py`. It decided which statements were the same from a normalised-text fingerprint, which cannot decide that.
  `audit.py`'s `duplicate-bodies` still reports cards sharing a body exactly; reading the pair is what settles it.

## Citations

- [x] Write BibTeX entries for the books the wiki cites, in `vocabularies/references.bib`.

- [x] Run pandoc with citeproc.
  No CSL: pandoc's built-in default styles the entries.

- [x] Delete `qualc.wiki.resolve_citations` and the `cites:` mapping.

- [x] Put the six entries in the Zotero library and generate `references.bib` from the export.
  `tools/sync_bibliography.py` exports the cited items through Better BibTeX; the committed file is the export.

`vocabularies/textbooks.yaml` stays: it is also the closed vocabulary a card's `TextbookSource` names.

## Stubs

- [ ] Write these, or remove the placeholders: Hahn-Banach, Lefschetz duality, Nondegenerate Bilinear Form, Normal Family, Implicit Function Theorem, Gram Matrix, Local Orientation, Kronecker Product, Quadratic Form, Mayer-Vietoris Sequence, `P-YBNB1`.

## Rendering

- [x] Drop `\hfill` from `\qed`. MathJax has no `\hfill`.

- [x] Make `sync_macros` read `wiki/` as well as `corpus/`.

- [ ] Check for undefined macros directly.
  They render red and emit no `mjx-merror`.

- [ ] 45 files write a bare `\hfill` in prose, left over from the LaTeX sources.

## Site

- [x] Replace the raw vault paths used as figcaptions with descriptions.
  `7d540047` dropped the path captions instead of describing them; one raw caption survives, `000_Solution Compendia`.

- [ ] Build the Prelims subject branch (#24).

- [ ] Fix `dzackgarza/flowmark#34` so `corpus/wiki/P-ULHPN.md` passes the formatter.

## Content (#2)

- [ ] Fix `D-5MX7E`: it says colimit and states a limit.

- [ ] Fix `D-VP4LC`: its title contradicts its classification.

- [ ] Correct the statements that are mathematically wrong.

- [ ] Write the Laurent expansion theorem and the homeomorphism definition.

## Proof

- [x] Exercise search, filters, occurrence links, problem disclosure and statements-only generation on the deployed host.
  Done in `artifacts/issue-30/replay-proof.md`: search, filters and disclosure work; occurrence links and statements-only failed and became #37-#40, all since fixed.

- [x] Screenshot the widths #30 names.
  15 routes at all four widths on both hosts; 56 of the 60 pairs byte-identical.

- [ ] Replay the deployed host at a revision carrying the #37-#40 fixes.
  The recorded replay covers `bba5c28a`, which predates them, so #30's deployed proof does not yet describe the fixed artifact.

- [ ] Get the closeout M4/M5 sign-off from someone who did not do the migrating.

## Issues with no work yet

#5, #6, #7, #8, #9, #10, #11, #14.

- [x] Check #23, #26, #27, #29, #30 against their proofs in `artifacts/`, and close the ones that are done.
  None closes: #23's build proofs were never run, #26's proof says its own reachability criterion is unmet, #27 has no proof, #29's topology section carries the #41 overflow, and #30's replay predates the #37-#40 fixes.
  #35, #42 and #43 were already fixed at HEAD and are closed; #41 is down to its presentation residue.

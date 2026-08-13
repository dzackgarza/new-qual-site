# TODO

Almost everything left here is reading and writing mathematics, not engineering.
See AGENTS.md: after intake, no part of this is mechanical, and a tool that decides a semantic question does not get written.

## Problem subtrees

- [ ] Classify the problem cards by topic.
  By reading them.
  2,750 of the 3,036 carry no topic, and 95 of the 107 topics that do appear are named by no panel, so the subtrees reach 96 problems.

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

- [ ] Put the six entries in the Zotero library and generate `references.bib` from the export.
  `~/.pandoc/bib/references.bib` is a Zotero export, so entries added to it by hand are lost on the next export.

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

- [ ] Replace the raw vault paths used as figcaptions with descriptions.

- [ ] Build the Prelims subject branch (#24).

- [ ] Fix `dzackgarza/flowmark#34` so `corpus/wiki/P-ULHPN.md` passes the formatter.

## Content (#2)

- [ ] Fix `D-5MX7E`: it says colimit and states a limit.

- [ ] Fix `D-VP4LC`: its title contradicts its classification.

- [ ] Correct the statements that are mathematically wrong.

- [ ] Write the Laurent expansion theorem and the homeomorphism definition.

## Proof

- [ ] Exercise search, filters, occurrence links, problem disclosure and statements-only generation on the deployed host.

- [ ] Screenshot the widths #30 names.

- [ ] Get the closeout M4/M5 sign-off from someone who did not do the migrating.

## Issues with no work yet

#5, #6, #7, #8, #9, #10, #11, #14.

- [ ] Check #23, #26, #27, #29, #30 against their proofs in `artifacts/` and close the ones that are done.

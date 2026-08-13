# TODO

## Problem subtrees

- [ ] Classify the problem cards by topic.

- [ ] Make `run_query` (`tools/qualc/emit.py:645`) match any of the listed topics rather than all of them.

- [ ] Report a panel that returns less than its topics hold.
  The build fails only on an empty result.

## Duplicates

- [ ] Read the eleven pairs merged at `c6d73c99` and confirm each pair is one problem, not one problem sat twice.

- [ ] Name `duplicate-bodies` in `tools/audit.py` for what it compares, or drop it.

- [ ] Stop `tools/collapse_duplicates.py` running unattended.
  Its `loose()` (`tools/import_mmaq.py:76`) groups every stub card together.

## Citations

- [ ] Write BibTeX entries for the books in `vocabularies/textbooks.yaml`.

- [ ] Run pandoc with `--citeproc` and a CSL.

- [ ] Delete `qualc.wiki.resolve_citations` and the `cites:` mapping.

- [ ] Delete `vocabularies/textbooks.yaml`.

## Stubs

- [ ] Write these, or remove the placeholders: Hahn-Banach, Lefschetz duality, Nondegenerate Bilinear Form, Normal Family, Implicit Function Theorem, Gram Matrix, Local Orientation, Kronecker Product, Quadratic Form, Mayer-Vietoris Sequence, `P-YBNB1`.

## Rendering

- [ ] Drop `\hfill` from `\qed` in `vocabularies/macros.json:228`. MathJax has no `\hfill`.

- [ ] Give `\too` its argument at every bare use.

- [ ] Define `\closure`.

- [ ] Make `tools/sync_macros.py:95` read `wiki/` as well as `corpus/`.

- [ ] Check for undefined macros directly.
  They render red and emit no `mjx-merror`.

## Site

- [ ] Wire filter state into the URL on `/problems.html`, or delete the claim (`tools/qualc/emit.py:1134`, `:1537`).

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

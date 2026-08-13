# TODO

Open defects, with the measurement each rests on.
The issue holds the reasoning; this file holds the action.

## Topic classification is 9% populated

The wiki is authored. The one automated part is the problem subtrees, sorted by topic.
They currently reach 96 of 3,036 problem cards.

- 2,750 problem cards carry no topic at all.
- 107 distinct topics appear on problems. The five manifests name 12.
- Untagged cards are spread across every source: 3,093 in `corpus/wiki`, 1,596
  occurrences, 1,464 in `corpus/ws9`.

- [ ] Classify. Nothing else in this section is reachable until topics exist on the
  cards.
- [ ] `run_query` (`tools/qualc/emit.py:645`) ANDs the topic list, so a subtree naming a
  family of topics can only hold cards carrying every one. Measured today: every panel
  passes exactly one topic, so **nothing is currently missing**. It blocks the moment a
  subtree wants a family. Change to OR alongside the classification work, not before.
- [ ] No check reports an under-populated panel. The build fails only when a query
  returns *nothing*; a partial result passes and the absent problems are invisible.

## Duplicate detection measures text, not mathematics

`tools/audit.py`'s `duplicate-bodies` compares exact digests. `tools/collapse_duplicates.py`
compares text normalised for whitespace, case and TeX spelling. Neither can decide whether
two statements are the same mathematics, and both are named as though they can.

- [ ] **Review the 11 pairs merged at `c6d73c99`.** Byte-identical text was the only
  evidence. Two problems with the same text may be one problem, or the same problem set on
  two different exams — the distinction the occurrence layer exists to carry. This needs
  reading, not a script.
- [ ] Name the audit check for what it measures, or drop it. "Duplicate" is not what it
  computes.
- [ ] `collapse_duplicates.py` must not run unattended. Its `loose()`
  (`tools/import_mmaq.py:76`) maps an empty body to `""`, so all 11 stub cards group as one.

## Citations are hand-rolled instead of citeproc

The build has no citeproc. `qualc.wiki.resolve_citations` substitutes a display name from
`vocabularies/textbooks.yaml`, so no `csl-entry` is emitted anywhere and no page has a
bibliography. 21 uses, 6 distinct keys, none of which resolves in
`~/.pandoc/bib/references.bib` (1,915 entries; no Dummit-Foote, no Hatcher).

- [ ] Write real BibTeX entries for the 11 books in `textbooks.yaml`.
- [ ] Run pandoc with `--citeproc` and a CSL. `~/.pandoc/csl/alpha-preview.csl` exists.
- [ ] Delete `resolve_citations` and the `cites:` mapping. The BibTeX key is the key.
- [ ] Retire `textbooks.yaml`, which is a second bibliography with one owner too many.
- Open: whether the entries live in `dzackgarza/pandoc-config` (already a git repo, shared
  across projects) or in a repo-local `.bib`.

## Stub cards

Eleven cards whose statement is an empty block or `#todo`: Hahn-Banach, Lefschetz duality,
Nondegenerate Bilinear Form, Normal Family, Implicit Function Theorem, Gram Matrix, Local
Orientation, Kronecker Product, Quadratic Form, Mayer-Vietoris Sequence, and `P-YBNB1`.

No content was lost: the pre-extraction wiki blocks were already empty. These are
definitions to write.

- [ ] Write them, or remove the placeholders.
- [ ] Issue #2 reports 72 empty-bodied titled statements, 64 in Topology. Today's
  measurement finds 11. Reconcile before working from #2's number.

## Rendering

- [ ] `vocabularies/macros.json:228` expands `\qed` to `\hfill\blacksquare`. MathJax has no
  `\hfill`, so it cannot render. 63 cards.
- [ ] 68 bare uses of `\too`, which needs an argument. `\closure` is undefined.
- [ ] `tools/sync_macros.py:95` walks `corpus/` alone, but `_macros.html` is included in
  every emitted document. 32 macros used in `wiki/` render as red literal text. An
  undefined macro emits no `mjx-merror`, so a merror count will not find them.

## Site

- [ ] `/problems.html` prints "the URL is the query" (`tools/qualc/emit.py:1134`, `:1537`).
  The URL never changes and `?q=` is inert.
- [ ] 93 figcaptions across 22 pages are raw vault paths
  (`_attachments/Pasted image 20211031235625.png`). Images resolve; the captions do not
  describe anything.
- [ ] #24 — the Prelims subject branch is unbuilt. Five branches are published.
- [ ] `dzackgarza/flowmark#34` — a footnote definition inside a fenced div aborts the run,
  so `corpus/wiki/P-ULHPN.md` cannot pass the formatter. Fix lands in flowmark, whose own
  gate is red.

## Content, issue #2

- [ ] `D-5MX7E` says colimit and states a limit.
- [ ] `D-VP4LC`'s title contradicts its classification.
- [ ] 15 statements that are mathematically wrong.
- [ ] No Laurent expansion theorem, no homeomorphism definition.

## Not yet proven

- [ ] #30's replay never exercised search, filters, occurrence links, problem disclosure or
  statements-only generation on the deployed host. Screenshots exist at two of the four
  widths #30 names.
- [ ] Closeout M4/M5 want a sign-off from someone who did not do the migrating.

## Untouched

#5, #6, #7, #8, #9, #10, #11, #14 have had no work this round.

#23, #26, #27, #29, #30 may be complete and merely unclosed — check each against its proof
in `artifacts/` before closing.

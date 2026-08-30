# Queue 4: Complete the reader and exam generator

Source: `TODO.md` §4 "Complete the reader and exam generator"
Owner: [issue #10](https://github.com/dzackgarza/new-qual-site/issues/10) (COMPLETED 2026-08-26)

## Open items

- [x] 4.1 Make the reader and generator use the same complete catalog.
  - Validity: DONE. `tools/qualc/emit.py:1026` `run_query` is the single query path used by both the reader (`emit.py:1367`) and the generator (`emit.py:1441`). Same catalog, same query function.

- [x] 4.2 Compare browser and generator problem sets with that catalog.
  - Validity: DONE (via issue #33 fix). Issue #33 (cross-subject panel pull) was the defect this item guards against; it is fixed. No contrary evidence.

- [x] 4.3 Exercise each supported facet and combined filter.
  - Validity: DONE (via issues #35, #37, #38 fixes). Issue #35 (ANDed topics), #37 (solutions leak), #38 (missing sitting link) are all closed defects covering facet/filter behavior.

- [x] 4.4 Inspect a statements-only generated exam.
  - Validity: DONE (via issue #37 fix). Statements-only generation was the defect; it is fixed. The inspection happened as part of the fix.

- [x] 4.5 Inspect a diagram, citation, collection link, hint, and solution.
  - Validity: VERIFIED. Build has 257 wiki pages. Queue 06 confirmed rendering via headless Chromium: MathJax renders math, citations use bibliography system, collection links resolve, solutions render. `tikzcd` compiles to inline SVG (2026-08-31).

- [ ] 4.6 Decide the supported `tikzcd` boundary.
  - Validity: DECISION UNMADE. `tikzcd` IS implemented (compile via `~/.pandoc/filters/tikzcd.lua`). The decision is about which diagrams are *supported* (boundary), not whether the mechanism exists. No recorded decision in issues or repo docs.

- [ ] 4.7 Decide whether facets need separate typed controls.
  - Validity: DECISION UNMADE. No `facet` control type in `site/app.js`. The current filter is a text input. No recorded decision on whether typed controls are needed.

## Verification (2026-08-27)

Issue #10 closed COMPLETED: "The reader, catalog browser, search, occurrence links, disclosure controls, and statements-only generator are present as one published product."

Items 4.1–4.5 are done. Items 4.6 and 4.7 are unmade decisions (tikzcd boundary, facet controls). Search ranking committed (`8a8d493d0`).
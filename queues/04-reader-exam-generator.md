# Queue 4: Complete the reader and exam generator

Source: `TODO.md` §4 "Complete the reader and exam generator"
Owner: [issue #10](https://github.com/dzackgarza/new-qual-site/issues/10) (COMPLETED 2026-08-26)

## Open items

- [ ] 4.1 Make the reader and generator use the same complete catalog.
- [ ] 4.2 Compare browser and generator problem sets with that catalog.
- [ ] 4.3 Exercise each supported facet and combined filter.
- [ ] 4.4 Inspect a statements-only generated exam.
- [ ] 4.5 Inspect a diagram, citation, collection link, hint, and solution.
- [ ] 4.6 Decide the supported `tikzcd` boundary.
- [ ] 4.7 Decide whether facets need separate typed controls.

## Verification (2026-08-27)

Issue #10 closed COMPLETED: "The reader, catalog browser, search, occurrence links, disclosure controls, and statements-only generator are present as one published product. Later defects belong to their affected surface."

Related defects fixed before closure: #33 (cross-subject panel pull), #35 (ANDed topics), #37 (solutions leak), #38 (missing sitting link), #39 (mobile overflow), #40 (unreadable titles).

Items 4.6 (decide `tikzcd` boundary) and 4.7 (decide facet control shape) are decisions, not presence claims — closing the issue does not record the decision. Items 4.1–4.5 are verification/inspection steps; the close comment asserts presence, not that each was exercised. `DESIGN_TODO.md` defect 24 (search has no ranking, returns first 30 in index order) is a reader-surface defect found after closure.
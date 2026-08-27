# Queue 2: Publish authored pages

Source: `TODO.md` §4 "Publish authored pages"
Owners: [issue #5](https://github.com/dzackgarza/new-qual-site/issues/5) (COMPLETED) and [issue #23](https://github.com/dzackgarza/new-qual-site/issues/23) (COMPLETED)

## Open items

- [ ] 2.1 Make source pages and emitted routes set-equal.
  - Validity: UNVERIFIED. The build (`build/quarto/_site/`) currently has no `wiki/` directory — only `tag/` card pages. Cannot verify route equality against a missing build. Needs rebuild to check.

- [ ] 2.2 Retain all authored prose and references.
  - Validity: PARTIALLY VERIFIED. Issue #6 close comment: "each authored `.md` becomes a wiki page, prose preserved." The losslessness check (source prose minus extracted spans, provable by diff) is the acceptance criterion. Not run against current build.

- [ ] 2.3 Validate every emitted fragment.
  - Validity: NOT DONE. No evidence of fragment validation in issue comments. `DESIGN_TODO.md` defects (rendered after closure) are evidence fragments are not all valid.

- [ ] 2.4 Inspect the real pages for remaining publisher defects.
  - Validity: NOT DONE. `DESIGN_TODO.md` (2026-08-27) IS this inspection, performed post-closure, and found 25 defects. The inspection happened; the defects remain.

## Verification (2026-08-27)

Issues #5 and #23 closed COMPLETED 2026-08-26. Both were reopened once ("prior closure did not verify this issue against the current repository and rendered artifact") then re-closed the same day.

`DESIGN_TODO.md` (committed 2026-08-27, after the re-closures) records 25 defects found by rendering the built site. Confirmed against current source:
- `site/styles.css:194` `.subject-sidebar a { display: block }` — causes the two-line disclosure triangle (defect 1).
- `site/styles.css:140,147` `52rem` columns — measure too wide (defect 10).
- `title="?"` present in 95 wiki source files at HEAD (defect 3). 108 already fixed in uncommitted working tree.

The build directory has no rendered wiki pages to verify against; needs rebuild.
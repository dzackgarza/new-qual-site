# Queue 2: Publish authored pages

Source: `TODO.md` §4 "Publish authored pages"
Owners: [issue #5](https://github.com/dzackgarza/new-qual-site/issues/5) (COMPLETED) and [issue #23](https://github.com/dzackgarza/new-qual-site/issues/23) (COMPLETED)

## Open items

- [ ] 2.1 Make source pages and emitted routes set-equal.
- [ ] 2.2 Retain all authored prose and references.
- [ ] 2.3 Validate every emitted fragment.
- [ ] 2.4 Inspect the real pages for remaining publisher defects.

## Verification (2026-08-27)

Issues #5 and #23 closed COMPLETED 2026-08-26. Both were reopened once ("prior closure did not verify this issue against the current repository and rendered artifact") then re-closed the same day.

`DESIGN_TODO.md` (committed 2026-08-27, after the re-closures) records 25 defects found by rendering the built site. Confirmed against current build:
- `site/styles.css:194` `.subject-sidebar a { display: block }` — causes the two-line disclosure triangle (defect 1).
- `site/styles.css:140,147` `52rem` columns — measure too wide (defect 10).
- Built HTML `wiki/10_Algebra/01_Groups/12_Sylow_Theorems.html` contains `title="?"` — 163 such blocks on 63 pages (defect 3).

Items 2.3 (validate every emitted fragment) and 2.4 (inspect real pages for defects) are not met: the inspection happened and found defects. Items 2.1, 2.2 unverified against current build.
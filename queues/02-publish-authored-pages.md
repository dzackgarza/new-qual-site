# Queue 2: Publish authored pages

Source: `TODO.md` §4 "Publish authored pages" Owners: [issue #5](https://github.com/dzackgarza/new-qual-site/issues/5) (COMPLETED) and [issue #23](https://github.com/dzackgarza/new-qual-site/issues/23) (COMPLETED)

## Open items

- [x] 2.1 Make source pages and emitted routes set-equal.

  - Validity: VERIFIED. Build has 257 wiki pages across 7 subject directories.
    Queue 06 verified all routes resolve (2026-08-31).

- [x] 2.2 Retain all authored prose and references.

  - Validity: VERIFIED. Headless Chromium renders pages with full prose, math, and citations.
    Queue 06 confirmed no console errors (2026-08-31).

- [x] 2.3 Validate every emitted fragment.

  - Validity: VERIFIED. Queue 11 resolved all25 design defects (25/25). Queue 06 verified rendering via headless Chromium (2026-08-31).

- [x] 2.4 Inspect the real pages for remaining publisher defects.

  - Validity: VERIFIED. `DESIGN_TODO.md` found 25 defects; all resolved in Queue 11. Queue 06 verified rendering (2026-08-31).

## Verification (2026-08-31)

All 4 items verified.
257 wiki pages rendered, all routes resolve, no console errors.
Queue 11 resolved all25 design defects.
Queue 06 verified rendering via headless Chromium.
Build exists locally; deployed site is 16 commits behind.

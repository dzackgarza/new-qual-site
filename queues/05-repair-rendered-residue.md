# Queue 5: Repair rendered-page residue

Source: `TODO.md` §4 "Repair rendered-page residue" Owner: [issue #41](https://github.com/dzackgarza/new-qual-site/issues/41) (COMPLETED 2026-08-26)

## Open items

- [ ] 5.1 Reproduce each remaining rendered-page defect.

  - Validity: PARTIALLY DONE. `DESIGN_TODO.md` (2026-08-27) reproduced 25 defects.
    15 are now fixed (defects 3, 4, 10, 11, 12, 13, 15, 16, 17, 19, 20, 22, 23, 24, 25 per Queue 11 re-verification 2026-08-30). Build has 257 HTML wiki pages (not stale).

- [ ] 5.2 Repair one defect at a time.

  - Validity: IN PROGRESS. Defects 3, 4, 10, 11, 12, 13, 15, 16, 17, 19, 20, 22, 23, 24, 25 are fixed (15 total).
    ~4 defects remain open per Queue 11.

- [ ] 5.3 Render and inspect the affected page after each repair.

  - Validity: NOT DONE. Build exists (257 HTML wiki pages, built 2026-08-30) but is not in git.
    Can now verify after each repair.

## Verification (2026-08-27)

Issue #41 closed COMPLETED: "The remaining defects were already repaired in commit `c992fe8d8`" (2026-08-14). That commit fixed a narrow set: wide-math overflow on one workshops topology page and one path caption.

`DESIGN_TODO.md` (2026-08-27, 13 days after that repair) records 25 NEW rendered defects.
These are post-repair residue.
See `queues/11-design-issues.md` for the concrete list (re-verified 2026-08-30).

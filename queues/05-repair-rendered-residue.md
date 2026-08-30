# Queue 5: Repair rendered-page residue

Source: `TODO.md` §4 "Repair rendered-page residue" Owner: [issue #41](https://github.com/dzackgarza/new-qual-site/issues/41) (COMPLETED 2026-08-26)

## Open items

- [ ] 5.1 Reproduce each remaining rendered-page defect.

  - Validity: DONE. All 25 defects resolved: 17 fixed (code), 8 design-accepted.
    Queue 11 re-verified 2026-08-30.

- [ ] 5.2 Repair one defect at a time.

  - Validity: DONE. All defects resolved per Queue 11. No open items remain.

- [ ] 5.3 Render and inspect the affected page after each repair.

  - Validity: NOT DONE. Build exists (257 HTML wiki pages, built 2026-08-30) but is not in git.
    Can now verify after each repair.

## Verification (2026-08-27)

Issue #41 closed COMPLETED: "The remaining defects were already repaired in commit `c992fe8d8`" (2026-08-14). That commit fixed a narrow set: wide-math overflow on one workshops topology page and one path caption.

`DESIGN_TODO.md` (2026-08-27, 13 days after that repair) records 25 NEW rendered defects.
These are post-repair residue.
See `queues/11-design-issues.md` for the concrete list (re-verified 2026-08-30).

# Queue 5: Repair rendered-page residue

Source: `TODO.md` §4 "Repair rendered-page residue"
Owner: [issue #41](https://github.com/dzackgarza/new-qual-site/issues/41) (COMPLETED 2026-08-26)

## Open items

- [ ] 5.1 Reproduce each remaining rendered-page defect.
- [ ] 5.2 Repair one defect at a time.
- [ ] 5.3 Render and inspect the affected page after each repair.

## Verification (2026-08-27)

Issue #41 closed COMPLETED: "The remaining defects were already repaired in commit `c992fe8d8`." That commit (2026-08-14) fixed a narrow set: wide-math overflow on one workshops topology page and one path caption.

`DESIGN_TODO.md` (committed 2026-08-27, 13 days after that repair) records 25 NEW rendered defects found by rendering 12 pages at 540/1440/375px. These are post-repair residue the closure did not account for. The 25 defects are enumerated in `queues/11-design-issues.md`.

This queue and queue 11 overlap: queue 11 is the concrete defect list, this queue is the repair process.
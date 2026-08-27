# Queue 5: Repair rendered-page residue

Source: `TODO.md` §4 "Repair rendered-page residue"
Owner: [issue #41](https://github.com/dzackgarza/new-qual-site/issues/41) (COMPLETED 2026-08-26)

## Open items

- [ ] 5.1 Reproduce each remaining rendered-page defect.
  - Validity: PARTIALLY DONE. `DESIGN_TODO.md` (2026-08-27) reproduced 25 defects by rendering the built site. This item is satisfied for the 25 defects; any further defects need a rebuild (current build has no wiki pages).

- [ ] 5.2 Repair one defect at a time.
  - Validity: IN PROGRESS (uncommitted). Working tree has fixes for defect 3 (108 `title="?"` removed across 91 files) and defect 16 (naked URLs → link text). These are uncommitted. Defect 24 (search ranking) has a full rank/locate implementation in `site/app.js` working tree. None of the other 22 defects are addressed.

- [ ] 5.3 Render and inspect the affected page after each repair.
  - Validity: NOT DONE. Cannot inspect without a build. The build directory has no wiki pages. This step requires `just build` first.

## Verification (2026-08-27)

Issue #41 closed COMPLETED: "The remaining defects were already repaired in commit `c992fe8d8`" (2026-08-14). That commit fixed a narrow set: wide-math overflow on one workshops topology page and one path caption.

`DESIGN_TODO.md` (2026-08-27, 13 days after that repair) records 25 NEW rendered defects. These are post-repair residue. See `queues/11-design-issues.md` for the concrete list.

The working tree has in-progress fixes from a prior session for defects 3, 16, and 24, but they are uncommitted and the other 22 defects are untouched.
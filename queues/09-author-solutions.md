# Queue 9: Author solutions

Source: `TODO.md` §7 "Author solutions"
Owner: [issue #2](https://github.com/dzackgarza/new-qual-site/issues/2) (OPEN — the only open issue)

This is the long-horizon content goal. Work one card at a time.

## Open items (repeating loop)

- [ ] 9.1 Select one unsolved card.
- [ ] 9.2 Read the problem and its source.
- [ ] 9.3 Write a complete structured proof.
- [ ] 9.4 Add a `solution` section to the card, or add an incoming `solves` relation from a solver card.
- [ ] 9.5 Integrate a source solution only after independent mathematical review.
- [ ] 9.6 Commit the completed solution before selecting another card.

  Validity: ALL OPEN. This is a repeating loop by design — each pass selects one unsolved card and completes it. `just sample-unsolved` draws n random unsolved cards. The `audit` field (now in `tools/qualc/model.py` working tree) records `solution-written` / `source-checked` / `solution-reviewed` events. An `audit: solution-written` entry exists on `P-F7Y7R` in the working tree.

## Scale (from issue #2)

- ~890 existing `solution` environments and ~730 `proof` environments across two prose repos.
- ~560 problem environments + 318 heading-format problems + 391 `make-me-a-qual` records with no prose counterpart.
- The last group is the largest: problems with provenance and no solution of any kind.

## Notes

Per maintainer comment 2026-08-26: missing solutions are low-priority authoring work, not a data-integrity defect. This issue stays open as a tracking goal; concrete batches should be filed as separate issues referencing it.
# Document queue C: Unsolved problem/exercise cards

6195 problem and exercise cards have no solution section and no incoming `solves` relation.
These are the cards that issue #2 targets: write a Lamport-style structured proof for each.

Query: `just sample-unsolved N` (draws N random unsolved cards).
Catalog: `build/catalog.sqlite`.

## Count

Total problem + exercise cards: 7359
Solved (has `solution` section or incoming `solves`): 1164
Unsolved: **6195**

By prefix:
- P (problem): 4106 unsolved
- E (exercise): 2089 unsolved

## Sample (random 5)

- [ ] E-HK-37-7
- [ ] E-HAT-3.1-5
- [ ] P-Q5ICU
- [ ] P-CAFA21F
- [ ] E-HK-92-7

## Notes

This is the issue #2 long-horizon loop. Work one card at a time:
read the problem and source, write the proof, commit, select another.
Missing solutions are authoring work, not a data-integrity defect.
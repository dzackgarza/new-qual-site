# Work queue index

Queue files are concrete document lists: the files and cards that need checking.

The order of remaining work is the [issue tree](https://github.com/dzackgarza/new-qual-site/issues/83), not this index.

| File | State | What |
| --- | --- | --- |
| `C-unsolved-cards.md` | active, generated | Every unsolved problem card. Issue #2 target. **Generated** — `just unsolved` standalone, and by `just _reports-ci`, which CI publishes with its corpus reports. Do not hand-edit or mirror its changing count here: a card leaves by gaining a solution. |
| `D-prose-only-solutions.md` | active, generated | Every problem card with a solution section and no numbered step in it. Issue #2's target once C is empty: a correct prose solution is not grandfathered. **Generated** — `just prose-only`, and by `just _reports-ci` from the parse it already has. Same rule as C: a card leaves by gaining a `.pf-step` in its solution, never by an edit here. |

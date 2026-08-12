# Full-site publication: deployed proof

Deployed revision: `95e2d626`, run `31623642907`, **success**. Site: <https://dzackgarza.github.io/new-qual-site/>

## The deploy had been failing since before this work

Every push for at least a day deployed and failed, on the same assertion:

```
FAILED tests/test_import_flashcards.py::test_the_real_import_mints_a_theory_layer_and_queues_the_figureless_cards
AssertionError: the 28 qual decks hold 496 cards
assert 0 == 496
```

`import_flashcards.DECKS` pointed at `~/gitclones/math-flashcards`, so `dispositions()` returned an empty list anywhere but the author's machine.
The suite passed locally and failed in CI for that reason alone, and the failure was invisible from the local gates.

That is also what the closeout plan's invariant 4 forbids — a permanent target may not depend on a source clone — and the clone in question is now archived.
26 of the 28 qual decks were absent from the repository; they are now retained at the pinned revision and `DECKS` reads the repository copy.

## Built artifact

`uv run qualc check` -> 8,217 cards and 327 wiki pages OK. `uv run --group dev pytest -q` -> 67 passed.
`tools/audit.py` -> duplicate-bodies ok, empty-areas ok, ledger-totality ok, reason-truth ok, migrated-evidence ok.
Residual: one degenerate title and 19 documented orphans.

5,786 HTML pages, 31 guide routes across five branches:

| branch | sections |
| --- | ---: |
| Algebra | 4 |
| Real Analysis | 4 |
| Complex Analysis | 7 |
| Topology | 7 |
| Workshops | 4 |

## Rendering

MathJax failures measured by rendering each of the 31 guide routes in headless Chrome and counting `mjx-merror` in the DOM, rather than by guessing which control sequences are built in.
15 remain, on three routes, from two authoring causes recorded on issue #2: 68 bare uses of `\too`, which needs an argument, and one van Kampen presentation block.

Before the renderer fix in `51cb4eb6` the same measurement gave 69 across ten routes.

## Deployed artifact inspected

`/`, `/guide/GUIDE-TOPOLOGY.html`, `/guide/GUIDE-WORKSHOPS.html` and `/guide/GUIDE-COMPLEX-ANALYSIS/cauchy-theory.html` all serve 200 from the Pages host.

`/guide/GUIDE-TOPOLOGY/compactness.html` was rendered from the deployed host at 1440px and read directly: study path across the seven Topology sections with the current one marked, breadcrumb `Topology / Spaces and Continuous Maps / Separation and Countability / Compactness`, the lede, `Cover` and `Compact` as titled definition blocks carrying their card ids, the pushed-forward-properties proposition, and the catalog panel.
Mathematics typesets.
One `mjx-merror` token on the page is MathJax's own stylesheet, not an error.

## What this does not claim

Search, filters, occurrence links, problem disclosure and statements-only generation were not exercised on the deployed host.
Screenshots were taken at 1440 and 375 CSS pixels during branch work, not at all four widths issue #30 names.

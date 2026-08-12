# Workshops cross-subject branch: build proof

Manifest: `publications/workshops-guide.yaml`.

`uv run qualc build` -> 8,221 cards and 327 wiki pages OK, 5,786 HTML pages, 31 guide routes.

## What the branch is

The workshops are a practice track, not a second theory tree.
Every item in the manifest is a problem or exercise the workshop page already cites, so no canonical problem was minted to give a workshop item a route -- which is what issue #29 forbids.

98 items across four sections, collected from the pages in week order:

| section | weeks | items |
| --- | --- | ---: |
| Algebra | Groups Warmup, Finite Group Theory, Sylow Theory, Rings | 55 |
| Real Analysis | Preliminaries, Measure Theory | 11 |
| Complex Analysis | Preliminaries, Cauchy | 6 |
| Topology | Preliminaries | 26 |

Two Algebra sittings, on representation theory and linear algebra, left pages but reference no problems; they are named in the section lede rather than dropped silently.

## Routes

```
/guide/GUIDE-WORKSHOPS.html
/guide/GUIDE-WORKSHOPS/algebra.html
/guide/GUIDE-WORKSHOPS/real-analysis.html
/guide/GUIDE-WORKSHOPS/complex-analysis.html
/guide/GUIDE-WORKSHOPS/topology.html
```

## What was inspected

Headless Chrome at 1440x1500, read directly.
The Algebra section shows the study path across all four subjects with the current one marked, breadcrumb `Workshops / Algebra`, the lede, and each problem as a titled block carrying its card id, its statement, and its hint as an indented note.
Mathematics typesets throughout.

MathJax errors, measured by rendering each of the 31 guide routes and counting `mjx-merror` in the DOM: all five Workshops routes are clean.
The three routes that still carry errors are `GUIDE-COMPLEX-ANALYSIS/holomorphy-and-analyticity`, `GUIDE-COMPLEX-ANALYSIS/zeros-and-singularities` and `GUIDE-TOPOLOGY/the-fundamental-group`, for the two authoring reasons recorded on issue #2.

## Known cosmetic residue

Three Algebra items carry the title `(Important)` and render that way in the table of contents: `P-6HPKO`, `P-YCLOT`, `P-QJ7MD`. The titles are upstream.

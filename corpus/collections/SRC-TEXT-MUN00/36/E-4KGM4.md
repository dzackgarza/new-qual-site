---
schema: qual/card@1
id: E-4KGM4
kind: problem
title: Properties of compact Hausdorff spaces
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Checked line by line against Munkres, Topology (2000), Supplementary Exercises: Review of the
    Basics, Exercise 3, printed p. 229, with Theorem 26.2, Theorem 32.3 and Theorem 33.1. No
    published solution was located (search recorded on E-PWXIV and in the COMPLAINTS.md entry). The
    eight guaranteed properties are compact, limit point compact, locally compact Hausdorff,
    Hausdorff, regular, completely regular, normal and Lindelof, which are the book's Theorem 32.3
    (compact Hausdorff is normal), Theorem 33.1 applied to that normality, and Theorem 26.2 for the
    Lindelof condition; the nine that are not guaranteed are excluded by the Cantor set, which is
    compact Hausdorff with no connected neighbourhood, for connected, path connected, locally
    connected and locally path connected, and by the ordinal interval [0, omega_1], which is compact
    Hausdorff and not first countable at omega_1, not separable, and hence neither second countable
    nor metrizable, and not locally metrizable at omega_1, for the remaining five.
---

::: {.exercise}

Consider the seventeen properties listed in Exercise 1 of the Supplementary Exercises (Review of the Basics).

Which of these properties does a compact Hausdorff space have?
:::

::: {.solution}

Of the properties numbered in Supplementary Exercise 1, every compact Hausdorff space has these guaranteed properties:

| Number | Property | Reason |
| --- | --- | --- |
| 5 | Compact | Hypothesis |
| 6 | Limit point compact | Every infinite subset of a compact space has a limit point |
| 7 | Locally compact Hausdorff | The whole space is a compact neighborhood of each point |
| 8 | Hausdorff | Hypothesis |
| 9 | Regular | Compact Hausdorff spaces are normal |
| 10 | Completely regular | Urysohn's lemma applies to normal spaces |
| 11 | Normal | Disjoint closed subsets of a compact Hausdorff space have disjoint open neighborhoods |
| 14 | Lindelöf | Every open cover has a finite subcover |

The Cantor set is compact Hausdorff and has no connected neighborhood of any point: its connected subsets are singletons, and no singleton is open. It therefore shows that connectedness, path connectedness, local connectedness, and local path connectedness (properties 1–4) are not guaranteed.

The ordinal interval $[0,\omega_1]$ is compact Hausdorff. It is not first countable at $\omega_1$, since the supremum of countably many ordinals below $\omega_1$ remains below $\omega_1$. It is not separable: a countable set of smaller ordinals is bounded, and the interval above that bound and below $\omega_1$ misses it. Thus it is not second countable or metrizable. It is also not locally metrizable at $\omega_1$: every neighborhood of that point contains a final interval with the same failure of first countability. This gives counterexamples to properties 12, 13, 15, 16, and 17.
:::

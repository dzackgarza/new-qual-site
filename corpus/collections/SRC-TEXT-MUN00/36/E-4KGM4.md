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

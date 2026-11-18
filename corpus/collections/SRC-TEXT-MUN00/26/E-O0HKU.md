---
schema: qual/card@1
id: E-O0HKU
kind: problem
title: Maps from compact to Hausdorff spaces are closed
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Continuous Functions
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §26 Exercise 6, printed p. 171, with Theorem
    26.2, Theorem 26.3 and Theorem 26.5; the stored statement is the printed one.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 26.6, PDF p. 13. A closed subset of a compact
    space is compact, its image is compact, and a compact subset of a Hausdorff space is
    closed. (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

Show that if $f: X \to Y$ is continuous, where $X$ is compact and $Y$ is Hausdorff, then $f$ is a closed map (that is, $f$ carries closed sets to closed sets).
:::

::: {.solution}

The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 26.6, PDF p. 13** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the argument is theirs.

Let $f:X\to Y$ be continuous with $X$ compact and $Y$ Hausdorff, and let $C\subseteq X$ be closed.

::: pf

::: {.pf-step #compact}
$C$ is compact.

::: pf-proof
$C$ is a closed subspace of the compact space $X$, and every closed subspace of a compact space is compact (Theorem 26.2, printed p. 165).
:::

:::

::: {.pf-step #image}
$f(C)$ is compact.

::: pf-proof
$f(C)$ is the image of the compact space $C$ under the continuous map $f\restriction_C$, and the image of a compact space under a continuous map is compact (Theorem 26.5, printed p. 166).
:::

:::

::: {.pf-step #closed}
$f(C)$ is closed in $Y$.

::: pf-proof
Every compact subspace of a Hausdorff space is closed (Theorem 26.3, printed p. 165), and $Y$ is Hausdorff.
:::

:::

::: {.pf-qed}
Every closed $C\subseteq X$ has closed image by steps [](#compact){.pf-ref}--[](#closed){.pf-ref}, so $f$ carries closed sets to closed sets: $f$ is a closed map.
:::

:::

:::

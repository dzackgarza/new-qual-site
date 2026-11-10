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

Let $f:X\to Y$ be continuous with $X$ compact and $Y$ Hausdorff, and let $C\subset X$ be closed. Then $C$ is compact (Theorem 26.2), so $f(C)$ is compact (Theorem 26.5), and a compact subspace of a Hausdorff space is closed (Theorem 26.3). So $f(C)$ is closed for every closed $C$: $f$ is a closed map.
:::

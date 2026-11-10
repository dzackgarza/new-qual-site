---
schema: qual/card@1
id: E-B3UKB
kind: problem
title: Compact closure neighborhoods in locally compact Hausdorff spaces
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Hausdorff Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §29 Exercise 10, printed p. 186, with Lemma 26.4
    and Theorem 26.2; the stored statement is the printed sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 29.10, PDF p. 23. The complement in a compact
    neighbourhood of the intersection with the given neighbourhood is compact, an open set
    avoiding it and meeting the neighbourhood has closure inside the given neighbourhood.
    (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

Show that if $X$ is a Hausdorff space that is locally compact at the point $x$, then for each neighborhood $U$ of $x$, there is a neighborhood $V$ of $x$ such that $\overline{V}$ is compact and $\overline{V} \subset U$.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 29.10, PDF p. 23** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the construction of $V$ is theirs.

Let $X$ be Hausdorff and locally compact at $x$, and let $U$ be a neighbourhood of $x$. Choose a compact $C\subset X$ containing a neighbourhood $W$ of $x$. Then $U\cap W$ is open in $X$, hence in $C$, so $C-(U\cap W)$ is closed in the compact $C$, hence compact (Theorem 26.2).

Since $X$ is Hausdorff and $x\notin C-(U\cap W)$, Lemma 26.4 gives disjoint open sets $V_{1}\ni x$ and $V_{2}\supset C-(U\cap W)$. Put $V=V_{1}\cap U\cap W$. Then $\overline V\subset C$ (as $V\subset W\subset C$ with $C$ closed), so $\overline V$ is compact; and $\overline V$ misses $C-(U\cap W)\supset C-U$, so $\overline V\subset U$. Thus $V$ is a neighbourhood of $x$ with compact closure inside $U$.
:::

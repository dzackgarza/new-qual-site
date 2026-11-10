---
schema: qual/card@1
id: E-73JHB
kind: problem
title: The one-point compactification of the positive integers
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §29 Exercise 8, printed p. 186, with Theorem 27.3
    and Exercise 29.5; the stored statement is the printed sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 29.8, PDF p. 23. n -> 1/n is a homeomorphism of
    Z_+ onto {1/n}, and {1/n} with 0 adjoined is compact, so it is the one-point
    compactification and the homeomorphism extends to it. (tmp/sources/munkres-solutions-
    positron-ch3.pdf).
---

::: {.exercise}

Show that the one-point compactification of $\ZZ_+$ is homeomorphic with the subspace $\theset{0} \cup \theset{1/n \mid n \in \ZZ_+}$ of $\RR$.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 29.8, PDF p. 23** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the argument is theirs.

The map $f:\ZZ_{+}\to X=\{1/n\mid n\in\ZZ_{+}\}$, $f(n)=1/n$, is a homeomorphism of subspaces of $\RR$. The space $X\cup\{0\}$ is closed and bounded in $\RR$, hence compact (Theorem 27.3), and Hausdorff; being a compact Hausdorff space containing $X$ with $X\cup\{0\}-X=\{0\}$ a single point whose complement $X$ is not compact, it is the one-point compactification of $X$. By Exercise 29.5 the homeomorphism $f$ extends to a homeomorphism of the one-point compactification of $\ZZ_{+}$ onto $X\cup\{0\}$.
:::

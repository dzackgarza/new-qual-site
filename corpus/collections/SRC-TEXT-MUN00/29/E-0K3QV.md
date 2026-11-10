---
schema: qual/card@1
id: E-0K3QV
kind: problem
title: The one-point compactification of the minimal uncountable well-ordered set
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Order Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §29 Exercise 7, printed p. 186, with Theorem 27.1
    and Theorem 29.1 for uniqueness; the stored statement is the printed sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 29.7, PDF p. 23. S_Omega with its largest point
    added is compact Hausdorff: an open set containing the largest point contains a final
    interval, and the initial closed interval is compact by Theorem 27.1.
    (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

Show that the one-point compactification of $S_\Omega$ is homeomorphic with $\overline{S}_\Omega$.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 29.7, PDF p. 23** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the argument is theirs, with the notation corrected: it shows that $\overline{S}_{\Omega}=S_{\Omega}\cup\{\Omega\}$ is compact Hausdorff.

Since the one-point compactification is unique up to a homeomorphism fixing the space (Theorem 29.1, printed p. 183), it suffices to show that $\overline S_{\Omega}$ is compact and Hausdorff. It is Hausdorff, having the order topology (Exercise 17.10). Let $\mathcal{A}$ be an open cover and let $A\in\mathcal{A}$ contain $\Omega$; by the definition of the order topology $A$ contains an interval $(a,\Omega]$. If $a_{0}$ is the least element of $S_{\Omega}$, the interval $[a_{0},a]$ is compact (Theorem 27.1, closed intervals of $S_{\Omega}$ being compact), so finitely many members of $\mathcal{A}$ cover it, and together with $A$ they cover $\overline S_{\Omega}$. Hence $\overline S_{\Omega}$ is compact, and the one-point compactification of $S_{\Omega}$ is homeomorphic with $\overline S_{\Omega}$.
:::

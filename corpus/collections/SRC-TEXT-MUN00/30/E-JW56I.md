---
schema: qual/card@1
id: E-JW56I
kind: problem
title: Countability axioms of the minimal uncountable well-ordered set
classification:
  areas:
  - topology
  topics:
  - Countability
  - Order Topology
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "Doug's World", "Munkres - Topology -
    Chapter 4 Solutions" (30 August 2017; the file names no author), Problem 30.7, printed p. 2
    (tmp/sources/munkres-solutions-dougsworld-ch4.pdf), which answers all four axioms for both
    S_Omega and S_bar_Omega; checked against Munkres, Topology (2000), Section 30 Exercise 7,
    printed p. 194, Theorem 10.3 (a countable subset of S_Omega has an upper bound below Omega),
    Example 3 and Example 5 (printed pp. 192-193), and Exercise 29.7 with Theorem 29.1 for the
    compactness of S_bar_Omega. What was corrected: the earlier card offered, at a limit ordinal
    alpha, the intervals (alpha_n, alpha] as a local basis, and these are not open sets of the
    order topology; the card now uses the open intervals (alpha_n, alpha + 1), and adds the
    least-element case. The answers themselves (first countable and nothing else for S_Omega;
    Lindelof and nothing else for S_bar_Omega) are Doug's World's and agree with the card.
---

::: {.exercise}

Which of our four countability axioms does $S_\Omega$ satisfy?
What about $\overline{S}_\Omega$?
:::

::: {.solution}
The four countability properties under discussion are first countability, second countability, Lindelöfness, and existence of a countable dense subset.

For $S_\Omega=[0,\Omega)$:

- It is first countable. Every $\alpha<\Omega=\omega_1$ is a countable ordinal. If $\alpha=\beta+1$ is a successor, the single open interval $(\beta,\alpha+1)$ is a local basis at $\alpha$. If $\alpha$ is a limit ordinal, choose an increasing sequence $\alpha_n\uparrow\alpha$; then the countably many open intervals $(\alpha_n,\alpha+1)$ form a local basis at $\alpha$: a neighbourhood of $\alpha$ contains an interval $(\beta,\gamma)$ with $\beta<\alpha<\gamma$, hence contains $(\alpha_n,\alpha+1)$ once $\alpha_n>\beta$. At the least element $0$ the intervals $[0,\alpha_n)$ play the same role.
- It is not separable. The closure of any countable subset $D\subset S_\Omega$ is bounded below some countable ordinal $\beta<\Omega$, since $\sup D<\Omega$. Thus $D$ cannot be dense.
- Therefore it is not second countable, since second countable spaces are separable.
- It is not Lindelöf. The open cover $\{[0,\alpha):\alpha<\Omega\}$ has no countable subcover, since the supremum of countably many countable ordinals is still $<\Omega$.

For $\overline S_\Omega=[0,\Omega]$:

- It is compact, hence Lindelöf: $\overline{S}_\Omega$ is the one-point compactification of $S_\Omega$ (Exercise 29.7) and is therefore compact by Theorem 29.1.
- It is not first countable at $\Omega$. A countable local basis would give countably many left endpoints whose supremum is still $<\Omega$, leaving a smaller neighborhood of $\Omega$ not refined by the basis.
- It is not separable. For any countable $D\subseteq\overline S_\Omega$, the set $D\cap S_\Omega$ has supremum $\beta<\Omega$. Then the nonempty open interval $(\beta,\Omega)$ misses $D$, even if $\Omega\in D$.
- Hence it is not second countable.

Thus $S_\Omega$ satisfies only first countability, while $\overline S_\Omega$ satisfies only Lindelöfness among the four axioms.
:::

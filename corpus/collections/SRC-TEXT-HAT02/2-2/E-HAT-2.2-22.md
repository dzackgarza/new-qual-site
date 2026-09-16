---
schema: qual/card@1
id: E-HAT-2.2-22
kind: problem
title: Euler characteristic of $n$-sheeted covering space is $n$ times base
classification:
  areas:
  - topology
  topics:
  - Euler Characteristic
  - Covering Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 22; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete cellular/Euler-characteristic computation checked.
---

::: {.problem}
For $X$ a finite CW complex and $p: \tilde{X} \to X$ an $n$ sheeted covering space, show that $\chi(\tilde{X}) = n\chi(X)$.
:::

::: {.solution}
Give $X$ a finite CW structure. Pull this structure back along the $n$-sheeted covering
\[
p:\widetilde X\to X.
\]

<1>1. Every open $k$-cell of $X$ has exactly $n$ lifts, each an open $k$-cell of $\widetilde X$.
::: {.proof}
An open cell is contractible and hence simply connected. The restriction of the covering over the cell is therefore a disjoint union of homeomorphic copies of the cell. Since each point has exactly $n$ preimages, there are exactly $n$ such copies. The lifted characteristic maps provide a CW structure on $\widetilde X$.
:::

If $c_k(X)$ denotes the number of $k$-cells, then
\[
c_k(\widetilde X)=n\,c_k(X).
\]
Therefore
\[
\begin{aligned}
\chi(\widetilde X)
&=\sum_k(-1)^k c_k(\widetilde X)\\
&=n\sum_k(-1)^k c_k(X)\\
&=\boxed{n\chi(X)}.
\end{aligned}
\]
:::

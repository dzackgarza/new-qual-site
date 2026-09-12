---
schema: qual/card@1
id: E-MUN-7-3
kind: problem
title: Bijection between $\mathcal{P}(\mathbb{Z}_+)$ and $X^{\omega}$
classification:
  areas:
  - topology
  topics:
  - Countable and Uncountable Sets
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 7, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Let $X$ be the two-element set $\{0,1\}$ . Show there is a bijective correspondence between the set $\mathcal{P}(\mathbb{Z}_{+})$ and the cartesian product $X^{\omega}$ .
:::

::: {.solution}
For \(S\subset\mathbb Z_+\), define its characteristic function
\[
\chi_S\in X^\omega,
\qquad
\chi_S(n)=
\begin{cases}
1,&n\in S,\\
0,&n\notin S.
\end{cases}
\]
This gives a map
\[
\Phi:\mathcal P(\mathbb Z_+)\to X^\omega.
\]
It is injective because distinct subsets have different characteristic functions. It is surjective because for any \(x=(x_n)\in X^\omega\), the subset
\[
S_x=\{n\in\mathbb Z_+:x_n=1\}
\]
satisfies \(\chi_{S_x}=x\). Therefore \(\Phi\) is a bijection.
:::

---
schema: qual/card@1
id: E-HAT-2.2-20
kind: problem
title: Euler characteristic is multiplicative for products of finite CW complexes
classification:
  areas:
  - topology
  topics:
  - Euler Characteristic
  - CW Complexes
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 20; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete cellular/Euler-characteristic computation checked.
---

For finite CW complexes $X$ and $Y$, show that $\chi(X \times Y) = \chi(X)\chi(Y)$.

::: {.solution}
Give $X$ and $Y$ finite CW structures. If $c_p(X)$ and $c_q(Y)$ denote the numbers of cells in dimensions $p$ and $q$, then the product CW structure on $X\times Y$ has one cell
\[
e^p\times e^q
\]
of dimension $p+q$ for every ordered pair of cells $(e^p,e^q)$.
Hence the number of $r$-cells of $X\times Y$ is
\[
c_r(X\times Y)=\sum_{p+q=r}c_p(X)c_q(Y).
\]
Therefore
\[
\begin{aligned}
\chi(X\times Y)
&=\sum_r(-1)^r c_r(X\times Y)\\
&=\sum_{p,q}(-1)^{p+q}c_p(X)c_q(Y)\\
&=\left(\sum_p(-1)^p c_p(X)\right)
  \left(\sum_q(-1)^q c_q(Y)\right)\\
&=\boxed{\chi(X)\chi(Y)}.
\end{aligned}
\]
:::

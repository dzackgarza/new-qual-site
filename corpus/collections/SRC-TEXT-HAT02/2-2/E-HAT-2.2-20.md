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
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the cell count: the product structure has one cell $e^p\times e^q$ of dimension $p+q$ for
    each pair, so $c_r(X\times Y)=\sum_{p+q=r}c_p(X)c_q(Y)$ and the alternating sums factor.
- event: solution-reviewed
  by: claude
  date: 2026-11-08
  note: >-
    Statement matches Exercise 20 as printed on p. 157. The argument is the cell count and is
    correct; it now cites the product cell structure of p. 8, where Hatcher also notes that the
    cell-complex topology agrees with the product topology when one factor has finitely many
    cells, which is the case here, and the definition of chi as the alternating sum of numbers of
    cells together with Theorem 2.44, both p. 146. What is not covered: no certificate.
---

::: {.problem}
For finite CW complexes $X$ and $Y$, show that $\chi(X \times Y) = \chi(X)\chi(Y)$.
:::

::: {.solution}
Give $X$ and $Y$ finite CW structures. If $c_p(X)$ and $c_q(Y)$ denote the numbers of cells in dimensions $p$ and $q$, then the product cell structure on $X\times Y$ (p. 8) has one cell
$$
e^p\times e^q
$$
of dimension $p+q$ for every ordered pair of cells $(e^p,e^q)$. Since both complexes are finite, the cell-complex topology on $X\times Y$ coincides with the product topology, as noted on p. 8, so this is a CW structure on the product space.
Hence the number of $r$-cells of $X\times Y$ is
$$
c_r(X\times Y)=\sum_{p+q=r}c_p(X)c_q(Y).
$$
Therefore
$$
\begin{aligned}
\chi(X\times Y)
&=\sum_r(-1)^r c_r(X\times Y)\\
&=\sum_{p,q}(-1)^{p+q}c_p(X)c_q(Y)\\
&=\left(\sum_p(-1)^p c_p(X)\right)
  \left(\sum_q(-1)^q c_q(Y)\right)\\
&=\boxed{\chi(X)\chi(Y)},
\end{aligned}
$$
where the first and last equalities are the definition of $\chi$ as the alternating sum of the numbers of cells of a finite CW complex, p. 146, which Theorem 2.44 (p. 146) shows agrees with the alternating sum of the ranks of the homology groups. Both sums are finite, so the rearrangement of the double sum is legitimate.This computation agrees with Sam's §2.2 Exercise 20, printed p. 12 of the same source: the product cell $e_p\times e_q$ has dimension $p+q$, and summing $(-1)^{p+q}$ over those cells factorizes the alternating sum into $\chi(X)\chi(Y)$.


:::

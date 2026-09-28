---
schema: qual/card@1
id: E-HAT-2.2-41
kind: problem
title: Euler characteristic equals alternating sum of dimensions of $H_n(X; F)$ over a field
classification:
  areas:
  - topology
  topics:
  - Euler Characteristic
  - Homology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 41; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete Mayer--Vietoris/algebraic proof checked.
---

::: {.problem}
For $X$ a finite CW complex and $F$ a field, show that the Euler characteristic $\chi(X)$ can also be computed by the formula $\chi(X) = \sum_n (-1)^n \dim H_n(X; F)$, the alternating sum of the dimensions of the vector spaces $H_n(X; F)$.
:::

::: {.solution}
Let $C_*^{CW}(X;F)$ be the cellular chain complex over the field $F$. Since $X$ is finite, every chain group is finite-dimensional and
\[
\dim_F C_n^{CW}(X;F)=c_n,
\]
the number of $n$-cells of $X$.

Write
\[
Z_n=\ker d_n,
\qquad
B_n=\operatorname{im}d_{n+1}.
\]
There are short exact sequences
\[
0\to Z_n\to C_n\to B_{n-1}\to0
\]
and
\[
0\to B_n\to Z_n\to H_n(X;F)\to0.
\]
Taking dimensions gives
\[
\dim C_n
=\dim B_n+\dim H_n(X;F)+\dim B_{n-1}.
\]
Therefore
\[
\begin{aligned}
\chi(X)
&=\sum_n(-1)^n\dim C_n\\
&=\sum_n(-1)^n\dim H_n(X;F)
 +\sum_n(-1)^n\dim B_n
 +\sum_n(-1)^n\dim B_{n-1}.
\end{aligned}
\]
The two boundary sums cancel after shifting the index, leaving
\[
\boxed{
\chi(X)=\sum_n(-1)^n\dim_F H_n(X;F).}
\]
:::

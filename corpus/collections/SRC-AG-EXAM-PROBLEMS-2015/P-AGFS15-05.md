---
schema: qual/card@1
id: P-AGFS15-05
kind: problem
title: Divisors of coordinates and differentials on a cubic curve
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained Algebraic Geometry FS 15 exam-guidelines PDF dated August 12, 2015.
---

::: {.problem}
Assume $\operatorname{char}k=0$.
Let
\[
C:\quad y^2=(x-e_1)(x-e_2)(x-e_3)\subset\mathbb A^2,
\]
where $e_1,e_2,e_3\in k$ are pairwise distinct.
Let $P_j=(e_j,0)\in C$, and let $P_\infty$ be the point at infinity of the projective closure $\overline C\subset\mathbb P^2$.

Show that
\[
\operatorname{div}(dx)=[P_1]+[P_2]+[P_3]-3[P_\infty],
\]
\[
\operatorname{div}(y)=[P_1]+[P_2]+[P_3]-3[P_\infty],
\]
and hence
\[
\operatorname{div}\!\left(\frac{dx}{y}\right)=0.
\]
In particular, $dx/y$ is a regular nowhere-vanishing differential on $\overline C$.
:::

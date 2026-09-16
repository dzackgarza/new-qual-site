---
schema: qual/card@1
id: T-C7GBB
kind: theorem
title: Gauss--Lucas theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Zeros
relations: []
review: draft
---

::: {.theorem}
Let $p\in\CC[z]$ be a nonconstant polynomial.
Then every zero of $p'$ lies in the convex hull of the set of zeros of $p$.
:::

::: {.proof}
Write $p(z)=a\prod_{j=1}^n(z-a_j)$ with $a\neq0$, $n\ge1$, and $a_1,\ldots,a_n\in\CC$ the zeros of $p$ listed with multiplicity.
Let $z\in\CC$ with $p'(z)=0$.
If $p(z)=0$, then $z$ is one of the $a_j$ and lies in the convex hull.
Otherwise $z\neq a_j$ for every $j$, and
$$
0=\frac{p'(z)}{p(z)}=\sum_{j=1}^n\frac{1}{z-a_j}=\sum_{j=1}^n\frac{\overline{z}-\overline{a_j}}{\abs{z-a_j}^2}.
$$
Rearranging gives
$$
\Bigl(\sum_{j=1}^n\frac{1}{\abs{z-a_j}^2}\Bigr)\overline{z}=\sum_{j=1}^n\frac{1}{\abs{z-a_j}^2}\overline{a_j}.
$$
Taking complex conjugates and dividing by $\sum_{j}\abs{z-a_j}^{-2}>0$ writes $z=\sum_j t_ja_j$ with $t_j=\abs{z-a_j}^{-2}/\sum_k\abs{z-a_k}^{-2}$.
The weights $t_j$ are positive and sum to $1$, so $z$ lies in the convex hull of $\{a_1,\ldots,a_n\}$.
:::

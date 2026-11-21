---
schema: qual/card@1
id: D-GRBNR
kind: definition
title: Term orders, initial ideals, and Gröbner bases
classification:
  areas:
  - algebra
  topics:
  - Gröbner Bases
  - Term Orders
  - Initial Ideals
relations: []
review: draft
---

::: {.definition}
Let $k$ be a field and $S = k[x_1,\ldots,x_n]$.

- A \dfn{term order} is a total order $\prec$ on the monomials of $S$ such that $1\preceq m$ for every monomial $m$, and $m\prec m'$ implies $mp\prec m'p$ for every monomial $p$. These two conditions make $\prec$ a well-order, so it has no infinite strictly descending sequence.

- For $f\in S$ nonzero, the \dfn{initial monomial} $\operatorname{in}_\prec(f)$ is the largest monomial occurring in $f$ with respect to $\prec$, and the \dfn{initial ideal} of an ideal $I\subseteq S$ is
$$
\operatorname{in}_\prec(I) \coloneqq \generators{\operatorname{in}_\prec(f) \st f\in I,\ f\neq 0},
$$
which is a monomial ideal.

- A finite subset $G = \theset{g_1,\ldots,g_r}\subseteq I$ is a \dfn{Gröbner basis} of $I$ with respect to $\prec$ if it generates $I$ and
$$
\operatorname{in}_\prec(I) = \generators{\operatorname{in}_\prec(g_1),\ldots,\operatorname{in}_\prec(g_r)} .
$$
:::

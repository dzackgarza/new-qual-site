---
schema: qual/card@1
id: P-PXZN2
kind: problem
title: Finite groups as Galois groups
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Classification
relations: []
review: draft
---

::: {.problem}
Which finite groups occur as Galois groups of some field extension?
:::

::: {.solution}
Every finite group occurs as the Galois group of some field extension.

Let $G$ be finite and choose a field $k$. Form the rational function field
\[
L=k(x_g:g\in G)
\]
in algebraically independent variables indexed by $G$. Let $G$ act on $L$ by
\[
h(x_g)=x_{hg}
\qquad(h,g\in G).
\]
This action is faithful. Let
\[
K=L^G
\]
be the fixed field. Artin's theorem on fixed fields of finite groups of automorphisms gives
\[
[L:K]=|G|
\]
and
\[
\operatorname{Gal}(L/K)\cong G.
\]

Thus there is no restriction if the base field is allowed to vary.

By contrast, asking which finite groups occur as Galois groups over the specific field $\QQ$ is the inverse Galois problem over $\QQ$, which is not known in full generality.
:::

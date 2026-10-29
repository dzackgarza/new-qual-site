---
schema: qual/card@1
id: E-KUGNH
kind: problem
title: Bounded derivatives imply removable singularities
classification:
  areas:
  - complex-analysis
  topics:
  - Removable Singularities
  - Casorati-Weierstrass
  - Singularities
  - Laurent Series
relations: []
review: draft
---

::: {.exercise}
Suppose $f$ is holomorphic on $\DD\smz$ and there exist $M, k$ such that
$$
\abs{f^{(k)}(z)} \leq {M\over \abs{z}^k} \qquad \forall\, 0 < \abs z < 1
.$$

Show that if $f$ has a singularity at $z=0$, then it must be removable.

:::

::: {.hint}
Differentiation sends $z^n$ to a nonzero multiple of $z^{n-1}$ when $n\neq0$, so differentiating $k$ times and multiplying by $z^k$ keeps every negative power of the Laurent series of $f$.
:::

::: {.solution}
Let $k\ge0$ be an integer, let $f(z)=\sum_{n\in\ZZ}a_nz^n$ be the Laurent series of $f$ on $\DD\smz$, and set $F(z)\coloneqq z^kf^{(k)}(z)$.

::: pf

::: {.pf-step #laurent-F}
$F(z)=\sum_{n\in\ZZ}(n)_k\,a_nz^n$ on $\DD\smz$, where $(n)_k\coloneqq n(n-1)\cdots(n-k+1)$, and $(n)_k\neq0$ for $n<0$.

::: pf-proof
Laurent series differentiate term by term, and $\frac{d^k}{dz^k}z^n=(n)_kz^{n-k}$. For $n<0$ every factor $n-j$ is negative.
:::

:::

::: {.pf-step #F-removable}
$F$ has a removable singularity at $0$.

::: pf-proof
The hypothesis gives $\abs F\le M$ on $\DD\smz$, so Riemann's removable singularity theorem applies.
:::

:::

::: pf-step
$0$ is a removable singularity of $f$.

::: pf-proof
By step [](#F-removable){.pf-ref} the Laurent coefficients of $F$ at negative powers vanish, so by step [](#laurent-F){.pf-ref} $(n)_ka_n=0$ and hence $a_n=0$ for every $n<0$. The Laurent series of $f$ is then a power series.
:::

:::

:::

:::

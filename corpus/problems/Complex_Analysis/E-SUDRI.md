---
schema: qual/card@1
id: E-SUDRI
kind: problem
title: Entire functions with $f(z)\to\infty$ as $z\to\infty$ are polynomials
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Polynomials
  - Singularities
  - Casorati-Weierstrass
relations: []
review: draft
---

::: {.exercise}
Show that if $f$ is entire and $f(z) \convergesto{z\to\infty} \infty$ then $f$ is a polynomial.
:::

::: {.solution}
Let $f(z) = \sum_{k\geq 0} c_k z^k$ be the Taylor series of $f$, which converges on $\CC$, and put $g(w) \coloneqq f(1/w)$ for $w\neq 0$, so that $g(w) = \sum_{k\geq 0} c_k w^{-k}$ is the Laurent series of $g$ about $0$.

::: pf

::: {.pf-step #pole}
$g$ has a pole at $0$.

::: pf-proof
$g$ is holomorphic on $\CC\sm\{0\}$ and $g(w)\to\infty$ as $w\to 0$. So $0$ is not removable, since $g$ is unbounded near $0$. It is not essential, since by Casorati--Weierstrass the image of every punctured neighbourhood of an essential singularity is dense in $\CC$, while here $\abs{g}>1$ on some punctured neighbourhood of $0$.
:::

:::

::: pf-step
$f$ is a polynomial.

::: pf-proof
Let $N$ be the order of the pole in step [](#pole){.pf-ref}. The principal part of $g$ at $0$ is $\sum_{k\geq 1} c_k w^{-k}$, and it ends at $w^{-N}$, so $c_k = 0$ for $k>N$ and $f(z) = \sum_{0\leq k\leq N} c_k z^k$.
:::

:::

:::

:::

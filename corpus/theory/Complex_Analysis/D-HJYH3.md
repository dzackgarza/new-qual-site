---
schema: qual/card@1
id: D-HJYH3
kind: definition
title: Riemann zeta function
classification:
  areas:
  - complex-analysis
  topics:
  - Riemann Zeta
relations: []
review: draft
---

::: {.definition}
For $s\in\CC$ with $\operatorname{Re}s>1$, the \dfn{Riemann zeta function} is
$$
\zeta(s)\coloneqq\sum_{n=1}^{\infty}\frac{1}{n^{s}},
$$
where $n^{s}\coloneqq e^{s\log n}$ with the real logarithm.
The series converges absolutely because $\abs{n^{-s}}=n^{-\operatorname{Re}s}$.
:::

::: {.proposition title="Euler product"}
For $\operatorname{Re}s>1$,
$$
\zeta(s)=\prod_{p\text{ prime}}\frac{1}{1-p^{-s}},
$$
where the product is over all prime numbers $p$ and converges as the limit of its partial products over $p\le N$.
:::

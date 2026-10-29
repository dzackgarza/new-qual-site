---
schema: qual/card@1
id: E-ALB7C
kind: problem
title: A pole of order $n$ of $f$ is a pole of order $n+k$ of $f^{(k)}$
classification:
  areas:
  - complex-analysis
  topics:
  - Poles
  - Laurent Series
  - Principal Parts
relations: []
review: draft
---

::: {.exercise}
Show that if $z_0$ is a pole of order $n$ of $f$, then it is a pole of order $n+k$ for $f^{(k)}$.

:::

::: {.solution}
Translating, assume $z_0=0$.

::: pf

::: {.pf-step #laurent}
On a punctured disc about $0$, $f^{(k)}(z) = \sum_{j\geq -n} j(j-1)\cdots(j-k+1)\, c_j z^{j-k}$, where $f(z)=\sum_{j\ge-n}c_jz^j$ with $c_{-n}\neq0$.

::: pf-proof
Since $0$ is a pole of order $n$, $f$ has a Laurent series of this form, and a Laurent series may be differentiated term by term on its annulus of convergence.
:::

:::

::: pf-step
$0$ is a pole of order $n+k$ of $f^{(k)}$.

::: pf-proof
The most negative power in step [](#laurent){.pf-ref} is $z^{-n-k}$, with coefficient
$$
(-n)(-n-1)\cdots(-n-k+1)\,c_{-n}=(-1)^k n(n+1)\cdots(n+k-1)\,c_{-n}\neq0.
$$
:::

:::

:::

:::

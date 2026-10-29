---
schema: qual/card@1
id: P-RHQC5
kind: problem
title: 'Weierstrass''s theorem: locally uniform limits of holomorphic functions are
  holomorphic'
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Convergence
  - Sequences of Functions
  - Holomorphic Functions
  - Morera
relations: []
review: draft
---

::: {.problem}
Suppose $\theset{f_n}_{n\in \NN}$ is a sequence of analytic functions on $\DD \definedas \theset{z\in \CC \suchthat \abs{z} < 1}$.

Show that if $f_n\to g$ for some $g: \DD \to \CC$ uniformly on every compact $K\subset \DD$, then $g$ is analytic on $\DD$.
:::

::: {.solution}

::: pf

::: {.pf-step #continuous}

$g$ is continuous on $\DD$.

::: pf-proof

Each point of $\DD$ has a compact neighborhood in $\DD$, on which $g$ is a uniform limit of continuous functions.

:::

:::

::: {.pf-step #triangles}

$\int_{\partial T}g(z)\,dz=0$ for every closed triangle $T\subset\DD$.

::: pf-proof

$f_n\to g$ uniformly on the compact set $\partial T$, so
$$
\int_{\partial T}g(z)\,dz=\lim_{n\to\infty}\int_{\partial T}f_n(z)\,dz,
$$
and each integral on the right is $0$ by Cauchy's theorem.

:::

:::

::: pf-step

$g$ is analytic on $\DD$.

::: pf-proof

By steps [](#continuous){.pf-ref} and [](#triangles){.pf-ref}, Morera's theorem applies.

:::

:::

:::

:::

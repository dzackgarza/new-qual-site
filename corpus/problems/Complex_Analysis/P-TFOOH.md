---
schema: qual/card@1
id: P-TFOOH
kind: problem
title: Compact-uniform limits of analytic functions on $\DD$ are analytic
classification:
  areas:
  - complex-analysis
  topics:
  - Morera
  - Uniform Convergence
  - Sequences of Functions
  - Holomorphic Functions
relations: []
review: draft
---

::: {.problem}
Suppose $\theset{f_n}_{n\in \NN}$ is a sequence of analytic functions on $\DD \definedas \theset{z\in \CC \suchthat \abs{z} < 1}$.

Show that if $f_n\to g$ for some $g: \DD \to \CC$ uniformly on every compact $K\subset \DD$, then $g$ is analytic on $\DD$.


:::

::: {.solution}

::: pf

::: {.pf-step #cont}

$g$ is continuous on $\DD$.

::: pf-proof

Each point of $\DD$ has a closed disc neighborhood $K \subset \DD$, which is compact. On $K$, $g$ is a uniform limit of continuous functions, hence continuous.

:::

:::

::: {.pf-step #tri}

$\int_{\partial T} g\,dz = 0$ for every closed triangle $T \subset \DD$.

::: pf-proof

The boundary $\partial T$ is compact, so $f_n \to g$ uniformly on $\partial T$. By Cauchy's theorem in the disc, $\int_{\partial T} f_n\,dz = 0$ for every $n$, and uniform convergence on a path of finite length lets the limit pass through the integral:
$$
\int_{\partial T} g\,dz = \lim_{n\to\infty} \int_{\partial T} f_n\,dz = 0.
$$

:::

:::

::: pf-step

$g$ is analytic on $\DD$.

::: pf-proof

This is Morera's theorem applied to $g$, using steps [](#cont){.pf-ref} and [](#tri){.pf-ref}.

:::

:::

:::

:::


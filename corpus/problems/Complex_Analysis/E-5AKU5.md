---
schema: qual/card@1
id: E-5AKU5
kind: problem
title: Locally uniform limits of holomorphic functions are holomorphic
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

::: {.exercise}
Show that if $f_n\to f$ locally uniformly and each $f_n$ is holomorphic then $f$ is holomorphic.

:::

::: {.solution}
Let $\Omega$ be the open set on which the $f_n$ are holomorphic.

::: pf

::: {.pf-step #s1}

$f$ is continuous on $\Omega$.

::: pf-proof

Each point of $\Omega$ has a compact neighbourhood in $\Omega$, on which $f$ is a uniform limit of continuous functions.

:::

:::

::: {.pf-step #s2}

$\int_{\partial T}f=0$ for every closed triangle $T\subset\Omega$.

::: pf-proof

By Goursat's theorem $\int_{\partial T}f_n=0$. The boundary $\partial T$ is compact, so $f_n\to f$ uniformly on it, and $\int_{\partial T}f=\lim_n\int_{\partial T}f_n=0$.

:::

:::

::: pf-qed

Every point of $\Omega$ has a disc in $\Omega$ around it, and on that disc steps [](#s1){.pf-ref} and [](#s2){.pf-ref} are the hypotheses of Morera's theorem [@SS03, Chapter 2, Theorem 5.2]. So $f$ is holomorphic near every point of $\Omega$.

:::

:::

:::

::: {.remark title="Variations"}
If $f_n\to f$ uniformly on all of $\Omega$, the hypothesis holds a fortiori, since uniform convergence on $\Omega$ is uniform convergence on each compact subset; the proof above applies unchanged.
:::

---
schema: qual/card@1
id: P-U2ZP6
kind: problem
title: Polynomials in $z$ are not uniformly dense in $C(\bar\DD)$
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Convergence
  - Polynomials
  - Counterexamples
  - Holomorphic Functions
relations: []
review: draft
---

::: {.problem}
Can every continuous function on $\bar \DD$ be uniformly approximated by polynomials in the variable $z$?
:::

::: {.hint}
Compare to Weierstrass for the real interval.
:::

::: {.solution}

::: pf

::: {.pf-step #limit}

A uniform limit on $\bar\DD$ of polynomials in $z$ is holomorphic on $\DD$.

::: pf-proof

Polynomials are holomorphic, and a locally uniform limit of holomorphic functions on an open set is holomorphic, by Morera's theorem.

:::

:::

::: pf-step

$\boxed{\text{No}}$: the function $f(z) = \bar z$ is continuous on $\bar\DD$ and is not a uniform limit of polynomials in $z$.

::: pf-proof

The function $\bar z$ fails the Cauchy--Riemann equations at every point, since $u = x$ and $v = -y$ give $u_x = 1 \neq -1 = v_y$. So it is not holomorphic on $\DD$, and step [](#limit){.pf-ref} excludes it.

:::

:::

:::

:::

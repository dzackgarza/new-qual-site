---
schema: qual/card@1
id: FD-EKGLW
kind: definition
title: Order of a pole as the least $m$ with $(z-a)^{m+1}f(z)\to0$
prompts:
- What is the order of a pole of $f$ at $a$?
classification:
  areas:
  - complex-analysis
  topics:
  - Poles
  - Singularities
relations:
- kind: variant-of
  target: FD-C7EQD
review: draft
---

::: {.definition}
Let $f$ be [[D-E7A5W|holomorphic]] on a punctured disc $D_r(a)\setminus\{a\}$ with a [[D-AUD6K|pole]] at $a$.
The \dfn{order} of the pole is the smallest integer $m\ge0$ such that
$$
\lim_{z\to a}(z-a)^{m+1}f(z)=0.
$$
:::

::: {.proposition}
If $f(z)=(z-a)^{-n}h(z)$ near $a$ with $n\ge1$, $h$ holomorphic near $a$, and $h(a)\neq0$, then the order defined here is $n$.
:::

::: {.proof}
We have $(z-a)^{m+1}f(z)=(z-a)^{m+1-n}h(z)$.
If $m\ge n$, this tends to $0$.
If $m=n-1$, it tends to $h(a)\neq0$; if $m<n-1$, its modulus tends to $\infty$.
So the smallest $m$ with limit $0$ is $n$.
:::

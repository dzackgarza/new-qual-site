---
schema: qual/card@1
id: P-OREB6
kind: problem
title: A permutation is odd iff it has an odd number of even-length cycles
classification:
  areas:
  - algebra
  topics:
  - Permutations
relations: []
review: draft
---

::: {.problem}
Show that a permutation is odd if and only if its disjoint-cycle decomposition contains an odd number of even-length cycles.
:::

::: {.solution}
Write a permutation as a product of disjoint cycles $\sigma=c_1\cdots c_r$, and let $e$ be the number of $c_i$ of even length.

::: pf

::: {.pf-step #cycle-sign}

An $m$-cycle has sign $(-1)^{m-1}$; it is odd exactly when $m$ is even.

::: pf-proof

$(a_1\ a_2\ \cdots\ a_m)=(a_1\ a_m)(a_1\ a_{m-1})\cdots(a_1\ a_2)$ is a product of $m-1$ transpositions.

:::

:::

::: pf-step

$\operatorname{sgn}(\sigma)=(-1)^e$, so $\sigma$ is odd exactly when $e$ is odd.

::: pf-proof

Since $\operatorname{sgn}$ is a homomorphism,
$$
\operatorname{sgn}(\sigma)=\prod_{i=1}^r\operatorname{sgn}(c_i).
$$
By step [](#cycle-sign){.pf-ref}, odd-length cycles contribute $+1$ and even-length cycles contribute $-1$.

:::

:::

:::

:::

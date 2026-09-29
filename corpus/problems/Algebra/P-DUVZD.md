---
schema: qual/card@1
id: P-DUVZD
kind: problem
title: Cycle type, order, and sign of $(4\,2\,1)(6\,1\,3\,2)$
classification:
  areas:
  - algebra
  topics:
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
- Let $\sigma = (4\, 2\, 1)(6\, 1\, 3\, 2) \in S_6$ in cycle notation.

  - Write $\sigma$ as a product of disjoint cycles.

  - Compute the order of $\sigma$.
    What is the general theorem about the order of cycles?

  - Determine if $\sigma$ is even or odd.
    What is the general theorem?
:::

::: {.solution}
Permutations are composed from right to left.

::: pf

::: pf-step

$\sigma=(1\,3)(2\,6\,4)$.

::: pf-proof

Applying $(6\,1\,3\,2)$ and then $(4\,2\,1)$:
$1\mapsto3\mapsto3$, $3\mapsto2\mapsto1$, $2\mapsto6\mapsto6$, $6\mapsto1\mapsto4$, $4\mapsto4\mapsto2$, $5\mapsto5$.
So $\sigma$ swaps $1$ and $3$, cycles $2\mapsto6\mapsto4\mapsto2$, and fixes $5$.

:::

:::

::: {.pf-step #s2}

If $\pi=c_1\cdots c_k$ is a product of disjoint cycles of lengths $\ell_1,\dots,\ell_k$, then $\operatorname{ord}(\pi)=\operatorname{lcm}(\ell_1,\dots,\ell_k)$; hence $\operatorname{ord}(\sigma)=\operatorname{lcm}(2,3)=\boxed{6}$.

::: pf-proof

Disjoint cycles commute, so $\pi^N=c_1^N\cdots c_k^N$, and the $c_i^N$ have disjoint supports.
Thus $\pi^N=1$ exactly when every $c_i^N=1$, that is, when $\ell_i\mid N$ for every $i$.

:::

:::

::: pf-step

With $\pi$ as in step [](#s2){.pf-ref}, $\operatorname{sgn}(\pi)=(-1)^{\sum_i(\ell_i-1)}$; hence $\operatorname{sgn}(\sigma)=(-1)^{1+2}=-1$ and $\sigma$ is odd.

::: pf-proof

A $k$-cycle is the product $(a_1\,a_k)(a_1\,a_{k-1})\cdots(a_1\,a_2)$ of $k-1$ transpositions, so it has sign $(-1)^{k-1}$, and $\operatorname{sgn}$ is a homomorphism.

:::

:::

:::

:::

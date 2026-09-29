---
schema: qual/card@1
id: P-UCTOP-SU09-8
kind: problem
title: Euler characteristic parity for even-dimensional manifolds
classification:
  areas:
  - topology
  topics:
  - Manifolds
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Let $M^{2n}$ be a closed orientable even-dimensional manifold.
Show that its Euler characteristic is odd if and only if the dimension of $H_n(M; \mathbb{Q})$ is odd, and that consequently a closed manifold of dimension $4n + 2$ with odd Euler characteristic must be non-orientable.
:::

::: {.solution}
**Goal.** For a closed orientable $2n$-manifold $M$, relate the parity of $\chi(M)$ to $\dim H_n(M;\QQ)$, and deduce a non-orientability statement in dimension $4n+2$.

::: pf

::: pf-step
$\chi(M) = \sum_{i=0}^{2n} (-1)^i b_i$, where $b_i = \dim H_i(M;\QQ)$.

::: pf-proof
the Euler characteristic equals the alternating sum of Betti numbers.
:::

:::

::: pf-step
By Poincaré duality, $b_i = b_{2n-i}$.

::: pf-proof
$H_i(M;\QQ) \cong H^{2n-i}(M;\QQ) \cong H_{2n-i}(M;\QQ)$ (orientable closed manifold).
:::

:::

::: pf-step
Hence $\chi(M) \equiv b_n \pmod 2$.

::: pf-proof

::: pf-step
The terms $(-1)^i b_i$ and $(-1)^{2n-i} b_{2n-i}$ are equal (since $b_i = b_{2n-i}$ and $(-1)^i = (-1)^{2n-i}$).

::: pf-proof
$2n - i$ and $i$ have the same parity.
:::

:::

::: pf-step
So all terms cancel in pairs except the middle term $(-1)^n b_n$.

::: pf-proof
the sum $\sum_{i=0}^{2n} (-1)^i b_i$ pairs $i$ with $2n-i$; the only unpaired index is $i = n$.
:::

:::

::: {.pf-step #s3-3}
Hence $\chi(M) = (-1)^n b_n + 2(\text{integer})$, so $\chi(M) \equiv b_n \pmod 2$.

::: pf-proof
the paired terms sum to an even integer.
:::

:::

:::

:::

::: {.pf-step #s4}
Therefore $\chi(M)$ is odd iff $b_n = \dim H_n(M;\QQ)$ is odd.

::: pf-proof
step [](#s3-3){.pf-ref}.
:::

:::

::: {.pf-step #s5}
A closed $4n+2$-manifold with odd $\chi$ is non-orientable.

::: pf-proof

::: pf-step
Suppose $M$ is orientable of dimension $4n+2 = 2(2n+1)$.

::: pf-proof
assume for contradiction.
:::

:::

::: pf-step
Then $b_{2n+1}$ is even.

::: pf-proof
the intersection form on $H_{2n+1}(M;\QQ)$ is alternating (skew-symmetric) since $2n+1$ is odd, and a nondegenerate alternating form on a vector space forces the dimension to be even.
:::

:::

::: {.pf-step #s5-3}
Hence $\chi(M)$ is even.

::: pf-proof
by step [](#s4){.pf-ref}, $\chi(M) \equiv b_{2n+1} \equiv 0 \pmod 2$.
:::

:::

::: pf-step
Contradiction with $\chi(M)$ odd.

::: pf-proof
step [](#s5-3){.pf-ref} contradicts the hypothesis.
:::

:::

:::

:::

::: pf-qed
step [](#s4){.pf-ref} is the first claim; step [](#s5){.pf-ref} is the consequence.
:::

:::
:::

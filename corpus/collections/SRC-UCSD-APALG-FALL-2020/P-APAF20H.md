---
schema: qual/card@1
id: P-APAF20H
kind: problem
title: Orthogonal complement of a $G$-invariant subspace is $G$-invariant
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Inner Product Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
Let $U\colon G\to\mathrm{U}(H)$ be a unitary representation of a compact group $G$ on a Hilbert space $H$.
Prove that, if $K$ is a closed subspace of $H$ invariant under the action of $G$, so is $K^\perp$.
:::

::: {.solution}

::: pf

::: {.pf-step #fix-v-and-g}
Let $v \in K^\perp$ and $g \in G$.

::: pf-proof
take an arbitrary element of $K^\perp$ and an arbitrary group element.
:::

:::

::: {.pf-step #inner-product-rewrite-via-unitary}
For any $w \in K$, $\langle U(g)v, w \rangle = \langle v, U(g)^* w \rangle = \langle v, U(g)^{-1} w \rangle = \langle v, U(g^{-1}) w \rangle$.

::: pf-proof
$U(g)$ is unitary, so $U(g)^* = U(g)^{-1} = U(g^{-1})$.
:::

:::

::: {.pf-step #preimage-in-k}
$U(g^{-1}) w \in K$ (since $K$ is $G$-invariant).

::: pf-proof
hypothesis.
:::

:::

::: {.pf-step #inner-product-vanishes}
Hence $\langle U(g)v, w \rangle = \langle v, U(g^{-1})w \rangle = 0$ (since $v \in K^\perp$).

::: pf-proof
Steps [](#inner-product-rewrite-via-unitary){.pf-ref} and [](#preimage-in-k){.pf-ref}.
:::

:::

::: {.pf-step #u-g-v-in-k-perp}
Therefore $U(g)v \in K^\perp$ for all $g \in G$, so $K^\perp$ is $G$-invariant.

::: pf-proof
Step [](#inner-product-vanishes){.pf-ref} (for arbitrary $w \in K$).
:::

:::

::: pf-qed
Step [](#u-g-v-in-k-perp){.pf-ref}.
:::

:::

:::

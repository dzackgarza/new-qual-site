---
schema: qual/card@1
id: P-TOPS05B
kind: problem
title: "Z_k-orientable manifold for k > 2 is orientable"
classification:
  areas:
  - topology
  topics:
  - Orientation
  - Manifolds
relations: []
review: draft
---

::: {.problem}
Let $X$ be a compact $\mathbb{Z}_k$ orientable manifold for $k > 2$.
Prove $X$ is orientable.
:::

::: {.solution}

::: pf

::: pf-step

The orientation local system of a connected manifold has monodromy
$$
\omega:\pi_1(X)\to\{\pm1\}.
$$

::: pf-proof

Transporting a local integral orientation around a loop either preserves it or reverses it, giving the orientation character.

:::

:::

::: pf-step

After reduction modulo $k$, orientation transport acts on the local group $\mathbb Z/k$ by multiplication by $\omega(\gamma)$.

::: pf-proof

The $\mathbb Z_k$-orientation system is obtained from the integral orientation system by tensoring with $\mathbb Z/k$.

:::

:::

::: {.pf-step #s3}

If $X$ is $\mathbb Z_k$-orientable, this mod-$k$ local system is trivial, so every loop acts as $+1$ on $\mathbb Z/k$.

::: pf-proof

Orientability over a coefficient ring means the orientation local system with those coefficients is constant.

:::

:::

::: {.pf-step #s4}

Since $k>2$, multiplication by $-1$ on $\mathbb Z/k$ is not the identity.

::: pf-proof

The equality $-1=1$ in $\mathbb Z/k$ would imply $k\mid2$, contrary to $k>2$.

:::

:::

::: pf-step

Hence $\omega$ is trivial and $X$ is orientable over $\mathbb Z$.

::: pf-proof

By steps [](#s3){.pf-ref} and [](#s4){.pf-ref} no loop can have orientation character $-1$.

:::

:::

:::

:::

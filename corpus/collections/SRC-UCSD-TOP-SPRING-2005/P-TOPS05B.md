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

::: problem
Let $X$ be a compact $\mathbb{Z}_k$ orientable manifold for $k > 2$.
Prove $X$ is orientable.
:::

::: {.solution}
<1>1. The orientation local system of a connected manifold has monodromy
$$
\omega:\pi_1(X)\to\{\pm1\}.
$$
::: {.proof}
Transporting a local integral orientation around a loop either preserves it or reverses it, giving the orientation character.
:::

<1>2. After reduction modulo $k$, orientation transport acts on the local group $\mathbb Z/k$ by multiplication by $\omega(\gamma)$.
::: {.proof}
The $\mathbb Z_k$-orientation system is obtained from the integral orientation system by tensoring with $\mathbb Z/k$.
:::

<1>3. If $X$ is $\mathbb Z_k$-orientable, this mod-$k$ local system is trivial, so every loop acts as $+1$ on $\mathbb Z/k$.
::: {.proof}
Orientability over a coefficient ring means the orientation local system with those coefficients is constant.
:::

<1>4. Since $k>2$, multiplication by $-1$ on $\mathbb Z/k$ is not the identity.
::: {.proof}
The equality $-1=1$ in $\mathbb Z/k$ would imply $k\mid2$, contrary to $k>2$.
:::

<1>5. Hence $\omega$ is trivial and $X$ is orientable over $\mathbb Z$.
::: {.proof}
By <1>3--<1>4 no loop can have orientation character $-1$.
:::
:::

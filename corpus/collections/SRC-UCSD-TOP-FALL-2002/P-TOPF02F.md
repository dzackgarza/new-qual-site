---
schema: qual/card@1
id: P-TOPF02F
kind: problem
title: "Z3-orientable manifold is orientable"
classification:
  areas:
  - topology
  topics:
  - Manifolds
  - Orientation
relations: []
review: draft
---

::: {.problem}
Let $X$ be an $n$-dimensional $\mathbb{Z}_3$-orientable manifold.
Prove that $X$ is orientable.
:::

::: {.solution}

::: pf

::: {.pf-step #orientation-monodromy}
For a connected $n$-manifold $X$, integral orientability is governed by the orientation monodromy
$$
\omega:\pi_1(X,x_0)\longrightarrow\operatorname{Aut}(H_n(X,X\setminus\{x_0\};\mathbb Z))\cong\{\pm1\}.
$$

::: pf-proof
Transporting a local orientation around a loop returns either the same orientation or its negative. The manifold is orientable exactly when this monodromy is trivial.
:::

:::

::: {.pf-step #mod3-reduction}
Reducing local homology modulo $3$ sends the two possible monodromies to multiplication by $+1$ and $-1=2$ on $\mathbb Z_3$.

::: pf-proof
The local homology group with $\mathbb Z_3$ coefficients is
$$
H_n(X,X\setminus\{x_0\};\mathbb Z_3)\cong\mathbb Z_3,
$$
and integral orientation transport reduces modulo $3$. Since $2\ne1$ in $\mathbb Z_3$, the sign is still detected after reduction.
:::

:::

::: {.pf-step #mod3-monodromy-trivial}
If $X$ is $\mathbb Z_3$-orientable, the mod-$3$ orientation monodromy is trivial.

::: pf-proof
A $\mathbb Z_3$-orientation is a globally consistent choice of nonzero local fundamental classes, equivalently triviality of the orientation local system with $\mathbb Z_3$ coefficients.
:::

:::

::: pf-step
Therefore the integral orientation monodromy is trivial.

::: pf-proof
If some loop had $\omega(\gamma)=-1$, then by step [](#mod3-reduction){.pf-ref} its action modulo $3$ would be multiplication by $2$, contradicting step [](#mod3-monodromy-trivial){.pf-ref}. Hence every loop acts by $+1$.
:::

:::

::: pf-step
Thus $X$ is orientable.

::: pf-proof
By step [](#orientation-monodromy){.pf-ref}, trivial integral orientation monodromy is equivalent to orientability. If $X$ is disconnected, apply the same argument to each connected component.
:::

:::

:::

:::


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

::: problem
Let $X$ be an $n$-dimensional $\mathbb{Z}_3$-orientable manifold.
Prove that $X$ is orientable.
:::

::: {.solution}
<1>1. For a connected $n$-manifold $X$, integral orientability is governed by the orientation monodromy
$$
\omega:\pi_1(X,x_0)\longrightarrow\operatorname{Aut}(H_n(X,X\setminus\{x_0\};\mathbb Z))\cong\{\pm1\}.
$$
::: {.proof}
Transporting a local orientation around a loop returns either the same orientation or its negative. The manifold is orientable exactly when this monodromy is trivial.
:::

<1>2. Reducing local homology modulo $3$ sends the two possible monodromies to multiplication by $+1$ and $-1=2$ on $\mathbb Z_3$.
::: {.proof}
The local homology group with $\mathbb Z_3$ coefficients is
$$
H_n(X,X\setminus\{x_0\};\mathbb Z_3)\cong\mathbb Z_3,
$$
and integral orientation transport reduces modulo $3$. Since $2\ne1$ in $\mathbb Z_3$, the sign is still detected after reduction.
:::

<1>3. If $X$ is $\mathbb Z_3$-orientable, the mod-$3$ orientation monodromy is trivial.
::: {.proof}
A $\mathbb Z_3$-orientation is a globally consistent choice of nonzero local fundamental classes, equivalently triviality of the orientation local system with $\mathbb Z_3$ coefficients.
:::

<1>4. Therefore the integral orientation monodromy is trivial.
::: {.proof}
If some loop had $\omega(\gamma)=-1$, then by <1>2 its action modulo $3$ would be multiplication by $2$, contradicting <1>3. Hence every loop acts by $+1$.
:::

<1>5. Thus $X$ is orientable.
::: {.proof}
By <1>1, trivial integral orientation monodromy is equivalent to orientability. If $X$ is disconnected, apply the same argument to each connected component.
:::
:::


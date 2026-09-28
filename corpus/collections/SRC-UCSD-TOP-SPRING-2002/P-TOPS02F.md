---
schema: qual/card@1
id: P-TOPS02F
kind: problem
title: "Orientation sheaf of an R-orientable manifold is a trivial local system"
classification:
  areas:
  - topology
  topics:
  - Orientation
  - Sheaves
  - Manifolds
relations: []
review: draft
---

::: {.problem}
Let $X$ be an $n$-dimensional manifold and $X_0$ its $R$-orientation sheaf.
Give $R$ the discrete topology.
If $X$ is $R$-orientable, prove $X_0$ is homeomorphic to $X \times R$.
:::

::: {.solution}
<1>1. For each $x\in X$, the stalk of the $R$-orientation sheaf is
$$
(X_0)_x=H_n(X,X-\{x\};R),
$$
a free rank-one $R$-module.
::: {.proof}
This is the local homology characterization of an $n$-manifold and the definition of the orientation local system.
:::

<1>2. An $R$-orientation is a continuous choice of generator
$$
s(x)\in (X_0)_x
$$
for every $x\in X$.
::: {.proof}
By definition, $R$-orientability means precisely that the orientation local system admits a nowhere-zero locally constant section which generates each rank-one stalk.
:::

<1>3. Define
$$
\Phi:X\times R\longrightarrow X_0,
\qquad
\Phi(x,r)=r\,s(x).
$$
::: {.proof}
Scalar multiplication is defined in each stalk. Since $R$ has the discrete topology and $s$ is locally constant in local trivializations, $\Phi$ is continuous.
:::

<1>4. The map $\Phi$ is a fiberwise bijection.
::: {.proof}
For each fixed $x$, the chosen element $s(x)$ is a basis of the free rank-one $R$-module $(X_0)_x$, so $r\mapsto r s(x)$ is a bijection $R\to (X_0)_x$.
:::

<1>5. In every orientation chart, $s$ identifies $X_0$ locally with $U\times R$, and under these identifications $\Phi$ is the identity trivialization.
::: {.proof}
On an orientable chart $U$, the local orientation section is constant in the standard trivialization of the orientation sheaf. Hence $\Phi|_{U\times R}$ and its inverse are continuous.
:::

<1>6. Therefore
$$
\boxed{X_0\cong X\times R}
$$
as covering spaces/local systems over $X$.
::: {.proof}
The local homeomorphisms from <1>5 glue to the global fiberwise bijection from <1>3--<1>4.
:::
:::

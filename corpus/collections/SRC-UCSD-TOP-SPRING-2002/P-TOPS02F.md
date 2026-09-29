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

::: pf

::: pf-step

For each $x\in X$, the stalk of the $R$-orientation sheaf is
$$
(X_0)_x=H_n(X,X-\{x\};R),
$$
a free rank-one $R$-module.

::: pf-proof

This is the local homology characterization of an $n$-manifold and the definition of the orientation local system.

:::

:::

::: pf-step

An $R$-orientation is a continuous choice of generator
$$
s(x)\in (X_0)_x
$$
for every $x\in X$.

::: pf-proof

By definition, $R$-orientability means precisely that the orientation local system admits a nowhere-zero locally constant section which generates each rank-one stalk.

:::

:::

::: {.pf-step #s3}

Define
$$
\Phi:X\times R\longrightarrow X_0,
\qquad
\Phi(x,r)=r\,s(x).
$$

::: pf-proof

Scalar multiplication is defined in each stalk. Since $R$ has the discrete topology and $s$ is locally constant in local trivializations, $\Phi$ is continuous.

:::

:::

::: {.pf-step #s4}

The map $\Phi$ is a fiberwise bijection.

::: pf-proof

For each fixed $x$, the chosen element $s(x)$ is a basis of the free rank-one $R$-module $(X_0)_x$, so $r\mapsto r s(x)$ is a bijection $R\to (X_0)_x$.

:::

:::

::: {.pf-step #s5}

In every orientation chart, $s$ identifies $X_0$ locally with $U\times R$, and under these identifications $\Phi$ is the identity trivialization.

::: pf-proof

On an orientable chart $U$, the local orientation section is constant in the standard trivialization of the orientation sheaf. Hence $\Phi|_{U\times R}$ and its inverse are continuous.

:::

:::

::: pf-step

Therefore
$$
\boxed{X_0\cong X\times R}
$$
as covering spaces/local systems over $X$.

::: pf-proof

The local homeomorphisms from step [](#s5){.pf-ref} glue to the global fiberwise bijection from steps [](#s3){.pf-ref} and [](#s4){.pf-ref}.

:::

:::

:::

:::

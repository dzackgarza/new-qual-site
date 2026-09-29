---
schema: qual/card@1
id: P-UCTOP-FA12-5
kind: problem
title: No retraction from compact orientable manifold to its boundary
classification:
  areas:
  - topology
  topics:
  - Manifolds
  - Duality
relations: []
review: draft
---

::: {.problem}
Show that if $M$ is a compact orientable manifold with boundary $\partial M$, then there does not exist a retraction $r : M \to \partial M$.
:::

::: {.solution}

::: pf

::: pf-step
Let $i:\partial M\hookrightarrow M$ be the inclusion and let $n=\dim M$.

::: pf-proof
It suffices to argue on a connected component with nonempty boundary.
:::

:::

::: {.pf-step #fundamental-class-nonzero}
The relative fundamental class satisfies
$$
\partial[M,\partial M]=[\partial M]\ne0
$$
in $H_{n-1}(\partial M;\mathbb Z)$.

::: pf-proof
This is the boundary formula for the relative fundamental class of a compact oriented manifold. The boundary class is the sum of the fundamental classes of its oriented components and is nonzero.
:::

:::

::: {.pf-step #boundary-class-killed}
Exactness of the pair sequence implies
$$
i_*[\partial M]=0.
$$

::: pf-proof
The segment
$$
H_n(M,\partial M)\xrightarrow{\partial}H_{n-1}(\partial M)\xrightarrow{i_*}H_{n-1}(M)
$$
is exact, so the image of the boundary map lies in the kernel of $i_*$.
:::

:::

::: {.pf-step #retraction-implies-injective}
A retraction $r:M\to\partial M$ would make $i_*$ injective.

::: pf-proof
If $r\circ i=\operatorname{id}_{\partial M}$, then
$$
r_*\circ i_*=\operatorname{id}_{H_*(\partial M)},
$$
so $i_*$ has a left inverse.
:::

:::

::: pf-step
Therefore no such retraction exists.

::: pf-proof
The nonzero class in step [](#fundamental-class-nonzero){.pf-ref} is killed by $i_*$ in step [](#boundary-class-killed){.pf-ref}, contradicting injectivity from step [](#retraction-implies-injective){.pf-ref}.
:::

:::

:::

:::

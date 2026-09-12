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

Show that if $M$ is a compact orientable manifold with boundary $\partial M$, then there does not exist a retraction $r : M \to \partial M$.

::: {.solution}
<1>1. Let $i:\partial M\hookrightarrow M$ be the inclusion and let $n=\dim M$.
::: {.proof}
It suffices to argue on a connected component with nonempty boundary.
:::

<1>2. The relative fundamental class satisfies
$$
\partial[M,\partial M]=[\partial M]\ne0
$$
in $H_{n-1}(\partial M;\mathbb Z)$.
::: {.proof}
This is the boundary formula for the relative fundamental class of a compact oriented manifold. The boundary class is the sum of the fundamental classes of its oriented components and is nonzero.
:::

<1>3. Exactness of the pair sequence implies
$$
i_*[\partial M]=0.
$$
::: {.proof}
The segment
$$
H_n(M,\partial M)\xrightarrow{\partial}H_{n-1}(\partial M)\xrightarrow{i_*}H_{n-1}(M)
$$
is exact, so the image of the boundary map lies in the kernel of $i_*$.
:::

<1>4. A retraction $r:M\to\partial M$ would make $i_*$ injective.
::: {.proof}
If $r\circ i=\operatorname{id}_{\partial M}$, then
$$
r_*\circ i_*=\operatorname{id}_{H_*(\partial M)},
$$
so $i_*$ has a left inverse.
:::

<1>5. Therefore no such retraction exists.
::: {.proof}
The nonzero class in <1>2 is killed by $i_*$ in <1>3, contradicting injectivity from <1>4.
:::
:::

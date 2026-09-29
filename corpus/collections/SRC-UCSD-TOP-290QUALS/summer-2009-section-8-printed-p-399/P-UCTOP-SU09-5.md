---
schema: qual/card@1
id: P-UCTOP-SU09-5
kind: problem
title: No retraction from compact manifold to its boundary
classification:
  areas:
  - topology
  topics:
  - Manifolds
relations: []
review: draft
---

::: {.problem}
Show that if $M$ is a compact orientable manifold with boundary $\partial M$, then there does not exist a retraction $r : M \to \partial M$.
:::

::: {.solution}

::: pf

::: pf-step
Let $M$ be connected of dimension $n$ with nonempty boundary, and let
$$
i:\partial M\hookrightarrow M
$$
be the inclusion.

::: pf-proof
If $M$ is disconnected, the argument applies to any component meeting the boundary. If the boundary is empty, a retraction onto it is impossible for a nonempty manifold.
:::

:::

::: {.pf-step #boundary-sends-to-fundamental-class}
The boundary homomorphism in the long exact sequence of the pair sends the relative fundamental class to the fundamental class of the boundary:
$$
\partial[M,\partial M]=[\partial M]\in H_{n-1}(\partial M;\mathbb Z).
$$

::: pf-proof
This is the standard boundary formula for the relative fundamental class of a compact oriented manifold. With the boundary orientation, $[\partial M]$ is the sum of the fundamental classes of the boundary components and is nonzero.
:::

:::

::: {.pf-step #boundary-class-killed}
Consequently
$$
i_*[\partial M]=0.
$$

::: pf-proof
Exactness of
$$
H_n(M,\partial M)\xrightarrow{\partial}H_{n-1}(\partial M)
\xrightarrow{i_*}H_{n-1}(M)
$$
shows that every element in the image of $\partial$ lies in the kernel of $i_*$. Apply step [](#boundary-sends-to-fundamental-class){.pf-ref}.
:::

:::

::: {.pf-step #retraction-implies-injective}
If a retraction $r:M\to\partial M$ existed, then $i_*$ would be injective on homology.

::: pf-proof
A retraction satisfies $r\circ i=\operatorname{id}_{\partial M}$. Therefore
$$
r_*\circ i_*=\operatorname{id}_{H_*(\partial M)},
$$
so $i_*$ has a left inverse and is injective.
:::

:::

::: pf-step
This contradicts steps [](#boundary-sends-to-fundamental-class){.pf-ref} and [](#boundary-class-killed){.pf-ref}. Hence no retraction $M\to\partial M$ exists.

::: pf-proof
The nonzero class $[\partial M]$ lies in $\ker i_*$, contradicting injectivity from step [](#retraction-implies-injective){.pf-ref}.
:::

:::

:::

:::


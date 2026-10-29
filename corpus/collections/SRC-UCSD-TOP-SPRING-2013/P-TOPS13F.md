---
schema: qual/card@1
id: P-TOPS13F
kind: problem
title: 'A $\ZZ/5$-orientable manifold is orientable'
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
Let $M$ be a $\ZZ_5$-orientable manifold.
Show that $M$ is orientable.
:::

::: {.solution}

::: pf

::: pf-step
The orientation local system has monodromy
$$
w:\pi_1(M)\to\{\pm1\},
$$
where $w(\gamma)=-1$ exactly for orientation-reversing loops.

::: pf-proof
Transport of a local integral orientation around a loop either preserves or reverses its sign.
:::

:::

::: pf-step
Reducing the orientation local system modulo $5$, an orientation-reversing loop acts by multiplication by $-1\equiv4\pmod5$, which is not the identity.

::: pf-proof
The two units $1$ and $-1$ are distinct in $\ZZ/5$.
:::

:::

::: pf-step
Since $M$ is $\ZZ_5$-orientable, the mod-$5$ orientation local system is trivial, so no loop can act by $-1$.

::: pf-proof
A global $\ZZ_5$-orientation is precisely a trivialization of the rank-one orientation local system over $\ZZ/5$, forcing trivial monodromy.
:::

:::

::: pf-step
Hence $w$ is trivial and
$$
\boxed{M\text{ is orientable}.}
$$

::: pf-proof
Triviality of the integral orientation character is equivalent to orientability.
:::

:::

:::

:::

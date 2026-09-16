---
schema: qual/card@1
id: P-TOPS13F
kind: problem
title: "Z5-orientable manifold is orientable"
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
Let $M$ be a $\mathbb{Z}_5$-orientable manifold.
Show that $M$ is orientable.
:::

::: {.solution}
<1>1. The orientation local system has monodromy
$$
w:\pi_1(M)\to\{\pm1\},
$$
where $w(\gamma)=-1$ exactly for orientation-reversing loops.
::: {.proof}
Transport of a local integral orientation around a loop either preserves or reverses its sign.
:::

<1>2. Reducing the orientation local system modulo $5$, an orientation-reversing loop acts by multiplication by $-1\equiv4\pmod5$, which is not the identity.
::: {.proof}
The two units $1$ and $-1$ are distinct in $\mathbb Z/5$.
:::

<1>3. Since $M$ is $\mathbb Z_5$-orientable, the mod-$5$ orientation local system is trivial, so no loop can act by $-1$.
::: {.proof}
A global $\mathbb Z_5$-orientation is precisely a trivialization of the rank-one orientation local system over $\mathbb Z/5$, forcing trivial monodromy.
:::

<1>4. Hence $w$ is trivial and
$$
\boxed{M\text{ is orientable}.}
$$
::: {.proof}
Triviality of the integral orientation character is equivalent to orientability.
:::
:::

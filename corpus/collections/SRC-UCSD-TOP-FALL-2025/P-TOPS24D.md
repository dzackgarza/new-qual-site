---
schema: qual/card@1
id: P-TOPS24D
kind: problem
title: The cube with opposite faces glued by $180^\circ$ rotations is $\RP^3$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Cell Complexes
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $X$ be the space obtained by gluing opposite pairs of faces of a standard cube $I^3$ via 180 degree rotations, as shown.
Compute the homology $H_*(X; \ZZ)$.
:::

::: {.solution}

::: pf

::: {.pf-step #antipodal}

Every face pairing is the restriction of the point reflection
$$\sigma:I^3\to I^3,\qquad \sigma(p)=(1,1,1)-p,$$
through the centre of the cube.

::: pf-proof

Take the front face $y=0$. The $180^\circ$ rotation of the face about its centre is $(x,z)\mapsto(1-x,1-z)$, so the front face is glued to the back face by $(x,0,z)\mapsto(1-x,1,1-z)=\sigma(x,0,z)$. The same computation holds for the other two pairs. A half-turn about the face centre is the only $180^\circ$ rotation of the face, so the figure does not change this.

:::

:::

::: {.pf-step #rp3}

$X\cong\RP^3$.

::: pf-proof

The map $\sigma$ is the antipodal map of the cube about its centre. The cube with antipodal boundary points identified is homeomorphic to the closed $3$-ball with antipodal boundary points identified, by radial projection from the centre, which commutes with $\sigma$. That quotient is $\RP^3$: it is the upper hemisphere of $S^3$, a fundamental domain for $x\mapsto-x$, with antipodal points of its equator identified.

:::

:::

::: pf-qed

By Step [](#rp3){.pf-ref} and the cellular chain complex $\ZZ\xrightarrow{0}\ZZ\xrightarrow{2}\ZZ\xrightarrow{0}\ZZ$ of $\RP^3$,
$$
\boxed{H_k(X;\ZZ)\cong
\begin{cases}
\ZZ,&k=0,3,\\
\ZZ/2,&k=1,\\
0,&\text{otherwise.}
\end{cases}}
$$

:::

:::

:::

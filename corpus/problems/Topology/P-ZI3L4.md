---
schema: qual/card@1
id: P-ZI3L4
kind: problem
title: Fundamental group of $S^2$ with equatorial antipodes identified
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Cell Complexes
  - Quotient Spaces
relations: []
review: draft
---

::: {.problem}
- Compute $\pi_1(X)$ where $X \definedas S^2/\sim$, where $x\sim -x$ only for $x$ on the equator $S^1 \injects S^2$.

  - Hint: try cellular homology.
    Should yield $[\ZZ, \ZZ/2\ZZ, \ZZ, 0, \cdots]$.
:::

::: {.solution}

::: pf

::: pf-step

The quotient of the equator by $x\sim -x$ is again a circle; call its generator $a$.

::: pf-proof

The antipodal quotient map $S^1\to S^1/(x\sim -x)$ is the degree-$2$ covering of a circle by a circle.

:::

:::

::: pf-step

The northern and southern hemispheres descend to two $2$-cells, each attached to this quotient circle by a degree-$2$ map.

::: pf-proof

Each hemisphere boundary is the original equator, and after passing to the quotient its attaching map is precisely the antipodal quotient $S^1\to S^1/(\pm1)$, of degree $2$ up to orientation.

:::

:::

::: pf-step

Hence van Kampen gives
$$\pi_1(X)\cong\langle a\mid a^2,a^2\rangle\cong\boxed{\mathbb Z/2}.$$

::: pf-proof

Attaching either $2$-cell kills $a^2$; the second gives the same relation up to inversion.

:::

:::

::: pf-step

The same CW complex has cellular boundary $\partial_2:\mathbb Z^2\to\mathbb Z$ given by $(m,n)\mapsto2m\pm2n$, so
$$H_2(X)\cong\mathbb Z,\qquad H_1(X)\cong\mathbb Z/2,$$
in agreement with the hint.

::: pf-proof

The image is $2\mathbb Z$ and the kernel has rank $1$.

:::

:::

:::

:::

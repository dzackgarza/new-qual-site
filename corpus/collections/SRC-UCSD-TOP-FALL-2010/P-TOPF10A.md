---
schema: qual/card@1
id: P-TOPF10A
kind: problem
title: "Fundamental group and homology of two solid tori glued by the identity"
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Homology
  - Heegaard Splittings
  - Manifolds
relations: []
review: draft
---

::: {.problem}
Let $X$ be a space formed by gluing two distinct copies of the solid torus $S^1 \times B^2$ along their boundary $S^1 \times S^1$, via the identity map.
Calculate the fundamental group and homology groups of $X$.
:::

::: {.solution}
<1>1. Since the gluing is the identity on the boundary product,
$$
X\cong S^1\times\bigl(B^2\cup_{S^1}B^2\bigr).
$$
::: {.proof}
Write each solid torus as $S^1\times B^2$. The two copies are glued along $S^1\times\partial B^2$ by the identity in both factors, so the quotient factors as the product of $S^1$ with the double of the disk.
:::

<1>2. The double of $B^2$ along its boundary is $S^2$. Hence
$$
X\cong S^1\times S^2.
$$
::: {.proof}
Two disks glued along their boundary circle form a $2$-sphere.
:::

<1>3. Therefore
$$
\boxed{\pi_1(X)\cong\mathbb Z}.
$$
::: {.proof}
The sphere factor is simply connected.
:::

<1>4. By Künneth,
$$
\boxed{H_i(X;\mathbb Z)\cong
\begin{cases}\mathbb Z,&i=0,1,2,3,\\0,&\text{otherwise}.\end{cases}}
$$
::: {.proof}
The only nonzero homology groups of $S^1$ are in degrees $0,1$, and those of $S^2$ are in degrees $0,2$; all are free, so there are no Tor terms.
:::
:::

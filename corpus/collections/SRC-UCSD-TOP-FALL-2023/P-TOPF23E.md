---
schema: qual/card@1
id: P-TOPF23E
kind: problem
title: "Homology and cohomology of K x K where K is the Klein bottle"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Cohomology
  - Künneth Formula
  - Surfaces
relations: []
review: draft
---

::: {.problem}
Let $K$ be the Klein bottle.
Compute the homology groups $H_*(K \times K; \mathbb{Z})$ and cohomology groups $H^*(K \times K; \mathbb{Z})$ (you don't need to work out the ring structure on the cohomology).
:::

::: {.solution}

::: pf

::: pf-step

For the Klein bottle $K$,
$$H_i(K;\mathbb Z)\cong\begin{cases}
\mathbb Z,&i=0,\\
\mathbb Z\oplus\mathbb Z/2,&i=1,\\
0,&i\ge2.
\end{cases}$$

::: pf-proof

This is the standard cellular homology computation for the Klein bottle.

:::

:::

::: {.pf-step #s2}

The integral homology of $K\times K$ is
$$\boxed{H_i(K\times K;\mathbb Z)\cong\begin{cases}
\mathbb Z,&i=0,\\
\mathbb Z^2\oplus(\mathbb Z/2)^2,&i=1,\\
\mathbb Z\oplus(\mathbb Z/2)^3,&i=2,\\
\mathbb Z/2,&i=3,\\
0,&i\ge4.
\end{cases}}$$

::: pf-proof

Apply the integral Künneth theorem to $A=H_1(K)=\mathbb Z\oplus\mathbb Z/2$. In degree $2$, $A\otimes A\cong\mathbb Z\oplus(\mathbb Z/2)^3$. In degree $3$, the only contribution is $\operatorname{Tor}(A,A)\cong\mathbb Z/2$.

:::

:::

::: pf-step

The integral cohomology groups are
$$\boxed{H^i(K\times K;\mathbb Z)\cong\begin{cases}
\mathbb Z,&i=0,\\
\mathbb Z^2,&i=1,\\
\mathbb Z\oplus(\mathbb Z/2)^2,&i=2,\\
(\mathbb Z/2)^3,&i=3,\\
\mathbb Z/2,&i=4,\\
0,&i>4.
\end{cases}}$$

::: pf-proof

Use the universal coefficient theorem
$$0\to\operatorname{Ext}(H_{i-1},\mathbb Z)\to H^i\to\operatorname{Hom}(H_i,\mathbb Z)\to0$$
and the homology groups from step [](#s2){.pf-ref}. The free parts contribute through Hom and the finite torsion summands through Ext one degree later.

:::

:::

:::

:::

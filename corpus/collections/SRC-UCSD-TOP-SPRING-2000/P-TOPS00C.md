---
schema: qual/card@1
id: P-TOPS00C
kind: problem
title: "Cohomology ring of CP^3 x RP^2"
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Cup Product
  - Projective Spaces
relations: []
review: draft
---

::: problem
Compute the cohomology ring of $\mathbb{CP}^3 \times \mathbb{RP}^2$.
:::

::: {.solution}
<1>1. The integral cohomology rings of the two factors are
$$
H^*(\mathbb{CP}^3;\mathbb Z)\cong\mathbb Z[x]/(x^4),\qquad |x|=2,
$$
and
$$
H^*(\mathbb{RP}^2;\mathbb Z)\cong \mathbb Z\cdot1\oplus(\mathbb Z/2)u,\qquad |u|=2,\quad u^2=0.
$$
::: {.proof}
The first is the standard projective-space computation. For $\mathbb{RP}^2$, integral homology is $H_0=\mathbb Z$, $H_1=\mathbb Z/2$, $H_2=0$; the cohomological universal coefficient theorem gives $H^2\cong\mathbb Z/2$ and no other positive-degree cohomology. Dimensional reasons give $u^2=0$.
:::

<1>2. Since $H^*(\mathbb{CP}^3;\mathbb Z)$ is free abelian, the cohomological Künneth theorem has no Tor contribution and the external cup product gives the product ring.
::: {.proof}
Tensoring with a free abelian group is exact, so the integral Künneth short exact sequences reduce to tensor products. Naturality of the external product identifies the multiplicative structure.
:::

<1>3. Therefore
$$
\boxed{H^*(\mathbb{CP}^3\times\mathbb{RP}^2;\mathbb Z)
\cong
\mathbb Z[x,u]/(x^4,\,2u,\,u^2),\qquad |x|=|u|=2.}
$$
::: {.proof}
The additive basis consists of $1,x,x^2,x^3$ and the four $2$-torsion classes $u,xu,x^2u,x^3u$. The displayed relations give exactly these groups and the Künneth multiplication from <1>2.
:::
:::

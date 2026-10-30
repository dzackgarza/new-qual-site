---
schema: qual/card@1
id: P-TOPS00C
kind: problem
title: 'Cohomology ring of $\CP^3\times\RP^2$'
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

::: {.problem}
Compute the cohomology ring of $\CP^3 \times \RP^2$.
:::

::: {.solution}

::: pf

::: pf-step

The integral cohomology rings of the two factors are
$$
H^*(\CP^3;\ZZ)\cong\ZZ[x]/(x^4),\qquad \gradeddegree{x}=2,
$$
and
$$
H^*(\RP^2;\ZZ)\cong \ZZ\cdot1\oplus(\ZZ/2)u,\qquad \gradeddegree{u}=2,\quad u^2=0.
$$

::: pf-proof

The first is the standard projective-space computation. For $\RP^2$, integral homology is $H_0=\ZZ$, $H_1=\ZZ/2$, $H_2=0$; the cohomological universal coefficient theorem gives $H^2\cong\ZZ/2$ and no other positive-degree cohomology. Dimensional reasons give $u^2=0$.

:::

:::

::: {.pf-step #s2}

Since $H^*(\CP^3;\ZZ)$ is free abelian, the cohomological Künneth theorem has no Tor contribution and the external cup product gives the product ring.

::: pf-proof

Tensoring with a free abelian group is exact, so the integral Künneth short exact sequences reduce to tensor products. Naturality of the external product identifies the multiplicative structure.

:::

:::

::: pf-step

Therefore
$$
\boxed{H^*(\CP^3\times\RP^2;\ZZ)
\cong
\ZZ[x,u]/(x^4,\,2u,\,u^2),\qquad \gradeddegree{x}=\gradeddegree{u}=2.}
$$

::: pf-proof

The additive basis consists of $1,x,x^2,x^3$ and the four $2$-torsion classes $u,xu,x^2u,x^3u$. The displayed relations give exactly these groups and the Künneth multiplication from step [](#s2){.pf-ref}.

:::

:::

:::

:::

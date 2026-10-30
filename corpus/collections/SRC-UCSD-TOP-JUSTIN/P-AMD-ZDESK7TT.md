---
schema: qual/card@1
id: P-AMD-ZDESK7TT
kind: problem
title: Homology of the closed orientable surface of genus $g$
classification:
  areas:
    - topology
  topics:
    - Surfaces
    - Classification
relations: []
review: draft
---

::: {.problem}
Use cellular chain complexes to compute the homology of the closed orientable surface of genus $g$. For $g=2$, the surface is the octagon with gluing pattern $a+b-a-b+c+d-c-d$.
:::

::: {.solution}

::: pf

::: {.pf-step #cw}

The closed orientable surface $\Sigma_g$ of genus $g\ge1$ is the quotient of a $4g$-gon by the boundary word
$$
a_1b_1a_1^{-1}b_1^{-1}\cdots a_gb_ga_g^{-1}b_g^{-1},
$$
which for $g=2$ is the pattern $a+b-a-b+c+d-c-d$ of the figure. This gives a CW structure with one $0$-cell, $2g$ $1$-cells $a_i,b_i$ and one $2$-cell.

::: pf-proof

The square with word $aba^{-1}b^{-1}$ is the torus, and the connected sum of $g$ tori is the polygon whose word is the product of the $g$ commutators. In this polygon every corner is identified to one point: the corners at the start and end of each commutator block are identified by the block, and consecutive blocks share a corner.

:::

:::

::: {.pf-step #diff}

Both cellular differentials are zero.

::: pf-proof

The cellular boundary of the $2$-cell is the sum of the exponents of each letter in the attaching word, and each $a_i$ and $b_i$ occurs once with exponent $+1$ and once with exponent $-1$. Each $1$-cell starts and ends at the single $0$-cell, so $d_1=0$.

:::

:::

::: pf-qed

The cellular chain complex $\ZZ\xrightarrow{0}\ZZ^{2g}\xrightarrow{0}\ZZ$ of Steps [](#cw){.pf-ref} and [](#diff){.pf-ref} gives
$$
\boxed{H_0(\Sigma_g)\cong\ZZ,\qquad H_1(\Sigma_g)\cong\ZZ^{2g},\qquad H_2(\Sigma_g)\cong\ZZ,}
$$
and $H_k(\Sigma_g)=0$ for $k\ge3$. For $g=0$, $\Sigma_0=S^2$ has $H_0=H_2=\ZZ$ and $H_1=0$, which is the same formula.

:::

:::

:::

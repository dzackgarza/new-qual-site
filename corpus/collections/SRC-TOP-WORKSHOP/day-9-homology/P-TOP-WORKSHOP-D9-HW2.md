---
schema: qual/card@1
id: P-TOP-WORKSHOP-D9-HW2
kind: problem
title: Homology of the torus $T^2=S^1\times S^1$
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement read from the card in `corpus/collections/SRC-TOP-WORKSHOP`; no correction is claimed.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    Computed on the product cell structure: one $0$-cell, two $1$-cells, one $2$-cell, with the
    boundary of the $2$-cell equal to $aba^{-1}b^{-1}$ whose image in $H_1$ is $a+a-b-b=0$. So
    $H_0=\ZZ$, $H_1=\ZZ^2$, $H_2=\ZZ$, everything else $0$; the vanishing of $H_2\to H_1$ is
    proved, not assumed. Nothing is left in outline.
---
---

::: {.problem}
Compute the homology of the torus $T^2=S^1\times S^1$.
:::

::: {.solution}

Let $T^2=S^1\times S^1$, given as a CW complex with the product cell structure.

::: pf

::: {.pf-step #s1}

$T^2$ has a CW structure with one $0$-cell $e^0$, two $1$-cells $a,b$, and one $2$-cell $e^2$.

::: pf-proof

Take the standard circle CW structure with one $0$-cell and one $1$-cell in each factor. The product of two CW complexes has cells the products of cells, with $\dim(X\times Y)$-cells being pairs of cells whose dimensions sum to the total. Hence $T^2$ has one cell of dimension $0$ (the product of the two $0$-cells), two of dimension $1$ ($0$-cell × $1$-cell and $1$-cell × $0$-cell), and one of dimension $2$.

:::

:::

::: {.pf-step #s2}

The cellular chain complex is
$$
0\longrightarrow\ZZ\xrightarrow{\ \partial_2\ } \ZZ^2\xrightarrow{\ \partial_1\ }\ZZ\longrightarrow0,
$$
and $\partial_1=0$, $\partial_2=0$.

::: pf-proof

The differential $\partial_1$ counts the endpoints of each $1$-cell with signs; both $1$-cells are loops at the single $0$-cell, so $\partial_1(a)=\partial_1(b)=0$.

For $\partial_2$: the $2$-cell is attached along the commutator loop $aba^{-1}b^{-1}$. The cellular boundary of $e^2$ is computed by projecting the attaching map onto the $1$-skeleton modulo the $0$-skeleton and taking degrees, so $\partial_2(e^2)=d_a\,a+d_b\,b$ where $d_a$, $d_b$ are the degrees of the composite $S^1\to X^{(1)}\to X^{(1)}/X^{(0)}=S^1\vee S^1\to S^1$ onto each wedge summand. The composite of the attaching map $aba^{-1}b^{-1}$ with either projection is the loop $t\mapsto t^{1+(-1)}=t^0$, i.e. constant, because abelianising the word gives $1-1+1-1=0$. Hence $d_a=d_b=0$ and $\partial_2=0$.

:::

:::

::: {.pf-step #s3}

$H_0(T^2;\ZZ)=\ZZ$, $H_1(T^2;\ZZ)=\ZZ^2$, $H_2(T^2;\ZZ)=\ZZ$, and $H_i=0$ for $i\ge3$.

::: pf-proof

The homology of a CW complex is the homology of its cellular chain complex, and all cell dimensions here are $\le2$, so $H_i=0$ for $i\ge3$.

With both differentials zero by step [](#s2){.pf-ref},
$$
H_0=\ker\partial_0/\operatorname{im}\partial_1=C_0/0\cong\ZZ^1\cong\ZZ,\qquad
H_1=\ker\partial_1/\operatorname{im}\partial_2=\ZZ^2/0\cong\ZZ^2,\qquad
H_2=\ker\partial_2/\operatorname{im}\partial_3=\ZZ/0\cong\ZZ .
$$

:::

:::

::: {.pf-step #s4}

Consistency: these agree with $T^2=S^1\times S^1$ as a product and with its Euler characteristic.

::: pf-proof

By the Künneth formula over the field $\QQ$, $H_*(T^2;\QQ)\cong H_*(S^1;\QQ)\otimes H_*(S^1;\QQ)$ has dimensions $1,2,1$ in degrees $0,1,2$, matching $\operatorname{rk}H_i=\operatorname{rank}$ of the groups found in step [](#s3){.pf-ref}. The Euler characteristic is $1-2+1=0$, as it must be for a closed orientable surface of genus $1$.

:::

:::

:::

:::

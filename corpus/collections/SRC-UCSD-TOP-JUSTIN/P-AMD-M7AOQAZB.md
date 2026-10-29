---
schema: qual/card@1
id: P-AMD-M7AOQAZB
kind: problem
title: A space with $H_*=(\ZZ,\ZZ_6,\ZZ_{12},\ZZ\oplus\ZZ_4)$ in degrees $0$–$3$ and
  vanishing above, and its cohomology
classification:
  areas:
  - topology
  topics:
  - Homology
  - Cell Complexes
  - Cohomology
relations: []
review: draft
---

::: {.problem}
Construct a space $X$ such that $H_*(X; \ZZ) = (\ZZ, \ZZ_6, \ZZ_{12}, \ZZ \oplus \ZZ_4, 0 \cdots)$ Compute $H^*(X; \ZZ)$
:::

::: {.solution}

::: pf

::: pf-step

For an abelian group $A$ and $r\ge1$, let $M(A,r)$ denote a Moore space with
$$
\widetilde H_i(M(A,r);\ZZ)\cong
\begin{cases}
A,&i=r,\\
0,&i\ne r.
\end{cases}
$$
For $A=\ZZ/m$, one may take
$$
M(\ZZ/m,r)=S^r\cup_m e^{r+1},
$$
where the top cell is attached by a degree-$m$ map.

::: pf-proof

Its cellular chain complex in the two positive dimensions is
$$
0\to\ZZ\xrightarrow{m}\ZZ\to0,
$$
so the only reduced homology is $\ZZ/m$ in degree $r$.

:::

:::

::: pf-step

Take
$$
X=M(\ZZ/6,1)\vee M(\ZZ/12,2)
\vee S^3\vee M(\ZZ/4,3).
$$
Then
$$
H_i(X;\ZZ)\cong
\begin{cases}
\ZZ,&i=0,\\
\ZZ/6,&i=1,\\
\ZZ/12,&i=2,\\
\ZZ\oplus\ZZ/4,&i=3,\\
0,&i\ge4.
\end{cases}
$$

::: pf-proof

Reduced homology takes wedges of connected CW complexes to direct sums. Each summand contributes exactly the indicated group in its designated degree.

:::

:::

::: pf-step

The cohomological universal coefficient theorem gives
$$
0\to\operatorname{Ext}(H_{i-1}(X),\ZZ)
\to H^i(X;\ZZ)
\to\operatorname{Hom}(H_i(X),\ZZ)\to0.
$$

::: pf-proof

This is the universal coefficient short exact sequence for integral cohomology.

:::

:::

::: pf-step

Therefore
$$
\boxed{H^i(X;\ZZ)\cong
\begin{cases}
\ZZ,&i=0,\\
0,&i=1,\\
\ZZ/6,&i=2,\\
\ZZ\oplus\ZZ/12,&i=3,\\
\ZZ/4,&i=4,\\
0,&i\ge5.
\end{cases}}
$$

::: pf-proof

Use
$$
\operatorname{Hom}(\ZZ/m,\ZZ)=0,
\qquad
\operatorname{Ext}(\ZZ/m,\ZZ)\cong\ZZ/m,
$$
and
$$
\operatorname{Hom}(\ZZ\oplus\ZZ/4,\ZZ)\cong\ZZ,
\qquad
\operatorname{Ext}(\ZZ\oplus\ZZ/4,\ZZ)\cong\ZZ/4.
$$
In degree $3$ the short exact sequence
$$
0\to\ZZ/12\to H^3(X)\to\ZZ\to0
$$
splits because $\ZZ$ is free, yielding $H^3(X)\cong\ZZ\oplus\ZZ/12$.

:::

:::

:::

:::

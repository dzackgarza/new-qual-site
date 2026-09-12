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
<1>1. For an abelian group $A$ and $r\ge1$, let $M(A,r)$ denote a Moore space with
$$
\widetilde H_i(M(A,r);\mathbb Z)\cong
\begin{cases}
A,&i=r,\\
0,&i\ne r.
\end{cases}
$$
For $A=\mathbb Z/m$, one may take
$$
M(\mathbb Z/m,r)=S^r\cup_m e^{r+1},
$$
where the top cell is attached by a degree-$m$ map.
::: {.proof}
Its cellular chain complex in the two positive dimensions is
$$
0\to\mathbb Z\xrightarrow{m}\mathbb Z\to0,
$$
so the only reduced homology is $\mathbb Z/m$ in degree $r$.
:::

<1>2. Take
$$
X=M(\mathbb Z/6,1)\vee M(\mathbb Z/12,2)
\vee S^3\vee M(\mathbb Z/4,3).
$$
Then
$$
H_i(X;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=0,\\
\mathbb Z/6,&i=1,\\
\mathbb Z/12,&i=2,\\
\mathbb Z\oplus\mathbb Z/4,&i=3,\\
0,&i\ge4.
\end{cases}
$$
::: {.proof}
Reduced homology takes wedges of connected CW complexes to direct sums. Each summand contributes exactly the indicated group in its designated degree.
:::

<1>3. The cohomological universal coefficient theorem gives
$$
0\to\operatorname{Ext}(H_{i-1}(X),\mathbb Z)
\to H^i(X;\mathbb Z)
\to\operatorname{Hom}(H_i(X),\mathbb Z)\to0.
$$
::: {.proof}
This is the universal coefficient short exact sequence for integral cohomology.
:::

<1>4. Therefore
$$
\boxed{H^i(X;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=0,\\
0,&i=1,\\
\mathbb Z/6,&i=2,\\
\mathbb Z\oplus\mathbb Z/12,&i=3,\\
\mathbb Z/4,&i=4,\\
0,&i\ge5.
\end{cases}}
$$
::: {.proof}
Use
$$
\operatorname{Hom}(\mathbb Z/m,\mathbb Z)=0,
\qquad
\operatorname{Ext}(\mathbb Z/m,\mathbb Z)\cong\mathbb Z/m,
$$
and
$$
\operatorname{Hom}(\mathbb Z\oplus\mathbb Z/4,\mathbb Z)\cong\mathbb Z,
\qquad
\operatorname{Ext}(\mathbb Z\oplus\mathbb Z/4,\mathbb Z)\cong\mathbb Z/4.
$$
In degree $3$ the short exact sequence
$$
0\to\mathbb Z/12\to H^3(X)\to\mathbb Z\to0
$$
splits because $\mathbb Z$ is free, yielding $H^3(X)\cong\mathbb Z\oplus\mathbb Z/12$.
:::
:::

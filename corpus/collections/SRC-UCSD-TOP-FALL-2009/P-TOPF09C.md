---
schema: qual/card@1
id: P-TOPF09C
kind: problem
title: "Integral homology of Y x RP^2 where Y is S^3 with a 4-cell attached by degree 6"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Cell Complexes
  - Projective Spaces
relations: []
review: draft
---

::: problem
Let $Y$ be a space obtained by attaching a $4$-ball, via a degree $6$ map of its boundary, to a $3$-sphere.
Calculate the integral homology $H^*(Y \times \mathbb{RP}^2; \mathbb{Z})$.
:::

::: {.solution}
<1>1. The cellular chain complex of $Y$ in positive dimensions is
$$
0\longrightarrow \mathbb Z\xrightarrow{6}\mathbb Z\longrightarrow0
$$
concentrated in degrees $4$ and $3$. Hence
$$
H_i(Y;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=0,\\
\mathbb Z/6,&i=3,\\
0,&\text{otherwise}.
\end{cases}
$$
::: {.proof}
The attaching map of the $4$-cell has degree $6$, so the cellular boundary $C_4\to C_3$ is multiplication by $6$.
:::

<1>2. The integral homology of $\mathbb{RP}^2$ is
$$
H_0\cong\mathbb Z,\qquad H_1\cong\mathbb Z/2,
$$
with all higher groups zero.
::: {.proof}
This is the standard cellular calculation for $\mathbb{RP}^2$.
:::

<1>3. The Künneth theorem gives
$$
\boxed{
H_i(Y\times\mathbb{RP}^2;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=0,\\
\mathbb Z/2,&i=1,4,5,\\
\mathbb Z/6,&i=3,\\
0,&\text{otherwise}.
\end{cases}}
$$
::: {.proof}
The tensor contribution $H_3(Y)\otimes H_1(\mathbb{RP}^2)$ is $\mathbb Z/2$ in degree $4$, while
$$
\operatorname{Tor}(\mathbb Z/6,\mathbb Z/2)\cong\mathbb Z/2
$$
contributes in degree $5$. The remaining nonzero tensor terms are $H_0(Y)\otimes H_0(\mathbb{RP}^2)\cong\mathbb Z$ in degree $0$, $H_0(Y)\otimes H_1(\mathbb{RP}^2)\cong\mathbb Z/2$ in degree $1$, and $H_3(Y)\otimes H_0(\mathbb{RP}^2)\cong\mathbb Z/6$ in degree $3$.
:::

<1>4. If the notation $H^*$ in the question was intended literally, the integral cohomology groups are
$$
H^i(Y\times\mathbb{RP}^2;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=0,\\
\mathbb Z/2,&i=2,5,6,\\
\mathbb Z/6,&i=4,\\
0,&\text{otherwise}.
\end{cases}
$$
::: {.proof}
Apply the universal coefficient theorem for cohomology to the homology groups in <1>3. Since all positive-degree homology is finite, Hom into $\mathbb Z$ vanishes there and the torsion reappears one degree higher through Ext.
:::
:::

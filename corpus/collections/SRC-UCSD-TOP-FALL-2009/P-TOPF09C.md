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

::: {.problem}
Let $Y$ be a space obtained by attaching a $4$-ball, via a degree $6$ map of its boundary, to a $3$-sphere.
Calculate the integral homology $H^*(Y \times \RP^2; \ZZ)$.
:::

::: {.solution}

::: pf

::: pf-step

The cellular chain complex of $Y$ in positive dimensions is
$$
0\longrightarrow \ZZ\xrightarrow{6}\ZZ\longrightarrow0
$$
concentrated in degrees $4$ and $3$. Hence
$$
H_i(Y;\ZZ)\cong
\begin{cases}
\ZZ,&i=0,\\
\ZZ/6,&i=3,\\
0,&\text{otherwise}.
\end{cases}
$$

::: pf-proof

The attaching map of the $4$-cell has degree $6$, so the cellular boundary $C_4\to C_3$ is multiplication by $6$.

:::

:::

::: pf-step

The integral homology of $\RP^2$ is
$$
H_0\cong\ZZ,\qquad H_1\cong\ZZ/2,
$$
with all higher groups zero.

::: pf-proof

This is the standard cellular calculation for $\RP^2$.

:::

:::

::: {.pf-step #s3}

The Künneth theorem gives
$$
\boxed{
H_i(Y\times\RP^2;\ZZ)\cong
\begin{cases}
\ZZ,&i=0,\\
\ZZ/2,&i=1,4,5,\\
\ZZ/6,&i=3,\\
0,&\text{otherwise}.
\end{cases}}
$$

::: pf-proof

The tensor contribution $H_3(Y)\otimes H_1(\RP^2)$ is $\ZZ/2$ in degree $4$, while
$$
\operatorname{Tor}(\ZZ/6,\ZZ/2)\cong\ZZ/2
$$
contributes in degree $5$. The remaining nonzero tensor terms are $H_0(Y)\otimes H_0(\RP^2)\cong\ZZ$ in degree $0$, $H_0(Y)\otimes H_1(\RP^2)\cong\ZZ/2$ in degree $1$, and $H_3(Y)\otimes H_0(\RP^2)\cong\ZZ/6$ in degree $3$.

:::

:::

::: pf-step

If the notation $H^*$ in the question was intended literally, the integral cohomology groups are
$$
H^i(Y\times\RP^2;\ZZ)\cong
\begin{cases}
\ZZ,&i=0,\\
\ZZ/2,&i=2,5,6,\\
\ZZ/6,&i=4,\\
0,&\text{otherwise}.
\end{cases}
$$

::: pf-proof

Apply the universal coefficient theorem for cohomology to the homology groups in step [](#s3){.pf-ref}. Since all positive-degree homology is finite, Hom into $\ZZ$ vanishes there and the torsion reappears one degree higher through Ext.

:::

:::

:::

:::

---
schema: qual/card@1
id: P-TOPF07C
kind: problem
title: "Integral homology of a product with RP^3"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Projective Spaces
relations: []
review: draft
---

::: problem
Let $X$ be a space whose homology groups are $\mathbb{Z}$, $0$, $\mathbb{Z}_6$ in dimensions $0$, $1$, $2$ and zero otherwise.
Compute the integral homology $H_*(X \times \mathbb{RP}^3; \mathbb{Z})$.
:::

::: {.solution}
<1>1. The nonzero homology groups of the factors are
$$
H_0(X)=\mathbb Z,\quad H_2(X)=\mathbb Z/6,
$$
and
$$
H_0(\mathbb{RP}^3)=\mathbb Z,\quad H_1(\mathbb{RP}^3)=\mathbb Z/2,\quad H_3(\mathbb{RP}^3)=\mathbb Z.
$$
::: {.proof}
The groups for $X$ are given. The projective-space groups follow from its standard cellular chain complex.
:::

<1>2. The tensor terms in Künneth give
$$
H_0=\mathbb Z,\ H_1=\mathbb Z/2,\ H_2=\mathbb Z/6,
$$
$$
H_3\supset\mathbb Z\oplus\mathbb Z/2,\qquad H_5\supset\mathbb Z/6.
$$
::: {.proof}
Besides the terms with $H_0$, one has
$$
H_2(X)\otimes H_1(\mathbb{RP}^3)\cong\mathbb Z/2
$$
in degree $3$ and
$$
H_2(X)\otimes H_3(\mathbb{RP}^3)\cong\mathbb Z/6
$$
in degree $5$.
:::

<1>3. The only nonzero Tor contribution is
$$
\operatorname{Tor}(\mathbb Z/6,\mathbb Z/2)\cong\mathbb Z/2
$$
in degree $4$.
::: {.proof}
In the homological Künneth sequence, $\operatorname{Tor}(H_p(X),H_q(Y))$ contributes to degree $p+q+1$. The only pair of torsion groups occurs for $(p,q)=(2,1)$.
:::

<1>4. Hence
$$
\boxed{H_i(X\times\mathbb{RP}^3;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=0,\\
\mathbb Z/2,&i=1,4,\\
\mathbb Z/6,&i=2,5,\\
\mathbb Z\oplus\mathbb Z/2,&i=3,\\
0,&\text{otherwise}.
\end{cases}}
$$
::: {.proof}
The Künneth short exact sequences split (noncanonically) over $\mathbb Z$, and <1>2--<1>3 list every nonzero summand.
:::
:::

---
schema: qual/card@1
id: P-TOPF07C
kind: problem
title: 'Integral homology of a product with $\RP^3$'
classification:
  areas:
  - topology
  topics:
  - Homology
  - Projective Spaces
relations: []
review: draft
---

::: {.problem}
Let $X$ be a space whose homology groups are $\ZZ$, $0$, $\ZZ_6$ in dimensions $0$, $1$, $2$ and zero otherwise.
Compute the integral homology $H_*(X \times \RP^3; \ZZ)$.
:::

::: {.solution}

::: pf

::: pf-step

The nonzero homology groups of the factors are
$$
H_0(X)=\ZZ,\quad H_2(X)=\ZZ/6,
$$
and
$$
H_0(\RP^3)=\ZZ,\quad H_1(\RP^3)=\ZZ/2,\quad H_3(\RP^3)=\ZZ.
$$

::: pf-proof

The groups for $X$ are given. The projective-space groups follow from its standard cellular chain complex.

:::

:::

::: {.pf-step #s2}

The tensor terms in Künneth give
$$
H_0=\ZZ,\ H_1=\ZZ/2,\ H_2=\ZZ/6,
$$
$$
H_3\supset\ZZ\oplus\ZZ/2,\qquad H_5\supset\ZZ/6.
$$

::: pf-proof

Besides the terms with $H_0$, one has
$$
H_2(X)\otimes H_1(\RP^3)\cong\ZZ/2
$$
in degree $3$ and
$$
H_2(X)\otimes H_3(\RP^3)\cong\ZZ/6
$$
in degree $5$.

:::

:::

::: {.pf-step #s3}

The only nonzero Tor contribution is
$$
\operatorname{Tor}(\ZZ/6,\ZZ/2)\cong\ZZ/2
$$
in degree $4$.

::: pf-proof

In the homological Künneth sequence, $\operatorname{Tor}(H_p(X),H_q(Y))$ contributes to degree $p+q+1$. The only pair of torsion groups occurs for $(p,q)=(2,1)$.

:::

:::

::: pf-step

Hence
$$
\boxed{H_i(X\times\RP^3;\ZZ)\cong
\begin{cases}
\ZZ,&i=0,\\
\ZZ/2,&i=1,4,\\
\ZZ/6,&i=2,5,\\
\ZZ\oplus\ZZ/2,&i=3,\\
0,&\text{otherwise}.
\end{cases}}
$$

::: pf-proof

The Künneth short exact sequences split (noncanonically) over $\ZZ$, and steps [](#s2){.pf-ref} and [](#s3){.pf-ref} list every nonzero summand.

:::

:::

:::

:::

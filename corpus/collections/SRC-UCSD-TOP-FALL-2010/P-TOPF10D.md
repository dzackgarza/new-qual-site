---
schema: qual/card@1
id: P-TOPF10D
kind: problem
title: 'Integral homology of $X\times\RP^3$ where $H_*(X)=\ZZ,0,\ZZ/8$'
classification:
  areas:
  - topology
  topics:
  - Homology
  - Künneth Formula
  - Projective Spaces
relations: []
review: draft
---

::: {.problem}
Let $X$ be a space whose integral homology groups are $\ZZ$, $0$, $\ZZ_8$ in dimensions $0$, $1$, $2$, and zero otherwise.
Compute the integral homology groups of $X \times \RP^3$.
:::

::: {.solution}

::: pf

::: pf-step

The nonzero integral homology groups of the factors are
$$
H_0(X)=\ZZ,\quad H_2(X)=\ZZ/8,
$$
and
$$
H_0(\RP^3)=\ZZ,\quad H_1(\RP^3)=\ZZ/2,\quad H_3(\RP^3)=\ZZ.
$$

::: pf-proof

The groups for $X$ are the hypothesis; those for $\RP^3$ are the standard cellular homology groups.

:::

:::

::: {.pf-step #s2}

The tensor terms in Künneth give
$$
H_0=\ZZ,\quad H_1=\ZZ/2,\quad H_2=\ZZ/8,
$$
$$
H_3=\ZZ\oplus\ZZ/2,\qquad H_5=\ZZ/8.
$$

::: pf-proof

The extra $\ZZ/2$ in degree $3$ is
$$
(\ZZ/8)\otimes(\ZZ/2)\cong\ZZ/2,
$$
and the degree-$5$ term is $(\ZZ/8)\otimes\ZZ$.

:::

:::

::: {.pf-step #s3}

The only nonzero Tor contribution is
$$
\operatorname{Tor}(\ZZ/8,\ZZ/2)\cong\ZZ/2,
$$
which occurs in degree $4$.

::: pf-proof

A Tor term $\operatorname{Tor}(H_i(X),H_j(\RP^3))$ contributes to total degree $i+j+1$. The only pair of torsion groups is $(i,j)=(2,1)$.

:::

:::

::: pf-step

Therefore
$$
\boxed{H_n(X\times\RP^3;\ZZ)\cong
\begin{cases}
\ZZ,&n=0,\\
\ZZ/2,&n=1,4,\\
\ZZ/8,&n=2,5,\\
\ZZ\oplus\ZZ/2,&n=3,\\
0,&\text{otherwise}.
\end{cases}}
$$

::: pf-proof

Combine steps [](#s2){.pf-ref} and [](#s3){.pf-ref}; the Künneth short exact sequences split noncanonically over $\ZZ$.

:::

:::

:::

:::

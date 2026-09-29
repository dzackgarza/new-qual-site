---
schema: qual/card@1
id: P-TOPF10D
kind: problem
title: "Integral homology of X x RP^3 where H_*(X) = Z, 0, Z_8"
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
Let $X$ be a space whose integral homology groups are $\mathbb{Z}$, $0$, $\mathbb{Z}_8$ in dimensions $0$, $1$, $2$, and zero otherwise.
Compute the integral homology groups of $X \times \mathbb{RP}^3$.
:::

::: {.solution}

::: pf

::: pf-step

The nonzero integral homology groups of the factors are
$$
H_0(X)=\mathbb Z,\quad H_2(X)=\mathbb Z/8,
$$
and
$$
H_0(\mathbb{RP}^3)=\mathbb Z,\quad H_1(\mathbb{RP}^3)=\mathbb Z/2,\quad H_3(\mathbb{RP}^3)=\mathbb Z.
$$

::: pf-proof

The groups for $X$ are the hypothesis; those for $\mathbb{RP}^3$ are the standard cellular homology groups.

:::

:::

::: {.pf-step #s2}

The tensor terms in Künneth give
$$
H_0=\mathbb Z,\quad H_1=\mathbb Z/2,\quad H_2=\mathbb Z/8,
$$
$$
H_3=\mathbb Z\oplus\mathbb Z/2,\qquad H_5=\mathbb Z/8.
$$

::: pf-proof

The extra $\mathbb Z/2$ in degree $3$ is
$$
(\mathbb Z/8)\otimes(\mathbb Z/2)\cong\mathbb Z/2,
$$
and the degree-$5$ term is $(\mathbb Z/8)\otimes\mathbb Z$.

:::

:::

::: {.pf-step #s3}

The only nonzero Tor contribution is
$$
\operatorname{Tor}(\mathbb Z/8,\mathbb Z/2)\cong\mathbb Z/2,
$$
which occurs in degree $4$.

::: pf-proof

A Tor term $\operatorname{Tor}(H_i(X),H_j(\mathbb{RP}^3))$ contributes to total degree $i+j+1$. The only pair of torsion groups is $(i,j)=(2,1)$.

:::

:::

::: pf-step

Therefore
$$
\boxed{H_n(X\times\mathbb{RP}^3;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&n=0,\\
\mathbb Z/2,&n=1,4,\\
\mathbb Z/8,&n=2,5,\\
\mathbb Z\oplus\mathbb Z/2,&n=3,\\
0,&\text{otherwise}.
\end{cases}}
$$

::: pf-proof

Combine steps [](#s2){.pf-ref} and [](#s3){.pf-ref}; the Künneth short exact sequences split noncanonically over $\mathbb Z$.

:::

:::

:::

:::

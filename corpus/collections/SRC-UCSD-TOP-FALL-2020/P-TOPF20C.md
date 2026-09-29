---
schema: qual/card@1
id: P-TOPF20C
kind: problem
title: "Homology of RP^2 x RP^2"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Projective Spaces
  - Künneth Formula
relations: []
review: draft
---

::: {.problem}
Compute the homology group $H_k(\mathbb{RP}^2 \times \mathbb{RP}^2; \mathbb{Z})$ for all $k \geq 0$.
:::

::: {.solution}

::: pf

::: pf-step

Integrally, $H_0(\mathbb{RP}^2)=\mathbb Z$, $H_1(\mathbb{RP}^2)=\mathbb Z/2$, and all higher homology vanishes.

::: pf-proof

This is the standard cellular calculation.

:::

:::

::: {.pf-step #s2}

The tensor terms in Künneth give $\mathbb Z$ in degree $0$, $(\mathbb Z/2)^2$ in degree $1$, and $\mathbb Z/2$ in degree $2$.

::: pf-proof

The degree-$2$ term is $(\mathbb Z/2)\otimes(\mathbb Z/2)\cong\mathbb Z/2$.

:::

:::

::: {.pf-step #s3}

The only nonzero Tor term is
$$\operatorname{Tor}(\mathbb Z/2,\mathbb Z/2)\cong\mathbb Z/2,$$
and it contributes in degree $3$.

::: pf-proof

In the Künneth short exact sequence for $H_n$, Tor terms with indices summing to $n-1$ occur; here both indices are $1$.

:::

:::

::: pf-step

Hence
$$\boxed{H_k(\mathbb{RP}^2\times\mathbb{RP}^2;\mathbb Z)\cong\begin{cases}
\mathbb Z,&k=0,\\
(\mathbb Z/2)^2,&k=1,\\
\mathbb Z/2,&k=2,3,\\
0,&\text{otherwise.}
\end{cases}}$$

::: pf-proof

Combine steps [](#s2){.pf-ref} and [](#s3){.pf-ref}; the Künneth sequence splits noncanonically.

:::

:::

:::

:::

---
schema: qual/card@1
id: P-AMD-KWQELSU7
kind: problem
title: $H_*(\RP^2 \times \RP^2; \ZZ_2)$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Product Topology
relations: []
review: draft
---

::: {.problem}
Compute $H_*(\RP^2 \cross \RP^2; \ZZ_2)$
:::

::: {.solution}

::: pf

::: pf-step

With coefficients in $\FF_2=\ZZ_2$,
$$
H_i(\RP^2;\FF_2)\cong
\begin{cases}
\FF_2,&i=0,1,2,\\
0,&\text{otherwise}.
\end{cases}
$$

::: pf-proof

The standard CW structure on $\RP^2$ has one cell in each dimension $0,1,2$. Its integral cellular boundary maps are respectively $0$ and multiplication by $2$; after tensoring with $\FF_2$, both boundary maps vanish.

:::

:::

::: pf-step

Over the field $\FF_2$, the Künneth theorem gives
$$
H_n(\RP^2\times\RP^2;\FF_2)
\cong\bigoplus_{i+j=n}H_i(\RP^2;\FF_2)\otimes H_j(\RP^2;\FF_2).
$$

::: pf-proof

Over a field there are no Tor terms in the homological Künneth theorem.

:::

:::

::: pf-step

Therefore
$$
\boxed{
H_n(\RP^2\times\RP^2;\ZZ_2)
\cong
\begin{cases}
\ZZ_2,&n=0,4,\\
(\ZZ_2)^2,&n=1,3,\\
(\ZZ_2)^3,&n=2,\\
0,&\text{otherwise}.
\end{cases}}
$$

::: pf-proof

Count pairs $(i,j)\in\{0,1,2\}^2$ with $i+j=n$. Their numbers are $1,2,3,2,1$ for $n=0,1,2,3,4$ respectively, and each tensor factor is one-dimensional over $\FF_2$.

:::

:::

:::

:::

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
<1>1. With coefficients in $\mathbb F_2=\mathbb Z_2$,
$$
H_i(\mathbb{RP}^2;\mathbb F_2)\cong
\begin{cases}
\mathbb F_2,&i=0,1,2,\\
0,&\text{otherwise}.
\end{cases}
$$
::: {.proof}
The standard CW structure on $\mathbb{RP}^2$ has one cell in each dimension $0,1,2$. Its integral cellular boundary maps are respectively $0$ and multiplication by $2$; after tensoring with $\mathbb F_2$, both boundary maps vanish.
:::

<1>2. Over the field $\mathbb F_2$, the Künneth theorem gives
$$
H_n(\mathbb{RP}^2\times\mathbb{RP}^2;\mathbb F_2)
\cong\bigoplus_{i+j=n}H_i(\mathbb{RP}^2;\mathbb F_2)\otimes H_j(\mathbb{RP}^2;\mathbb F_2).
$$
::: {.proof}
Over a field there are no Tor terms in the homological Künneth theorem.
:::

<1>3. Therefore
$$
\boxed{
H_n(\mathbb{RP}^2\times\mathbb{RP}^2;\mathbb Z_2)
\cong
\begin{cases}
\mathbb Z_2,&n=0,4,\\
(\mathbb Z_2)^2,&n=1,3,\\
(\mathbb Z_2)^3,&n=2,\\
0,&\text{otherwise}.
\end{cases}}
$$
::: {.proof}
Count pairs $(i,j)\in\{0,1,2\}^2$ with $i+j=n$. Their numbers are $1,2,3,2,1$ for $n=0,1,2,3,4$ respectively, and each tensor factor is one-dimensional over $\mathbb F_2$.
:::
:::

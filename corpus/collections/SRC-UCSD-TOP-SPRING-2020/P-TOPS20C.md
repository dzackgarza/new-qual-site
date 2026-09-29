---
schema: qual/card@1
id: P-TOPS20C
kind: problem
title: "Homology of X x X where X is S^2 with a 3-cell attached by degree 3"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Cell Complexes
  - Künneth Formula
relations: []
review: draft
---

::: {.problem}
Let $X$ be a $3$-dimensional CW complex obtained by attaching a single $3$-dimensional cell to $S^2$ via an attaching map of degree $3$.
Compute the homology group $H_k(X \times X; \mathbb{Z})$ for all $k \geq 0$.
:::

::: {.solution}

::: pf

::: {.pf-step #cellular-chain-complex-x}
The cellular chain complex of $X$ in positive degrees is
$$0\to\mathbb Z\xrightarrow{3}\mathbb Z\to0$$
concentrated in degrees $3$ and $2$.

::: pf-proof
The cellular boundary of the attached $3$-cell is multiplication by the degree of its attaching map, namely $3$.
:::

:::

::: pf-step
Thus
$$H_i(X;\mathbb Z)\cong\begin{cases}
\mathbb Z,&i=0,\\
\mathbb Z/3,&i=2,\\
0,&\text{otherwise.}
\end{cases}$$

::: pf-proof
Compute the homology of the complex in step [](#cellular-chain-complex-x){.pf-ref} together with the degree-$0$ cell.
:::

:::

::: pf-step
The integral Künneth theorem gives
$$\boxed{H_k(X\times X;\mathbb Z)\cong\begin{cases}
\mathbb Z,&k=0,\\
(\mathbb Z/3)^2,&k=2,\\
\mathbb Z/3,&k=4,5,\\
0,&\text{otherwise.}
\end{cases}}$$

::: pf-proof
The degree-$2$ groups come from $H_2\otimes H_0$ and $H_0\otimes H_2$. In degree $4$, $H_2\otimes H_2\cong\mathbb Z/3$. The only Tor contribution is $\operatorname{Tor}(\mathbb Z/3,\mathbb Z/3)\cong\mathbb Z/3$, appearing in degree $5$.
:::

:::

:::

:::

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

::: problem
Let $X$ be a $3$-dimensional CW complex obtained by attaching a single $3$-dimensional cell to $S^2$ via an attaching map of degree $3$.
Compute the homology group $H_k(X \times X; \mathbb{Z})$ for all $k \geq 0$.
:::

::: {.solution}
<1>1. The cellular chain complex of $X$ in positive degrees is
$$0\to\mathbb Z\xrightarrow{3}\mathbb Z\to0$$
concentrated in degrees $3$ and $2$.
::: {.proof}
The cellular boundary of the attached $3$-cell is multiplication by the degree of its attaching map, namely $3$.
:::

<1>2. Thus
$$H_i(X;\mathbb Z)\cong\begin{cases}
\mathbb Z,&i=0,\\
\mathbb Z/3,&i=2,\\
0,&\text{otherwise.}
\end{cases}$$
::: {.proof}
Compute the homology of the complex in <1>1 together with the degree-$0$ cell.
:::

<1>3. The integral Künneth theorem gives
$$\boxed{H_k(X\times X;\mathbb Z)\cong\begin{cases}
\mathbb Z,&k=0,\\
(\mathbb Z/3)^2,&k=2,\\
\mathbb Z/3,&k=4,5,\\
0,&\text{otherwise.}
\end{cases}}$$
::: {.proof}
The degree-$2$ groups come from $H_2\otimes H_0$ and $H_0\otimes H_2$. In degree $4$, $H_2\otimes H_2\cong\mathbb Z/3$. The only Tor contribution is $\operatorname{Tor}(\mathbb Z/3,\mathbb Z/3)\cong\mathbb Z/3$, appearing in degree $5$.
:::
:::

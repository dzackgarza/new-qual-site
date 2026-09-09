---
schema: qual/card@1
id: P-TOPS23E
kind: problem
title: "Homology of RP^3 as B^3 with antipodal boundary points identified"
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

::: problem
Let $X$ be the space obtained from a solid ball $B^3$ by identifying pairs of antipodal points on its boundary sphere $S^2$.
Decompose $X$ as a CW-complex and compute its homology $H_*(X; \mathbb{Z})$.
:::

::: {.solution}
<1>1. The quotient $X=B^3/(x\sim-x\text{ on }S^2)$ is the standard model of $\mathbb{RP}^3$.
::: {.proof}
Real projective $3$-space is obtained from a closed $3$-ball by identifying antipodal points on its boundary sphere.
:::

<1>2. It has a CW structure with one cell $e^k$ in each dimension $k=0,1,2,3$.
::: {.proof}
The standard filtration $\mathbb{RP}^0\subset\mathbb{RP}^1\subset\mathbb{RP}^2\subset\mathbb{RP}^3$ adds one cell in each dimension.
:::

<1>3. The cellular boundary maps are
$$0\to\mathbb Z\xrightarrow{0}\mathbb Z\xrightarrow{2}\mathbb Z\xrightarrow{0}\mathbb Z\to0.$$
::: {.proof}
For the standard CW structure on $\mathbb{RP}^n$, the cellular boundary in degree $k$ is multiplication by $1+(-1)^k$: it is $0$ for odd $k$ and $2$ for even $k$.
:::

<1>4. Therefore
$$\boxed{H_k(X;\mathbb Z)\cong\begin{cases}
\mathbb Z,&k=0,3,\\
\mathbb Z/2,&k=1,\\
0,&\text{otherwise.}
\end{cases}}$$
::: {.proof}
Compute kernels modulo images in the chain complex from <1>3.
:::
:::

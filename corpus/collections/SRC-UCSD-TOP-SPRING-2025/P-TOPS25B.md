---
schema: qual/card@1
id: P-TOPS25B
kind: problem
title: Singular homology of $\mathbb{RP}^9 / \mathbb{RP}^4$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Cell Complexes
relations: []
review: draft
---

::: {.problem}
Let $\mathbb{RP}^4$ be realised as a subspace of $\mathbb{RP}^9$ by setting the last 5 homogeneous coordinates equal to $0$.
Let $X$ be the quotient $\mathbb{RP}^9 / \mathbb{RP}^4$.
Compute its singular homology with integral coefficients.
:::

::: {.solution}
<1>1. The quotient $X=\mathbb{RP}^9/\mathbb{RP}^4$ inherits one cell in each dimension $5,6,7,8,9$, together with the quotient basepoint.
::: {.proof}
Use the standard CW filtration $\mathbb{RP}^0\subset\cdots\subset\mathbb{RP}^9$ and collapse its $4$-skeleton.
:::

<1>2. Its reduced cellular chain complex is
$$0\to\mathbb Z\xrightarrow{2}\mathbb Z\xrightarrow0\mathbb Z\xrightarrow2\mathbb Z\xrightarrow0\mathbb Z\to0,$$
with the terms in degrees $9,8,7,6,5$.
::: {.proof}
For real projective space the cellular boundary in degree $k$ is multiplication by $1+(-1)^k$: it is $0$ for odd $k$ and $2$ for even $k$.
:::

<1>3. Therefore
$$\boxed{H_i(X;\mathbb Z)\cong\begin{cases}\mathbb Z,&i=0,9,\\ \mathbb Z/2,&i=5,7,\\0,&\text{otherwise.}\end{cases}}$$
::: {.proof}
Read kernels modulo images from the complex in <1>2.
:::
:::

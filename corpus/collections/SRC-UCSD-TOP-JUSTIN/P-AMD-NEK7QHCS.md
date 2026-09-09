---
schema: qual/card@1
id: P-AMD-NEK7QHCS
kind: problem
title: Space with prescribed finitely generated homology groups
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
Let $\theset{A_i}^n \in \mathbf{Ab}$ be finitely generated, show $\exists X \mid H_i(X) \cong A_i$ for $i\leq n$ and 0 otherwise.
:::

::: {.solution}
<1>1. Write each finitely generated abelian group as
$$
A_i\cong \mathbb Z^{r_i}\oplus\bigoplus_{j=1}^{s_i}\mathbb Z/d_{ij},
\qquad d_{ij}\ge2.
$$
::: {.proof}
This is the structure theorem for finitely generated abelian groups.
:::

<1>2. For $i\ge1$, realize the free summand $\mathbb Z^{r_i}$ by a wedge of $r_i$ copies of $S^i$.
::: {.proof}
The reduced homology of $S^i$ is $\mathbb Z$ in degree $i$ and zero elsewhere.
:::

<1>3. Realize each torsion summand $\mathbb Z/d_{ij}$ in degree $i$ by the Moore space
$$
M(\mathbb Z/d_{ij},i)=S^i\cup_{d_{ij}}e^{i+1}.
$$
::: {.proof}
Its cellular chain complex in positive degrees has
$$
0\to\mathbb Z\xrightarrow{d_{ij}}\mathbb Z\to0
$$
concentrated in degrees $i+1$ and $i$, hence reduced homology $\mathbb Z/d_{ij}$ in degree $i$ and zero elsewhere.
:::

<1>4. Let $X$ be the wedge of all these spheres and Moore spaces over $1\le i\le n$.
::: {.proof}
There are finitely many summands because every $A_i$ is finitely generated and only finitely many $i$ occur.
:::

<1>5. Then for every $1\le i\le n$,
$$
\widetilde H_i(X;\mathbb Z)\cong A_i,
$$
and $\widetilde H_k(X;\mathbb Z)=0$ for $k>n$.
::: {.proof}
Reduced homology takes wedges of based CW complexes to direct sums. The only cells above dimension $n$ are the $(n+1)$-cells used in Moore spaces for torsion in $A_n$, and their boundaries are injective multiplication maps, so they create no homology in degree $n+1$.
:::

<1>6. If the requested $A_0$ is $\mathbb Z^c$ for some finite $c\ge1$, take the disjoint union of $c$ connected constructions, distributing the positive-degree summands among the components; then $H_0\cong\mathbb Z^c$.
::: {.proof}
For any space, $H_0$ is free abelian on its path components. Hence only free abelian groups can occur as $H_0$. In the usual connected formulation one necessarily has $A_0\cong\mathbb Z$.
:::
:::

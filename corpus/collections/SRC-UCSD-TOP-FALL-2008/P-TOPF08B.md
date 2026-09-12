---
schema: qual/card@1
id: P-TOPF08B
kind: problem
title: "Moore space M(p) as a manifold: which primes work?"
classification:
  areas:
  - topology
  topics:
  - Moore Spaces
  - Manifolds
  - Cell Complexes
relations: []
review: draft
---

::: problem
Let $p$ be a prime integer, let $M(p)$ denote the space obtained as the identification space of the $2$-disc $D^2$ under the identification: $x \sim y$ if $x, y \in \partial D^2 = S^1$ and $x = e^{2\pi i y/p}$, $n \in \mathbb{Z}$.
Find the values of $p$ for which $M(p)$ is homotopy equivalent to a compact boundaryless manifold.
:::

::: {.solution}
<1>1. The space $M(p)$ has a CW structure with one cell in dimensions $0,1,2$ and cellular boundary
$$
\partial_2:\mathbb Z\xrightarrow{\ p\ }\mathbb Z.
$$
::: {.proof}
The boundary circle of the $2$-disk is identified by the degree-$p$ map onto the resulting $1$-cell. This is the standard Moore space $M(\mathbb Z/p,1)$.
:::

<1>2. Thus
$$
H_i(M(p);\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=0,\\
\mathbb Z/p,&i=1,\\
0,&i\ge2.
\end{cases}
$$
::: {.proof}
This is the homology of the cellular complex $0\to\mathbb Z\xrightarrow p\mathbb Z\to\mathbb Z\to0$.
:::

<1>3. If $p$ is odd, then $M(p)$ has trivial reduced homology with $\mathbb F_2$ coefficients.
::: {.proof}
Modulo $2$, multiplication by the odd integer $p$ is an isomorphism, so the cellular chain complex is exact in positive degrees.
:::

<1>4. Hence for odd $p$, $M(p)$ cannot be homotopy equivalent to a compact connected boundaryless manifold of positive dimension.
::: {.proof}
Every closed connected $d$-manifold has $H_d(-;\mathbb F_2)\cong\mathbb F_2$ by mod-$2$ Poincaré duality, whereas <1>3 gives zero reduced mod-$2$ homology in every positive degree.
:::

<1>5. For $p=2$, $M(2)$ is homeomorphic to $\mathbb{RP}^2$.
::: {.proof}
The standard disk model of $\mathbb{RP}^2$ identifies antipodal points of the boundary circle, equivalently attaches a $2$-cell to $S^1$ by the degree-$2$ map. This is precisely $M(2)$.
:::

<1>6. Therefore
$$
\boxed{p=2\text{ is the unique prime for which }M(p)\text{ has the homotopy type of a closed manifold}.}
$$
::: {.proof}
Combine <1>4 and <1>5.
:::
:::

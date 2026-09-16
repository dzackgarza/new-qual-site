---
schema: qual/card@1
id: P-TOPS24A
kind: problem
title: Homology of four mutually tangent unit 2-spheres
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
---

::: {.problem}
Let $X$ be the union of four mutually tangent unit 2-spheres inside $\mathbb{R}^3$.
Compute $H_*(X; \mathbb{Z})$.
:::

::: {.solution}
<1>1. The four spheres are pairwise tangent at six distinct points, with no triple intersection. Regard each sphere as a vertex space and each tangency point as an edge joining the two corresponding vertex spaces.
::: {.proof}
There are $\binom42=6$ pairwise tangencies. The incidence graph is therefore the complete graph $K_4$.
:::

<1>2. The union $X$ is homotopy equivalent to
$$\left(\bigvee_{i=1}^4 S^2\right)\vee\left(\bigvee_{j=1}^3 S^1\right).$$
::: {.proof}
Choose within each sphere a contractible tree joining its three tangency points and collapse each such tree to the corresponding vertex. This preserves the sphere's $S^2$ homotopy class while leaving the incidence graph $K_4$. A connected graph with $4$ vertices and $6$ edges has rank $6-4+1=3$, hence is homotopy equivalent to a wedge of three circles.
:::

<1>3. Consequently
$$\boxed{H_k(X;\mathbb Z)\cong\begin{cases}
\mathbb Z,&k=0,\\
\mathbb Z^3,&k=1,\\
\mathbb Z^4,&k=2,\\
0,&k\ge3.
\end{cases}}$$
::: {.proof}
Use the wedge decomposition from <1>2.
:::
:::

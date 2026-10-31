---
schema: qual/card@1
id: E-HAT-2.1-24
kind: problem
title: $n$-simplices in barycentric subdivision defined by inequalities on barycentric coordinates
classification:
  areas:
  - topology
  topics:
  - Homology
  - Simplicial Complexes
  - Barycentric Subdivision
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
Show that each $n$ simplex in the barycentric subdivision of $\Delta^n$ is defined by $n$ inequalities $t_{i_0} \leq t_{i_1} \leq \dots \leq t_{i_n}$ in its barycentric coordinates, where $(i_0, \cdots, i_n)$ is a permutation of $(0, \cdots, n)$.
:::

::: {.solution}
A maximal chain of nonempty faces of $\Delta^n$ has the form
$$
S_k=\{i_0,\ldots,i_k\}\qquad(0\le k\le n)
$$
for a permutation $(i_0,\ldots,i_n)$ of $(0,\ldots,n)$. Let $b_k$ be the barycenter of the face $S_k$.

::: pf

::: {.pf-step #s1}

Every point of the subdivided simplex $[b_0,\ldots,b_n]$ satisfies
$$
t_{i_0}\ge t_{i_1}\ge\cdots\ge t_{i_n}.
$$

::: pf-proof

The barycenter $b_k$ has coordinate $1/(k+1)$ at each $i_j$ with $j\le k$ and coordinate $0$ at all other vertices. Hence its coordinates have the stated order. The inequalities are preserved under convex combinations.

:::

:::

::: {.pf-step #s2}

Every point of $\Delta^n$ whose coordinates satisfy this order lies in $[b_0,\ldots,b_n]$.

::: pf-proof

Put $t_{i_{n+1}}=0$ and define
$$
\lambda_k=(k+1)(t_{i_k}-t_{i_{k+1}})\qquad(0\le k\le n).
$$
The ordering gives $\lambda_k\ge0$, and telescoping gives
$$
\sum_{k=0}^n\lambda_k
=\sum_{k=0}^n t_{i_k}=1.
$$
The coordinate at $i_j$ of $\sum_k\lambda_k b_k$ is
$$
\sum_{k=j}^n\frac{\lambda_k}{k+1}
=\sum_{k=j}^n(t_{i_k}-t_{i_{k+1}})
=t_{i_j}.
$$
Thus the point is the displayed convex combination of the barycenters.

:::

:::

::: pf-step

The $n$-simplices of the barycentric subdivision are exactly the regions defined by one ordering of the barycentric coordinates.

::: pf-proof

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} show that the simplex for the chain $S_0\subsetneq\cdots\subsetneq S_n$ equals the region $t_{i_0}\ge\cdots\ge t_{i_n}$. Reversing the permutation writes the same region as
$$
t_{i_n}\le\cdots\le t_{i_0},
$$
which has the form stated in the exercise.

:::

:::

:::
:::

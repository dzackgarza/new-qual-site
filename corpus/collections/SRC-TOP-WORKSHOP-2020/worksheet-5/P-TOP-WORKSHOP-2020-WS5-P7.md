---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS5-P7
kind: problem
title: Simplicial homology of the $\Delta$-complex obtained from $\Delta^3$ by identifying all $k$-faces
classification:
  areas:
  - topology
  topics:
  - Homology
  - Cell Complexes
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
(May 2013) Let $Y$ be the standard $3$-simplex $\Delta^3$ with a total ordering on its four vertices.
Let $X$ be the $\Delta$-complex obtained from $Y$ by identifying, for each $k\leq 3$, all of its $k$-dimensional faces such that the identifications respect the vertex ordering.
Thus $X$ has a single $k$-simplex for each $k\leq 3$.
Compute the simplicial homology groups of the $\Delta$-complex $X$.
:::

::: {.solution}
Let $e_k$ be the unique $k$-simplex of $X$ for $0\le k\le 3$, so $\Delta_k(X)=\mathbb Z e_k$ for $0\le k\le3$ and $\Delta_k(X)=0$ for $k\ge4$. Every face of $e_k$ of dimension $k-1$ is $e_{k-1}$.

::: pf

::: {.pf-step #s1}

$\partial_1=0$, $\partial_2(e_2)=e_1$, and $\partial_3=0$.

::: pf-proof

$\partial_1 e_1=[v_1]-[v_0]=e_0-e_0=0$. $\partial_2 e_2=[v_1,v_2]-[v_0,v_2]+[v_0,v_1]=e_1-e_1+e_1=e_1$. $\partial_3 e_3=[v_1,v_2,v_3]-[v_0,v_2,v_3]+[v_0,v_1,v_3]-[v_0,v_1,v_2]=e_2-e_2+e_2-e_2=0$.

:::

:::

::: pf-qed

By step [](#s1){.pf-ref}, $\partial_2\colon\mathbb Z\to\mathbb Z$ is an isomorphism and $\partial_1=\partial_3=0$. Hence
$H_0=\mathbb Z e_0/0\cong\mathbb Z$, $H_1=\mathbb Z e_1/\mathbb Z e_1=0$, $H_2=\ker\partial_2/\operatorname{im}\partial_3=0$, $H_3=\ker\partial_3=\mathbb Z e_3\cong\mathbb Z$, and $H_k=0$ for $k\ge4$:
$$
\boxed{H_k(X)\cong\begin{cases}\mathbb{Z}, & k = 0, 3,\\ 0, & \text{otherwise}.\end{cases}}
$$

:::

:::

:::

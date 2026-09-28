---
schema: qual/card@1
id: P-OX3MY
kind: problem
title: A non-invertible endomorphism $T$ admitting $S$ with $TS=0$ but $ST\neq 0$
classification:
  areas:
  - algebra
  topics:
  - Rank and Nullity
  - Linear Algebra
  - Matrices
relations: []
review: draft
---

::: {.problem}
Let $V$ be a finite-dimensional $k\dash$vector space and $T:V\to V$ a non-invertible $k\dash$linear map.
Show that there exists a $k\dash$linear map $S:V\to V$ with $T\circ S = 0$ but $S\circ T\neq 0$.
:::

::: {.solution}
Assume $T\neq 0$. Since $T$ is not invertible and $V$ is finite-dimensional, $\ker T\neq 0$ by rank-nullity, so there is a nonzero $\vector v \in \ker T$. Since $T\neq 0$, there is a nonzero $\vector w \in \im(T)$; fix $\vector x_0$ with $T\vector x_0 = \vector w$.
Choose a linear functional $\varphi\colon V\to k$ with $\varphi(\vector w)=1$ (extend $\vector w$ to a basis of $V$), and define
$$
S\colon V\to V,
\qquad
S\vector x = \varphi(\vector x)\,\vector v.
$$

For every vector $\vector x$,
$$
TS\vector x = \varphi(\vector x)\,T\vector v = \vector 0,
$$
so $T\circ S = 0$. At $\vector x_0$,
$$
ST\vector x_0 = S\vector w = \varphi(\vector w)\,\vector v = \vector v \neq \vector 0,
$$
so $S\circ T\neq 0$.

$\qed$
:::

::: {.remark}
The statement needs $T\neq 0$: for $T=0$, $S\circ T=0$ for every $S$.
:::

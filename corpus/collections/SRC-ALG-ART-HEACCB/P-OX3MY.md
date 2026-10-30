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
Let $V$ be a finite-dimensional $k\dash$vector space and $T:V\to V$ a nonzero, non-invertible $k\dash$linear map.
Show that there exists a $k\dash$linear map $S:V\to V$ with $T\circ S = 0$ but $S\circ T\neq 0$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}
There are a nonzero $\vector v\in\ker T$ and a vector $\vector x_0$ with
$\vector w=T\vector x_0\neq\vector 0$.

::: pf-proof
Since $T$ is not invertible and $V$ is finite-dimensional, rank-nullity gives
$\ker T\neq 0$. Since $T\neq 0$, some $\vector x_0$ has $T\vector x_0\neq\vector 0$.
:::

:::

::: {.pf-step #s2}
Choose a linear functional $\varphi\colon V\to k$ with $\varphi(\vector w)=1$, and define
$$
S\colon V\to V,
\qquad
S\vector x = \varphi(\vector x)\,\vector v.
$$
Then $T\circ S=0$.

::: pf-proof
The functional exists because $\vector w\neq\vector 0$ extends to a basis of $V$.
For every vector $\vector x$,
$$
TS\vector x = \varphi(\vector x)\,T\vector v = \vector 0,
$$
because $\vector v\in\ker T$ by step [](#s1){.pf-ref}.
:::

:::

::: {.pf-step #s3}
$S\circ T\neq 0$.

::: pf-proof
At $\vector x_0$,
$$
ST\vector x_0 = S\vector w = \varphi(\vector w)\,\vector v = \vector v \neq \vector 0.
$$
:::

:::

::: pf-qed
Steps [](#s2){.pf-ref} and [](#s3){.pf-ref} give the required map $S$.
:::

:::

:::

---
schema: qual/card@1
id: E-2V2VL
kind: problem
title: Compact subspaces of metric spaces are closed and bounded
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Show that every compact subspace of a metric space is bounded in that metric and is closed.
Find a metric space in which not every closed bounded subspace is compact.
:::

::: {.solution}
**Goal:** Prove that compact subspaces of metric spaces are closed and bounded, and provide a metric space containing a closed, bounded subspace that fails to be compact.

::: pf

::: pf-step
Compact subspaces are closed:
Let $K$ be a compact subspace of a metric space $(X, d)$. Then $K$ is closed in $X$.

::: pf-proof

::: pf-step
Every metric space is Hausdorff ($T_2$).
:::

::: pf-step
Let $x \in X \setminus K$. For each $y \in K$, let $r_y = d(x, y) > 0$.
:::

::: pf-step
Define $U_y = B(y, \frac{r_y}{2})$ and $V_y = B(x, \frac{r_y}{2})$. Then $U_y \cap V_y = \emptyset$.
:::

::: pf-step
The family $\{U_y\}_{y \in K}$ is an open cover of $K$. Since $K$ is compact, there exists a finite subcover $\{U_{y_1}, \dots, U_{y_k}\}$.
:::

::: pf-step
The set $V = \bigcap_{i=1}^k V_{y_i}$ is an open neighborhood of $x$.
:::

::: pf-step
Since $V \cap U_{y_i} = \emptyset$ for each $i$, $V \cap K \subseteq V \cap (\bigcup_{i=1}^k U_{y_i}) = \emptyset$.
:::

::: pf-step
Thus $X \setminus K$ is open, so $K$ is closed in $X$.
:::

:::

:::

::: pf-step
Compact subspaces are bounded:
Let $K$ be a compact subspace of $(X, d)$. Then $\operatorname{diam}(K) < \infty$.

::: pf-proof

::: pf-step
If $K = \emptyset$, $\operatorname{diam}(K) = 0 < \infty$.
:::

::: pf-step
If $K \neq \emptyset$, fix an arbitrary basepoint $x_0 \in K$.
:::

::: pf-step
For every $x \in K$, $d(x_0, x) < n$ for some integer $n \in \mathbb{Z}_+$, so $K \subseteq \bigcup_{n=1}^\infty B(x_0, n)$.
:::

::: pf-step
Since $\{B(x_0, n)\}_{n=1}^\infty$ is an open cover of the compact space $K$, there exists a finite subcover $\{B(x_0, n_1), \dots, B(x_0, n_k)\}$.
:::

::: pf-step
Setting $N = \max\{n_1, \dots, n_k\}$, we have $K \subseteq B(x_0, N)$.
:::

::: pf-step
By the triangle inequality, for all $x, y \in K$:
$$d(x, y) \le d(x, x_0) + d(x_0, y) < N + N = 2N.$$
:::

::: pf-step
Thus $\operatorname{diam}(K) \le 2N < \infty$, so $K$ is bounded.
:::

:::

:::

::: pf-step
Counterexample (closed + bounded $\not\implies$ compact):

::: pf-proof

::: pf-step
Consider an infinite set $X$ (e.g. $X = \mathbb{Z}_+$) equipped with the discrete metric $d(x, y) = 1$ for all $x \neq y$ and $d(x, x) = 0$.
:::

::: pf-step
The entire space $X$ is closed in itself and is bounded since $\operatorname{diam}(X) = 1 \le 1$.
:::

::: pf-step
The open cover $\mathcal{U} = \{B(x, 1/2)\}_{x \in X} = \{\{x\}\}_{x \in X}$ consists of singleton open sets.
:::

::: pf-step
Since $X$ is infinite, no finite subcollection of $\mathcal{U}$ can cover $X$.
:::

::: pf-step
Thus the closed bounded metric space $(X, d)$ is not compact. Q.E.D.
:::

:::

:::

:::

:::

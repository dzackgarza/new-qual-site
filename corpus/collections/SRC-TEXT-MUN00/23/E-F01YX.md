---
schema: qual/card@1
id: E-F01YX
kind: problem
title: Arbitrary products of connected spaces are connected
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Let $\ts{X_\alpha}_{\alpha \in J}$ be an indexed family of connected spaces; let $X$ be the product space

$$
X = \prod_{\alpha \in J} X_\alpha.
$$

Let $\mathbf{a} = (a_\alpha)$ be a fixed point of $X$.

(a) Given any finite subset $K$ of $J$, let $X_K$ denote the subspace of $X$ consisting of all points $\mathbf{x} = (x_\alpha)$ such that $x_\alpha = a_\alpha$ for $\alpha \notin K$.
Show that $X_K$ is connected.

(b) Show that the union $Y$ of the spaces $X_K$ is connected.

(c) Show that $X$ equals the closure of $Y$; conclude that $X$ is connected.
:::

::: {.solution}
(a) For finite $K\subseteq J$, the space $X_K$ is naturally homeomorphic to
\[
\prod_{\alpha\in K}X_\alpha
\]
by forgetting the fixed coordinates. A finite product of connected spaces is connected, so $X_K$ is connected.

(b) Every $X_K$ contains the fixed point $\mathbf a$. Hence the union
\[
Y=\bigcup_{K\subseteq J,\ K\text{ finite}}X_K
\]
is a union of connected sets with a common point, and is therefore connected.

(c) Let $U$ be a nonempty basic open set of the product $X$. It restricts only finitely many coordinates, say those in $K$. Choose $x\in U$ and define $y$ by
\[
y_\alpha=x_\alpha\quad(\alpha\in K),\qquad
 y_\alpha=a_\alpha\quad(\alpha\notin K).
\]
Then $y\in U\cap X_K\subseteq U\cap Y$. Thus every nonempty basic open set meets $Y$, so $\overline Y=X$. The closure of a connected set is connected, hence $X$ is connected.
:::

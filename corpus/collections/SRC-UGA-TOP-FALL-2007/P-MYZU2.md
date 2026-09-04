---
schema: qual/card@1
id: P-MYZU2
kind: problem
title: Union of connected subspaces sharing a point is connected
classification:
  areas:
  - topology
  topics:
  - Connectedness
relations: []
review: draft
---

::: {.problem}
Let $\theset{X_\alpha \mid \alpha \in A}$ be a family of connected subspaces of a space $X$ such that there is a point $p \in X$ which is in each of the $X_\alpha$.

Show that the union of the $X_\alpha$ is connected.
:::

::: {.solution}
Let
\[
Y=\bigcup_{\alpha\in A}X_\alpha.
\]
Suppose, toward a contradiction, that $Y$ is disconnected.
Then there are disjoint nonempty sets $U,V$, open in $Y$, such that
\[
Y=U\disjoint V.
\]
Since the common point $p$ belongs to $Y$, after interchanging $U$ and $V$ if necessary we may assume $p\in U$.

Choose $q\in V$.
Since $q\in Y$, there is some $\alpha$ with $q\in X_\alpha$.
Then
\[
p\in U\cap X_\alpha,
\qquad
q\in V\cap X_\alpha.
\]
The sets $U\cap X_\alpha$ and $V\cap X_\alpha$ are disjoint, nonempty, open in the subspace $X_\alpha$, and their union is $X_\alpha$.
This is a separation of $X_\alpha$, contradicting its connectedness.

Therefore $Y$ is connected.
:::

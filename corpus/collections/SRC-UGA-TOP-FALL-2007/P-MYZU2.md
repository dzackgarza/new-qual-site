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

<1>1. Any separation of $Y$ would separate one of the subspaces $X_\alpha$.
::: {.proof}
Suppose
\[
Y=U\disjoint V.
\]
is a separation. Since the common point $p$ belongs to $Y$, after interchanging $U$ and $V$ if necessary assume $p\in U$.

Choose $q\in V$.
Since $q\in Y$, there is some $\alpha$ with $q\in X_\alpha$.
Then
\[
p\in U\cap X_\alpha,
\qquad
q\in V\cap X_\alpha.
\]
The sets $U\cap X_\alpha$ and $V\cap X_\alpha$ are disjoint, nonempty, open in the subspace $X_\alpha$, and their union is $X_\alpha$.
Thus they form a separation of $X_\alpha$.
:::

<1>2. $Y$ is connected.
::: {.proof}
If $Y$ were disconnected, a separation would exist. By <1>1 it would separate some $X_\alpha$, contradicting the hypothesis that every $X_\alpha$ is connected.
:::
:::

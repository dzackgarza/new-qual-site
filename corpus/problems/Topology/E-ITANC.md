---
schema: qual/card@1
id: E-ITANC
kind: problem
title: A compact subset of a Hausdorff space is closed
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Hausdorff Spaces
relations: []
review: draft
---

::: {.exercise}
Show that a compact set in a Hausdorff space is closed.
:::

::: {.solution}
<1>1. Let $K$ be compact in a Hausdorff space $X$, and fix $x\notin K$.
::: {.proof}
We construct an open neighborhood of $x$ disjoint from $K$.
:::

<1>2. For every $y\in K$, choose disjoint open sets $U_y\ni x$ and $V_y\ni y$.
::: {.proof}
This is the Hausdorff property.
:::

<1>3. Compactness gives $y_1,\dots,y_r$ with $K\subseteq V_{y_1}\cup\cdots\cup V_{y_r}$. Then $U=U_{y_1}\cap\cdots\cap U_{y_r}$ is an open neighborhood of $x$ disjoint from $K$.
::: {.proof}
If a point of $U$ lay in $K$, it would lie in some $V_{y_i}$, contradicting $U\subseteq U_{y_i}$ and $U_{y_i}\cap V_{y_i}=\varnothing$.
:::

<1>4. Thus $X\setminus K$ is open and $K$ is closed.
::: {.proof}
Every point of the complement has the neighborhood constructed in <1>3.
:::
:::

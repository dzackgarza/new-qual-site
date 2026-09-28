---
schema: qual/card@1
id: P-TOP-WORKSHOP-D1-W1
kind: problem
title: A compact subset of a $T_2$ space is closed
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Hausdorff Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
If $X$ is $T_2$ and $A\subseteq X$ is compact, then $A$ is closed.
:::

::: {.solution}
<1>1. Every $x \in X \setminus A$ has an open neighborhood disjoint from $A$.
::: {.proof}
For each $a \in A$, since $X$ is Hausdorff and $x \neq a$, choose disjoint open sets $U_a \ni x$ and $V_a \ni a$. The sets $V_a$ cover $A$, so by compactness $A \subseteq V_{a_1} \cup \cdots \cup V_{a_k}$ for some $a_1, \ldots, a_k \in A$. Put $U = U_{a_1} \cap \cdots \cap U_{a_k}$, an open set containing $x$. Since $U \subseteq U_{a_i}$ and $U_{a_i} \cap V_{a_i} = \varnothing$ for each $i$, $U$ is disjoint from $V_{a_1} \cup \cdots \cup V_{a_k} \supseteq A$.
:::

<1>2. Q.E.D.
::: {.proof}
By step <1>1, $X \setminus A$ is a union of open sets, hence open, so $A$ is closed.
:::
:::

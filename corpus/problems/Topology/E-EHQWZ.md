---
schema: qual/card@1
id: E-EHQWZ
kind: problem
title: $X$ is connected if and only if its only clopen subsets are $\emptyset$ and
  $X$
classification:
  areas:
  - topology
  topics:
  - Connectedness
relations: []
review: draft
---

::: {.exercise}
Prove that $X$ is connected iff the only clopen subsets are $\emptyset, X$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If $X$ is disconnected, then $X$ has a clopen subset other than $\varnothing$ and $X$.

::: pf-proof

Write $X=U\sqcup V$ with $U,V$ nonempty, disjoint, and open. Then $U$ is open, and closed because its complement $V$ is open; it is neither empty nor all of $X$ because $V\neq\varnothing$.

:::

:::

::: {.pf-step #s2}

If $A\subseteq X$ is clopen with $A\neq\varnothing,X$, then $X$ is disconnected.

::: pf-proof

The sets $A$ and $X\setminus A$ are nonempty, disjoint, and open because $A$ is both open and closed, so $X=A\sqcup(X\setminus A)$ is a separation.

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} shows that if $X$ is connected, then its only clopen subsets are $\varnothing$ and $X$; step [](#s1){.pf-ref} is the contrapositive of the converse.

:::

:::

:::

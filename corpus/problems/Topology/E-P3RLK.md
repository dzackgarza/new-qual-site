---
schema: qual/card@1
id: E-P3RLK
kind: problem
title: Closed subsets of compact spaces are compact
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
---

::: {.problem}
Let $A\subset X$ with $A$ closed and $X$ compact, and show that $A$ is compact.
:::

::: {.solution}

Let $\mathcal U$ be an open cover of $A$ by subsets open in the subspace topology.
For each $U\in\mathcal U$, choose an open set $V_U\subseteq X$ with $U=A\cap V_U$.

::: pf

::: {.pf-step #cover}

$\{V_U:U\in\mathcal U\}\cup\{X\setminus A\}$ is an open cover of $X$.

::: pf-proof

Since $A$ is closed, $X\setminus A$ is open. A point of $A$ lies in some $U\subseteq V_U$, and every other point lies in $X\setminus A$.

:::

:::

::: pf-step

$A$ is compact.

::: pf-proof

Compactness of $X$ gives a finite subcover $V_{U_1},\ldots,V_{U_n},X\setminus A$ of the cover in step [](#cover){.pf-ref}. Intersecting with $A$ removes the last set and gives
$$A=(A\cap V_{U_1})\cup\cdots\cup(A\cap V_{U_n})=U_1\cup\cdots\cup U_n,$$
a finite subcover of $\mathcal U$.

:::

:::

:::

:::

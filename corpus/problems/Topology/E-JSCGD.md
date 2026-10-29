---
schema: qual/card@1
id: E-JSCGD
kind: problem
title: Closed subsets of compact spaces are compact
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Let $X$ be a compact topological space and let $A \subseteq X$ be a closed subset of $X$.
Prove that $A$ is compact in the subspace topology.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Let $\{V_i\}_{i\in I}$ be an open cover of $A$ in the subspace topology, and choose open sets $U_i\subseteq X$ with $V_i=U_i\cap A$.

::: pf-proof

This is the definition of the subspace topology.

:::

:::

::: {.pf-step #s2}

$\{U_i:i\in I\}\cup\{X\setminus A\}$ is an open cover of $X$.

::: pf-proof

Since $A$ is closed, $X\setminus A$ is open. Points of $A$ lie in some $V_i\subseteq U_i$, and the remaining points lie in $X\setminus A$.

:::

:::

::: pf-step

$A$ is compact.

::: pf-proof

Compactness of $X$ applied to the cover of step [](#s2){.pf-ref} gives indices $i_1,\ldots,i_m$ with
$$X\subseteq U_{i_1}\cup\cdots\cup U_{i_m}\cup(X\setminus A).$$
Intersecting with $A$ yields $A\subseteq V_{i_1}\cup\cdots\cup V_{i_m}$, a finite subcover of the cover in step [](#s1){.pf-ref}.

:::

:::

:::

:::

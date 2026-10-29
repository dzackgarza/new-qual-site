---
schema: qual/card@1
id: E-HXOHR
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
Let $X$ be a compact space and let $A$ be a closed subspace.
Show that $A$ is compact.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Let $\theset{U_\alpha}$ be an open cover of $A$ in the subspace topology, and choose open sets $V_\alpha \subseteq X$ with $U_\alpha = V_\alpha \intersect A$.

::: pf-proof

This is the definition of the subspace topology.

:::

:::

::: {.pf-step #s2}

$\theset{V_\alpha} \union \theset{X\setminus A}$ is an open cover of $X$.

::: pf-proof

Since $A$ is closed, $X\setminus A$ is open. A point of $A$ lies in some $U_\alpha \subseteq V_\alpha$, and a point outside $A$ lies in $X\setminus A$.

:::

:::

::: pf-step

$A$ is compact.

::: pf-proof

By compactness of $X$, the cover of step [](#s2){.pf-ref} has a finite subcover $V_{\alpha_1}, \ldots, V_{\alpha_N}, X\setminus A$. Intersecting with $A$ removes $X\setminus A$ and gives $A = U_{\alpha_1} \union \cdots \union U_{\alpha_N}$, a finite subcover of the cover in step [](#s1){.pf-ref}.

:::

:::

:::

:::

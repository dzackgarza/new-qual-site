---
schema: qual/card@1
id: P-TOPS18C
kind: problem
title: "H_1 of a mapping telescope built from degree-k gluing maps"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Direct Limits
  - Mapping Telescope
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Let $X_n$ be the space formed from the disjoint union of $n$ copies $C_1, \ldots, C_n$ of the cylinder $S^1 \times I$ by gluing, for each $k$, the $S^1 \times \{1\}$ of $C_k$ to the $S^1 \times \{0\}$ of $C_{k+1}$ using a map of degree $k$.
There is a natural sequence of inclusions $X_1 \subseteq X_2 \subseteq X_3 \subseteq \cdots$ and so we may define $X$ to be the direct limit of this family.
(This is called a mapping telescope.)
What is $H_1(X; \mathbb{Z})$?
:::

::: {.solution}

::: pf

::: pf-step
$H_1(X_n) = \ZZ$ for each $n$.

::: pf-proof
The union of $C_k$ with the bottom circle of $C_{k+1}$ is the mapping cylinder of the degree-$k$ attaching map $S^1\to S^1$. A mapping cylinder deformation retracts onto its target, regardless of whether the attaching map is a homotopy equivalence. Iterating these retractions collapses the finite telescope $X_n$ onto the terminal circle in $C_n$. Hence $X_n\simeq S^1$ and $H_1(X_n)\cong\ZZ$.
:::

:::

::: pf-step
The inclusion $X_n \hookrightarrow X_{n+1}$ induces on $H_1$ the map $\ZZ \to \ZZ$ given by multiplication by $n$.

::: pf-proof
the inclusion of $X_n$ into $X_{n+1}$ sends the generator of $H_1(X_n)$ (the core circle of $C_n$) to the core circle of $C_{n+1}$ via the gluing map of degree $n$, so the induced map is multiplication by $n$.
:::

:::

::: {.pf-step #h1-is-direct-limit}
$H_1(X) = \varinjlim H_1(X_n)$.

::: pf-proof
homology commutes with direct limits (filtered colimits) of spaces.
:::

:::

::: {.pf-step #direct-limit-is-q}
The direct limit of the system $\ZZ \xrightarrow{1} \ZZ \xrightarrow{2} \ZZ \xrightarrow{3} \ZZ \xrightarrow{4} \cdots$ is $\QQ$.

::: pf-proof
the direct limit of $\ZZ \xrightarrow{\cdot n} \ZZ$ over all $n$ is the localization of $\ZZ$ at all nonzero integers, i.e. $\QQ$ (every element is a fraction $a/b$ with $b$ a product of the gluing degrees).
:::

:::

::: {.pf-step #h1-equals-q}
Hence $H_1(X;\ZZ) = \QQ$.

::: pf-proof
Step [](#h1-is-direct-limit){.pf-ref} and step [](#direct-limit-is-q){.pf-ref}.
:::

:::

::: pf-qed
Step [](#h1-equals-q){.pf-ref}.
:::

:::

:::

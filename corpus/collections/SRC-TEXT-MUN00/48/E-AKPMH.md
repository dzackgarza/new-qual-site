---
schema: qual/card@1
id: E-AKPMH
kind: problem
title: The irrationals are a Baire space
classification:
  areas:
  - topology
  topics:
  - Baire Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Show that the irrationals are a Baire space.
:::

::: {.solution}
Let $\mathbb{P} = \mathbb{R} \setminus \mathbb{Q}$ with the subspace topology.

::: pf

::: pf-step
Representation of $\mathbb{P}$ as a $G_\delta$ subset of $\mathbb{R}$:

::: pf-proof

::: pf-step
Enumerate the countable set of rational numbers as $\mathbb{Q} = \{q_n\}_{n=1}^\infty$.
:::

::: pf-step
For each $n \ge 1$, the singleton $\{q_n\}$ is closed in $\mathbb{R}$, so $U_n = \mathbb{R} \setminus \{q_n\}$ is an open and dense subset of $\mathbb{R}$.
:::

::: pf-step
The subspace of irrational numbers is:
$$\mathbb{P} = \mathbb{R} \setminus \mathbb{Q} = \bigcap_{n=1}^\infty U_n.$$
:::

:::

:::

::: {.pf-step #s2}
Verification of the dense open intersection condition:

::: pf-proof

::: pf-step
Let $\{V_k\}_{k=1}^\infty$ be a countable sequence of dense open subsets of the subspace $\mathbb{P}$.
:::

::: pf-step
Since each $V_k$ is open in $\mathbb{P}$, there exists an open set $W_k \subseteq \mathbb{R}$ such that $V_k = W_k \cap \mathbb{P}$.
:::

::: pf-step
Because $V_k$ is dense in $\mathbb{P}$ and $\mathbb{P}$ is dense in $\mathbb{R}$, the open set $W_k$ is dense in $\mathbb{R}$ for each $k \ge 1$.
:::

::: pf-step
The combined collection $\{W_k\}_{k=1}^\infty \cup \{U_n\}_{n=1}^\infty$ is a countable family of open and dense subsets of $\mathbb{R}$.
:::

::: pf-step
By the Baire category theorem, the complete metric space $\mathbb{R}$ is a Baire space, so the countable intersection:
$$\bigcap_{k=1}^\infty W_k \cap \bigcap_{n=1}^\infty U_n = \left(\bigcap_{k=1}^\infty W_k\right) \cap \mathbb{P} = \bigcap_{k=1}^\infty V_k$$
is dense in $\mathbb{R}$.
:::

::: pf-step
Since this intersection lies in $\mathbb{P}$ and is dense in $\mathbb{R}$, it is dense in the subspace $\mathbb{P}$.
:::

:::

:::

::: pf-qed
By step [](#s2){.pf-ref}, every countable intersection of dense open subsets of $\mathbb{P}$ is dense in $\mathbb{P}$.
:::

:::

:::

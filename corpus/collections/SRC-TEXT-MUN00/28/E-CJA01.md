---
schema: qual/card@1
id: E-CJA01
kind: problem
title: The unit interval is not limit point compact in the lower limit topology
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.exercise}

Show that $[0, 1]$ is not limit point compact as a subspace of $\mathbb{R}_\ell$.
:::

::: {.solution}
**Goal:** Prove that the closed unit interval $[0, 1]$ endowed with the subspace topology from the lower limit line $\mathbb{R}_\ell$ is not limit point compact.

::: pf

::: pf-step
Definition of limit point compactness:

::: pf-proof

::: pf-step
A topological space $X$ is limit point compact (also called countably compact for $T_1$ spaces) if every infinite subset of $X$ has at least one limit point in $X$.
:::

::: pf-step
A point $x \in X$ is a limit point of $A \subseteq X$ if every open neighborhood $U$ of $x$ contains a point of $A$ distinct from $x$ (i.e. $(U \setminus \{x\}) \cap A \neq \emptyset$).
:::

:::

:::

::: pf-step
Construction of an infinite subset $A \subset [0, 1]$:

::: pf-proof

::: pf-step
Define
$$A = \left\{ 1 - \frac{1}{n} : n \in \mathbb{N}, \; n \ge 2 \right\} = \left\{ \frac{1}{2}, \frac{2}{3}, \frac{3}{4}, \frac{4}{5}, \dots \right\} \subset [0, 1].$$
:::

::: pf-step
Since the sequence $x_n = 1 - 1/n$ is strictly increasing, $A$ is an infinite subset of $[0, 1]$.
:::

:::

:::

::: pf-step
Verification that $A$ has no limit points in $[0, 1]_{\mathbb{R}_\ell}$:

::: pf-proof
We show that for every $x \in [0, 1]$, there exists an open neighborhood $U_x$ of $x$ in $[0, 1]_{\mathbb{R}_\ell}$ such that $(U_x \setminus \{x\}) \cap A = \emptyset$.

::: pf-step
Case $x \in [0, 1/2)$: The set $U_x = [x, 1/2) \cap [0, 1]$ is open in $[0, 1]_{\mathbb{R}_\ell}$, contains $x$, and satisfies $U_x \cap A = \emptyset$ because every element of $A$ is $\ge 1/2$.
:::

::: pf-step
Case $x = 1 - 1/n \in A$ for some $n \ge 2$: The set $U_x = [1 - 1/n, 1 - 1/(n+1)) \cap [0, 1]$ is open in the lower limit subspace topology, contains $x$, and contains no other element of $A$, so $(U_x \setminus \{x\}) \cap A = \emptyset$.
:::

::: pf-step
Case $x \in (1 - 1/n, 1 - 1/(n+1))$ for some $n \ge 2$: The set $U_x = [x, 1 - 1/(n+1)) \cap [0, 1]$ is open, contains $x$, and satisfies $U_x \cap A = \emptyset$.
:::

::: pf-step
Case $x = 1$: The set $U_1 = [1, 2) \cap [0, 1] = \{1\}$ is open in $[0, 1]_{\mathbb{R}_\ell}$ and contains no point of $A$, so $(U_1 \setminus \{1\}) \cap A = \emptyset$.
:::

:::

:::

::: pf-step
Conclusion:

::: pf-proof
The infinite subset $A \subset [0, 1]$ has no limit point in $[0, 1]_{\mathbb{R}_\ell}$. Therefore $[0, 1]$ is not limit point compact in $\mathbb{R}_\ell$.
:::

:::

:::

:::

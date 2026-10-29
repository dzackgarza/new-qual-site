---
schema: qual/card@1
id: E-MUN-6-5
kind: problem
title: Finiteness of Cartesian products
classification:
  areas:
  - topology
  topics:
  - Finite Sets
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.exercise}
If $A \times B$ is finite, does it follow that $A$ and $B$ are finite?
:::

::: {.solution}
::: pf

::: pf-step

$\boxed{\text{No}}$: if $B = \emptyset$, then $A \times B$ is finite for every $A$, including infinite $A$.

::: pf-proof

::: pf-step

Suppose $B = \emptyset$.

:::

::: pf-step

By definition of the Cartesian product, $A \times \emptyset = \emptyset$.

:::

::: pf-step

The empty set $\emptyset$ has cardinality $0$, which is finite.

:::

::: pf-step

However, $A$ can be chosen to be an arbitrary infinite set (for example, $A = \NN$).

:::

::: pf-step

Thus $A \times B$ is finite while $A$ is infinite.

:::

:::

:::

::: pf-step

If both $A$ and $B$ are nonempty, then $A$ and $B$ are finite.

::: pf-proof

::: pf-step

Since $B \neq \emptyset$, fix an element $b_0 \in B$.

:::

::: pf-step

Define the inclusion map $\iota: A \to A \times B$ by $\iota(a) = (a, b_0)$.

:::

::: pf-step

The map $\iota$ is injective: if $\iota(a_1) = \iota(a_2)$, then $(a_1, b_0) = (a_2, b_0)$, so $a_1 = a_2$.

:::

::: pf-step

Since $A \times B$ is finite and $\iota(A) \subseteq A \times B$, the image $\iota(A)$ is finite.

:::

::: pf-step

Since $\iota: A \to \iota(A)$ is a bijection, $A$ is finite.

:::

::: pf-step

Symmetrically, fixing $a_0 \in A$ and considering $b \mapsto (a_0, b)$ shows that $B$ is finite.

:::

:::

:::

:::

:::

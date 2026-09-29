---
schema: qual/card@1
id: P-ZQBPZ
kind: problem
title: Closed sets covering a connected space with connected intersection are connected
classification:
  areas:
  - topology
  topics:
  - Point-Set Topology
  - Closure
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Let $X$ be a connected space and $A,B\subseteq X$ closed subsets with $X=A\cup B$ and $A\cap B$ connected.
Show that $A$ and $B$ are connected.

![](../../assets/Workshops/Topology/_attachments/Pasted%20image%2020210520145810.png)
:::

::: {.solution}
**Goal.** For connected $X = A \cup B$ with $A, B$ closed and $A \cap B$ connected, show $A$ and $B$ are connected.

::: pf

::: pf-step
Suppose $A$ is disconnected.

::: pf-proof
assume for contradiction.
:::

:::

::: pf-step
Then $A = C \cup D$ with $C, D$ nonempty, disjoint, and closed in $A$ (hence closed in $X$, since $A$ is closed).

::: pf-proof
a disconnected space is a union of two nonempty disjoint closed subsets.
:::

:::

::: pf-step
$A \cap B$ is connected, so it lies entirely in $C$ or entirely in $D$.

::: pf-proof
$A \cap B = (C \cap B) \cup (D \cap B)$ is a union of two disjoint closed sets; since $A \cap B$ is connected, one of them is empty, so $A \cap B \subseteq C$ or $A \cap B \subseteq D$.
:::

:::

::: pf-step
WLOG $A \cap B \subseteq C$.

::: pf-proof
relabel if necessary.
:::

:::

::: pf-step
Then $X = (C \cup B) \cup D$ is a union of two disjoint nonempty closed sets.

::: pf-proof

::: pf-step
$C \cup B$ and $D$ are disjoint.

::: pf-proof
$C \cap D = \emptyset$ and $B \cap D = \emptyset$ (since $A \cap B \subseteq C$ and $D \subseteq A$).
:::

:::

::: pf-step
$C \cup B$ and $D$ are closed.

::: pf-proof
$C, D$ are closed in $X$, and $B$ is closed, so $C \cup B$ is closed.
:::

:::

::: pf-step
Both are nonempty.

::: pf-proof
$C \neq \emptyset$ and $D \neq \emptyset$.
:::

:::

::: pf-step
$X = (C \cup B) \cup D$.

::: pf-proof
$X = A \cup B = (C \cup D) \cup B = (C \cup B) \cup D$.
:::

:::

:::

:::

::: pf-step
This contradicts $X$ being connected.

::: pf-proof
$X$ is a union of two disjoint nonempty closed sets.
:::

:::

::: {.pf-step #s7}
Hence $A$ is connected; by symmetry, $B$ is connected.

::: pf-proof
the same argument with $A$ and $B$ swapped.
:::

:::

::: pf-qed
step [](#s7){.pf-ref} is the claim.
:::

:::

:::

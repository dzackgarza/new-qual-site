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
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: "The statement was followed by a screenshot of the same source text, which opens with the locator '(May 2016)'; the screenshot is removed from the statement."
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Let $X$ be a connected space and $A,B\subseteq X$ closed subsets with $X=A\cup B$ and $A\cap B$ connected.
Show that $A$ and $B$ are connected.
:::

::: {.solution}
By the symmetry of the hypotheses in $A$ and $B$, it suffices to show that $A$ is connected.

::: pf

::: {.pf-step #split}
If $A$ is disconnected, then $A = C \cup D$ with $C, D$ nonempty, disjoint, closed in $X$, and $A \cap B \subseteq C$.

::: pf-proof
A separation of $A$ consists of nonempty disjoint sets $C, D$ closed in $A$, hence closed in $X$ because $A$ is closed.
The connected set $A \cap B$ is the union of the disjoint relatively closed sets $C \cap B$ and $D \cap B$, so one of them is empty; relabel so that $D \cap B = \emptyset$.
:::

:::

::: pf-step
$A$ is connected.

::: pf-proof
Otherwise take $C$ and $D$ as in step [](#split){.pf-ref}.
Then $X = A \cup B = (C \cup B) \cup D$, where $C \cup B$ and $D$ are nonempty, closed, and disjoint because $C \cap D = \emptyset$ and $B \cap D = \emptyset$.
This separates the connected space $X$, a contradiction.
:::

:::

:::

:::

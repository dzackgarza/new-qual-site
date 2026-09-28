---
schema: qual/card@1
id: E-MFCCS
kind: problem
title: A pairwise disjoint family of intervals with nonempty interior in $\RR$ is
  countable
classification:
  areas:
  - real-analysis
  topics:
  - Countability
  - Euclidean Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.exercise}
- Show that any disjoint intervals is countable.
:::

::: {.solution}
<1>1. A family $\mathcal I$ of pairwise disjoint intervals in $\RR$, each with nonempty interior, is at most countable.

<2>1. Each $I \in \mathcal I$ contains a rational number $q_I$.

::: {.proof}
$I$ contains a nonempty open interval, and $\QQ$ is dense in $\RR$.
:::

<2>2. The map $I \mapsto q_I$ is injective.

::: {.proof}
If $I \neq J$, then $I \cap J = \emptyset$, so $q_I \neq q_J$.
:::

<2>3. Q.E.D.

::: {.proof}
Steps <2>1 and <2>2 give an injection of $\mathcal I$ into the countable set $\QQ$.
:::

<1>2. The family of singletons $\theset{\theset{x} : x \in \RR}$ is an uncountable family of pairwise disjoint degenerate intervals $[x,x]$.

::: {.proof}
Distinct singletons are disjoint, and $\RR$ is uncountable.
:::

<1>3. Q.E.D.

::: {.proof}
Step <1>1 is the statement for intervals with nonempty interior, in particular for open intervals; step <1>2 shows that it fails for degenerate intervals.
:::
:::

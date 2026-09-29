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

::: pf

::: {.pf-step #s1}

A family $\mathcal I$ of pairwise disjoint intervals in $\RR$, each with nonempty interior, is at most countable.

::: pf-proof

::: {.pf-step #s1-1}

Each $I \in \mathcal I$ contains a rational number $q_I$.

::: pf-proof

$I$ contains a nonempty open interval, and $\QQ$ is dense in $\RR$.

:::

:::

::: {.pf-step #s1-2}

The map $I \mapsto q_I$ is injective.

::: pf-proof

If $I \neq J$, then $I \cap J = \emptyset$, so $q_I \neq q_J$.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} give an injection of $\mathcal I$ into the countable set $\QQ$.

:::

:::

:::

::: {.pf-step #s2}

The family of singletons $\theset{\theset{x} : x \in \RR}$ is an uncountable family of pairwise disjoint degenerate intervals $[x,x]$.

::: pf-proof

Distinct singletons are disjoint, and $\RR$ is uncountable.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} is the statement for intervals with nonempty interior, in particular for open intervals; step [](#s2){.pf-ref} shows that it fails for degenerate intervals.

:::

:::

:::

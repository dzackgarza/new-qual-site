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
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: The source reads "Show that any disjoint intervals is countable."; a family of disjoint singletons is uncountable, so the statement requires intervals with nonempty interior, as the title does.
---

::: {.exercise}
Show that any family of pairwise disjoint intervals in $\RR$, each with nonempty interior, is countable.
:::

::: {.solution}
Let $\mathcal I$ be such a family.

::: pf

::: {.pf-step #rational}

Each $I \in \mathcal I$ contains a rational number $q_I$.

::: pf-proof

$I$ contains a nonempty open interval, and $\QQ$ is dense in $\RR$.

:::

:::

::: pf-step

The map $\mathcal I \to \QQ$, $I \mapsto q_I$, is injective, so $\mathcal I$ is at most countable.

::: pf-proof

The map is defined by step [](#rational){.pf-ref}. If $I \neq J$, then $I \cap J = \emptyset$, so $q_I \neq q_J$. The set $\QQ$ is countable.

:::

:::

:::

:::

::: {.remark}
The hypothesis of nonempty interior is needed: the singletons $\theset{x} = [x,x]$, $x \in \RR$, form an uncountable family of pairwise disjoint degenerate intervals.
:::

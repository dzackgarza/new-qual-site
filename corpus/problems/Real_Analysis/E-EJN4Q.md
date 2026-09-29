---
schema: qual/card@1
id: E-EJN4Q
kind: problem
title: Open subsets of $\mathbb{R}$ are countable unions of disjoint open intervals
classification:
  areas:
  - real-analysis
  topics:
  - Euclidean Spaces
  - Measure Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.exercise}
- Show that every open $U \subseteq \RR$ is a countable union of disjoint open intervals.
:::

::: {.solution}
Let $U \subseteq \RR$ be open.

::: pf

::: {.pf-step #s1}

Each connected component $C$ of $U$ is an open interval $(a,b)$ with $-\infty \leq a < b \leq \infty$.

::: pf-proof

Components of an open subset of a locally connected space are open, so $C$ is open in $\RR$. A nonempty connected subset of $\RR$ is an interval, and an open interval of $\RR$ has the form $(a,b)$ with $a,b \in [-\infty, \infty]$.

:::

:::

::: {.pf-step #s2}

Distinct components are disjoint, and $U$ is their union.

::: pf-proof

The components are the equivalence classes of the relation $x \sim y$ if and only if $x$ and $y$ lie in a common connected subset of $U$, and equivalence classes partition $U$.

:::

:::

::: {.pf-step #s3}

There are at most countably many components.

::: pf-proof

Each component is a nonempty open interval, so it contains a rational number; choose one, $q_C$, for each component $C$. By step [](#s2){.pf-ref} distinct components are disjoint, so $C \mapsto q_C$ is injective into the countable set $\QQ$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} express $U$ as a disjoint union of open intervals, and step [](#s3){.pf-ref} shows the family is countable.

:::

:::

:::

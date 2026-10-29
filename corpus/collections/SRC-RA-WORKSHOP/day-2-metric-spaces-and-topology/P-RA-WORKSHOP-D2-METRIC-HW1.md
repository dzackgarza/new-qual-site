---
schema: qual/card@1
id: P-RA-WORKSHOP-D2-METRIC-HW1
kind: problem
title: 'Compactness via open covers'
classification:
  areas:
  - real-analysis
  topics:
  - Compactness
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
Throughout, $X$ is a metric space.
State the definition of what it means for a set $K\subset X$ to be compact, including the definition of open cover.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

An **open cover** of $K$ is a family $(U_\alpha)_{\alpha\in A}$ of open subsets of $X$ such that $K\subseteq\bigcup_{\alpha\in A}U_\alpha$.

::: pf-proof

This is the definition of an open cover of a subset of a metric space.

:::

:::

::: {.pf-step #s2}

A **finite subcover** of $(U_\alpha)_{\alpha\in A}$ is a restriction to a finite subset $F\subseteq A$ satisfying $K\subseteq\bigcup_{\alpha\in F}U_\alpha$.

::: pf-proof

The restricted family consists of finitely many members of the original cover and still covers $K$, which is precisely the definition of a finite subcover.

:::

:::

::: {.pf-step #s3}

The set $K$ is **compact** if every open cover of $K$ admits a finite subcover.

::: pf-proof

This is the open-cover definition of compactness, using the terms defined in steps [](#s1){.pf-ref} and [](#s2){.pf-ref}.

:::

:::

:::

:::

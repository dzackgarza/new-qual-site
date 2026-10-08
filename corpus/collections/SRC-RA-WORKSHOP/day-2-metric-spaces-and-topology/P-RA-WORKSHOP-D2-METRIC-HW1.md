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
<1>1. An **open cover** of $K$ is a family $(U_\alpha)_{\alpha\in A}$ of open subsets of $X$ such that $K\subseteq\bigcup_{\alpha\in A}U_\alpha$.

::: {.proof}
This is the definition of an open cover of a subset of a metric space.
:::

<1>2. A **finite subcover** of $(U_\alpha)_{\alpha\in A}$ is a restriction to a finite subset $F\subseteq A$ satisfying $K\subseteq\bigcup_{\alpha\in F}U_\alpha$.

::: {.proof}
The restricted family consists of finitely many members of the original cover and still covers $K$, which is precisely the definition of a finite subcover.
:::

<1>3. The set $K$ is **compact** if every open cover of $K$ admits a finite subcover.

::: {.proof}
This is the open-cover definition of compactness, using the terms defined in steps <1>1 and <1>2.
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>1–<1>3 give the requested definitions.
:::
:::

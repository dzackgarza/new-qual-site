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

<1>1. Each connected component $C$ of $U$ is an open interval $(a,b)$ with $-\infty \leq a < b \leq \infty$.

::: {.proof}
Components of an open subset of a locally connected space are open, so $C$ is open in $\RR$. A nonempty connected subset of $\RR$ is an interval, and an open interval of $\RR$ has the form $(a,b)$ with $a,b \in [-\infty, \infty]$.
:::

<1>2. Distinct components are disjoint, and $U$ is their union.

::: {.proof}
The components are the equivalence classes of the relation $x \sim y$ if and only if $x$ and $y$ lie in a common connected subset of $U$, and equivalence classes partition $U$.
:::

<1>3. There are at most countably many components.

::: {.proof}
Each component is a nonempty open interval, so it contains a rational number; choose one, $q_C$, for each component $C$. By step <1>2 distinct components are disjoint, so $C \mapsto q_C$ is injective into the countable set $\QQ$.
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>1 and <1>2 express $U$ as a disjoint union of open intervals, and step <1>3 shows the family is countable.
:::
:::

---
schema: qual/card@1
id: E-FFARP
kind: problem
title: Every compact set in a metric space is closed and bounded
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
  date: 2026-08-17
---

::: {.exercise}
- Show that every compact set is closed and bounded.
:::

::: {.solution}
Let $(X,d)$ be a metric space and $K \subseteq X$ compact. If $K = \emptyset$ both claims hold, so assume $K \neq \emptyset$.

::: pf

::: {.pf-step #s1}

$K$ is bounded.

::: pf-proof

Fix $x_0 \in X$. The open balls $B(x_0, n)$, $n \geq 1$, cover $X$, hence $K$. Compactness gives a finite subcover $B(x_0, n_1), \ldots, B(x_0, n_j)$; with $N = \max_i n_i$, $K \subseteq B(x_0, N)$.

:::

:::

::: {.pf-step #s2}

$K$ is closed.

::: pf-proof

::: {.pf-step #s2-1}

Fix $x \in X \setminus K$. For each $y \in K$, the balls $U_y = B(y, d(x,y)/3)$ and $V_y = B(x, d(x,y)/3)$ are disjoint open neighborhoods of $y$ and $x$.

::: pf-proof

$d(x,y) > 0$ because $y \in K$ and $x \notin K$. A point $z$ in both balls would give $d(x,y) \leq d(x,z) + d(z,y) < 2d(x,y)/3$.

:::

:::

::: {.pf-step #s2-2}

There are $y_1, \ldots, y_m \in K$ with $K \subseteq \bigcup_{i=1}^m U_{y_i}$.

::: pf-proof

The sets $U_y$, $y \in K$, form an open cover of the compact set $K$.

:::

:::

::: {.pf-step #s2-3}

$V \coloneqq \bigcap_{i=1}^m V_{y_i}$ is an open neighborhood of $x$ disjoint from $K$.

::: pf-proof

$V$ is a finite intersection of open sets containing $x$. If $z \in V \cap K$, then by step [](#s2-2){.pf-ref} $z \in U_{y_i}$ for some $i$, while $z \in V \subseteq V_{y_i}$, contradicting $U_{y_i} \cap V_{y_i} = \emptyset$ from step [](#s2-1){.pf-ref}.

:::

:::

::: pf-qed

By step [](#s2-3){.pf-ref} every point of $X \setminus K$ has an open neighborhood in $X \setminus K$, so $X \setminus K$ is open.

:::

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves boundedness and step [](#s2){.pf-ref} proves closedness.

:::

:::

:::

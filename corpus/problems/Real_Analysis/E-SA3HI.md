---
schema: qual/card@1
id: E-SA3HI
kind: problem
title: Disjoint compact and closed sets have positive distance
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
- Show that if $K$ is compact and $F$ is closed with $K, F$ disjoint then $\dist(K, F) > 0$.
:::

::: {.solution}
Work in a metric space $(X,d)$ with $K$ and $F$ nonempty; if either is empty, $\dist(K,F) = \infty$.

<1>1. The function $x \mapsto \dist(x, F)$ is $1$-Lipschitz, hence continuous.

::: {.proof}
For $z \in F$, $\dist(x,F) \leq d(x,z) \leq d(x,y) + d(y,z)$. Taking the infimum over $z$ gives $\dist(x,F) \leq d(x,y) + \dist(y,F)$, and the same holds with $x$ and $y$ exchanged.
:::

<1>2. There is $k_0 \in K$ with $\dist(k_0, F) = \dist(K, F)$.

::: {.proof}
$\dist(K,F) = \inf_{k \in K}\dist(k,F)$, and a continuous function on a nonempty compact set attains its infimum; step <1>1 gives continuity.
:::

<1>3. $\dist(k_0, F) > 0$.

::: {.proof}
If $\dist(k_0, F) = 0$, then $k_0$ is a limit of points of $F$; since $F$ is closed, $k_0 \in F$, contradicting $K \cap F = \emptyset$.
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>2 and <1>3.
:::
:::

::: {.remark}
Compactness of $K$ cannot be weakened to closedness. In $\RR$, $K = \NN$ and $F = \theset{n + 2^{-n} : n \in \NN}$ are closed and disjoint, and $\dist(K, F) = \inf_n 2^{-n} = 0$.
:::

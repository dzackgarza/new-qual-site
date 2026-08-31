---
schema: qual/card@1
id: P-O2PWG
kind: problem
title: Compact sets are closed and bounded, complete totally bounded sets are compact,
  and $\dist(K,F)>0$
classification:
  areas:
  - real-analysis
  topics:
  - Compactness
  - Metric Spaces
  - Completeness
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: problem
- Show that every compact set is closed and bounded.

- Show that if a subset of a metric space is complete and totally bounded, then it is compact.

- Show that if $K$ is compact and $F$ is closed with $K, F$ disjoint then $\dist(K, F) > 0$.
:::
::: {.solution}
<1>1. Every compact set $K$ in a metric space is closed and bounded.
<2>1. $K$ is closed: given $x \notin K$, for each $y \in K$ choose disjoint open $U_y \ni y$, $V_y \ni x$; $\{U_y\}_{y \in K}$ is an open cover with a finite subcover $U_{y_1}, \ldots, U_{y_n}$; then $V = \bigcap_i V_{y_i}$ is an open neighborhood of $x$ disjoint from $K$.
::: {.proof}
Hausdorff separation + finite subcover.
:::
<2>2. $K$ is bounded: fix $x_0$; $\{B(x_0, n)\}_{n \in \NN}$ is an open cover with a finite subcover, so $K \subseteq B(x_0, N)$ for some $N$.
::: {.proof}
finite subcover of the nested balls.
:::

<1>2. If $E$ is complete and totally bounded, then $E$ is compact.
<2>1. Every sequence in $E$ has a Cauchy subsequence.
::: {.proof}
total boundedness gives a finite $2^{-k}$-net for each $k$; a diagonal argument picks a subsequence that is $2^{-k}$-close eventually for each $k$, i.e. Cauchy.
:::
<2>2. Every Cauchy sequence in $E$ converges in $E$.
::: {.proof}
completeness.
:::
<2>3. Q.E.D.
::: {.proof}
<2>1 and <2>2 give sequential compactness, equivalent to compactness in metric spaces.
:::
(A subset of a complete space is compact iff closed and totally bounded.)

<1>3. If $K$ compact and $F$ closed with $K \cap F = \varnothing$, then $\dist(K, F) > 0$.
<2>1. $x \mapsto \dist(x, F)$ is continuous: $|\dist(x, F) - \dist(y, F)| \le d(x, y)$.
::: {.proof}
triangle inequality.
:::
<2>2. $\dist(\cdot, F) > 0$ on $K$ (since $K \cap F = \varnothing$ and $F$ closed: if $\dist(x, F) = 0$ then $x \in \overline F = F$).
::: {.proof}
$\dist(x, F) = 0$ iff $x \in \overline F$.
:::
<2>3. $\dist(\cdot, F)$ attains its minimum on the compact set $K$; the minimum is $> 0$.
::: {.proof}
continuous function on a compact set attains its extrema (<2>1); the value is $> 0$ by <2>2.
:::

<1>4. Q.E.D.
::: {.proof}
<1>1, <1>2, <1>3 establish the three claims.
:::
:::

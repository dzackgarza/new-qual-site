---
schema: qual/card@1
id: E-FFARP
kind: exercise
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

::: exercise
- Show that every compact set is closed and bounded.
:::

::: {.solution}
**Goal:** Show that every compact subset $K$ of a metric space (in particular of $\RR^n$) is closed and bounded.

<1>1. $K$ is bounded.
Proof: fix $x_0 \in X$; the family $\theset{B(x_0, n)}_{n=1}^{\infty}$ of open balls is an open cover of $X$, hence of $K$.
Compactness yields a finite subcover $\theset{B(x_0, n_j)}$; with $N = \max n_j$, $K \subseteq B(x_0, N)$, so $K$ is bounded.
<1>2. $K$ is closed.
<2>1. Let $x \notin K$; it suffices to find an open neighborhood of $x$ disjoint from $K$.
Proof: then $X \setminus K$ is open and $K$ is closed.
<2>2. For each $y \in K$, choose disjoint open neighborhoods $U_y \ni y$, $V_y \ni x$ (e.g. balls of radius $d(x,y)/3$). Proof: $y \neq x$ since $y \in K$, $x \notin K$, and metric spaces are Hausdorff.
<2>3. $\theset{U_y}_{y \in K}$ covers $K$; by compactness pick $y_1, \ldots, y_m$ with $K \subseteq \bigcup_{i=1}^m U_{y_i}$.
Proof: compactness.
<2>4. $V := \bigcap_{i=1}^m V_{y_i}$ is an open neighborhood of $x$ disjoint from $K$.
Proof: $V$ is a finite intersection of open sets, hence open, and contains $x$ since each $V_{y_i} \ni x$.
If $z \in V \cap K$, then $z \in U_{y_i}$ for some $i$ (as $K \subseteq \bigcup U_{y_i}$) while $z \in V \subseteq V_{y_i}$, contradicting $U_{y_i} \cap V_{y_i} = \emptyset$.
<1>3. Q.E.D. Proof: <1>1 proves boundedness and <1>2 proves closedness.
:::

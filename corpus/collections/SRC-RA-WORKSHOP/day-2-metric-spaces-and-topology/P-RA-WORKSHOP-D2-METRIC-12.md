---
schema: qual/card@1
id: P-RA-WORKSHOP-D2-METRIC-12
kind: problem
title: Open subsets of $\mathbb R$ are finite or countable unions of disjoint open intervals
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
  date: 2026-08-25
---

::: {.problem}
Prove Proposition 1.4: Every open set $G\subset\mathbb R$ can be written as a finite or countable union of disjoint open intervals $(a_j,b_j)$ with at most one $a_j=-\infty$ and at most one $b_j=\infty$.
:::

:::: {.solution}
<1>1. Components of $G$ are open intervals.
Proof: for $x \in G$, let $C_x$ be the connected component of $x$ in $G$.
Since $G$ is open, $C_x$ is open (the components of an open set in $\mathbb{R}$ are open: if $y \in C_x$, then $(y-\delta, y+\delta) \subseteq G$ for some $\delta$, and $(y-\delta,y+\delta)\cup C_x$ is connected, so it equals $C_x$). Being a connected subset of $\mathbb{R}$, $C_x$ is an interval; an open interval $(a_x, b_x)$ with $a_x, b_x \in [-\infty,\infty]$.
Distinct components are disjoint, and $G = \bigcup_{x\in G} C_x$.
<1>2. The collection of components is countable.
Proof: each component $(a_x, b_x)$ is a nonempty open interval, so it contains a rational $q$.
Distinct components are disjoint, hence contain distinct rationals; choosing one rational per component gives an injection from the set of components into $\mathbb{Q}$, which is countable.
<1>3. Endpoint conditions.
Proof: at most one component has $a_j = -\infty$: two distinct components are disjoint, and two intervals $(a_1, b_1)$, $(a_2, b_2)$ both unbounded below would both contain $(\min(a_1,a_2), \min(b_1,b_2))$ — they would intersect.
Similarly, at most one component has $b_j = +\infty$.
<1>4. Q.E.D.
:::

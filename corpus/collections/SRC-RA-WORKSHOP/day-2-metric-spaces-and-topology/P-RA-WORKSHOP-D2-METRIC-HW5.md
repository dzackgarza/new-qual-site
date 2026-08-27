---
schema: qual/card@1
id: P-RA-WORKSHOP-D2-METRIC-HW5
kind: problem
title: Classify two sets as open, closed, or compact in their metric spaces (warm-up)
classification:
  areas:
  - real-analysis
  topics:
  - Compactness
  - Function Spaces
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
(January 2010 #1a partial) Determine whether or not the sets $$\{(x,y)\in\mathbb R^2:x+y<3\}$$ and $$\{f\in C([-1,1]):f(0)=0\}$$ are open, closed, or compact, where $C([-1,1])$ is considered with $\lVert\cdot\rVert_\infty$.
:::

:::: {.solution}
<1>1. $A_1 = \{(x,y) \in \mathbb{R}^2 : x + y < 3\}$ is open, not closed, not compact.
<2>1. Open: the map $(x,y) \mapsto x+y$ is continuous and $A_1 = (x+y)^{-1}((-\infty, 3))$ is the preimage of the open set $(-\infty,3)$.
<2>2. Not closed: the sequence $(3 - 1/n, 0) \in A_1$ converges to $(3,0) \notin A_1$.
<2>3. Not compact: $A_1$ is unbounded (e.g. $\{(-m, 0) : m \ge 1\} \subseteq A_1$), and compact subsets of $\mathbb{R}^2$ are bounded.
<1>2. $A_2 = \{f \in C([-1,1]) : f(0) = 0\}$ is closed, not open, not compact.
<2>1. Closed: the evaluation map $E: C([-1,1]) \to \mathbb{R}$, $E(f) = f(0)$, is continuous (indeed $|E(f)| \le \lVert f\rVert_\infty$), and $A_2 = E^{-1}(\{0\})$ is the preimage of the closed set $\{0\}$.
<2>2. Not open: the zero function $0 \in A_2$, but every ball $B_\epsilon(0)$ contains the constant function $g \equiv \epsilon/2$, for which $g(0) = \epsilon/2 \ne 0$, so $g \notin A_2$; no ball around $0$ is contained in $A_2$.
<2>3. Not compact: $A_2$ is unbounded — the functions $f_m(x) = mx$ satisfy $f_m(0) = 0$ and $\lVert f_m\rVert_\infty = m \to \infty$.
<1>3. Q.E.D.
:::

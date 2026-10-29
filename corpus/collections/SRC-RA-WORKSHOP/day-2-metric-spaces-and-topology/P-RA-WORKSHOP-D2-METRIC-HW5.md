---
schema: qual/card@1
id: P-RA-WORKSHOP-D2-METRIC-HW5
kind: problem
title: Open, closed, and compact status of two metric-space subsets
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
(January 2010 #1a partial) Determine whether or not the sets $$\{(x,y)\in\RR^2:x+y<3\}$$ and $$\{f\in C([-1,1]):f(0)=0\}$$ are open, closed, or compact, where $C([-1,1])$ is considered with $\norm{\cdot}_\infty$.
:::

::: {.solution}
Write $A_1=\{(x,y)\in\RR^2:x+y<3\}$ and $A_2=\{f\in C([-1,1]):f(0)=0\}$.

::: pf

::: {.pf-step #s1}

The set $A_1$ is open, neither closed nor compact.

::: pf-proof

The continuous map $s:\RR^2\to\RR$ defined by $s(x,y)=x+y$ satisfies $A_1=s^{-1}(( -\infty,3))$, so $A_1$ is open. The sequence $(3-1/n,0)$ belongs to $A_1$ and converges to $(3,0)\notin A_1$, so $A_1$ is not closed. Finally, $(-m,0)\in A_1$ for every positive integer $m$, so $A_1$ is unbounded. Every compact metric space is bounded, hence $A_1$ is not compact.

:::

:::

::: {.pf-step #s2}

The set $A_2$ is closed, neither open nor compact in the supremum norm.

::: pf-proof

Evaluation $E:C([-1,1])\to\RR$, $E(f)=f(0)$, is continuous because $\abs{E(f)-E(g)}\leq\norm{f-g}_\infty$. Thus $A_2=E^{-1}(\{0\})$ is closed. For every $\varepsilon>0$ the constant function $g\equiv\varepsilon/2$ belongs to $B_\varepsilon(0)$ but not to $A_2$, so $A_2$ is not open. The functions $f_m(t)=mt$ belong to $A_2$ and satisfy $\norm{f_m}_\infty=m$. Consequently $A_2$ is unbounded and therefore not compact.

:::

:::

::: pf-qed

By steps [](#s1){.pf-ref} and [](#s2){.pf-ref}, $\boxed{A_1 \text{ is open, not closed, not compact; } A_2 \text{ is closed, not open, not compact.}}$

:::

:::

:::

---
schema: qual/card@1
id: P-PRACT20-W6-12
kind: problem
title: The discrete metric on $\RR$
classification:
  areas:
  - prelim
  topics:
  - Metric Spaces
  - Discrete Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the arrow lost from choice (D) and separated the choices, checked against Week6_solns.pdf (Problem 12).
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the arrow lost from the identity map in the solution, checked against Week6_solns.pdf (Problem 12).
---

::: {.problem}
Let $d(x, y) = \begin{cases} 0, & x = y, \\ 1, & x \neq y. \end{cases}$ Which of the following hold in the metric space $(\RR, d)$?

(A) $\{x\}$ is open for each $x \in \RR$.

(B) Every subset of $\RR$ is closed.

(C) If $d'$ is the ordinary metric on $\RR$, then the identity map $(\RR, d) \to (\RR, d')$ is continuous.

(D) If $d'$ is the ordinary metric on $\RR$, then the identity map $(\RR, d') \to (\RR, d)$ is continuous.
:::

::: {.solution}
(A), (B) and (C) hold; (D) does not.

$d$ is the discrete metric: the ball of radius $1/2$ about $x$ is $\{x\}$, so every singleton is open and $d$ generates the discrete topology on $\RR$. Every set is open, so every set is also closed. Thus (A) and (B) hold.

For (C) and (D), let $X$ carry two topologies $\tau_1,\tau_2$. The identity $\iota\colon(X,\tau_1)\to(X,\tau_2)$ is continuous iff $\iota^{-1}(V)=V\in\tau_1$ for every $V\in\tau_2$, that is, iff $\tau_2\subseteq\tau_1$. The discrete topology contains every topology on $\RR$, so (C) holds. The standard topology does not contain the open set $\{0\}$ of the discrete topology, so (D) fails.
:::

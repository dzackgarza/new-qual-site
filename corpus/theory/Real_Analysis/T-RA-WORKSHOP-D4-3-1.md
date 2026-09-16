---
schema: qual/card@1
id: T-RA-WORKSHOP-D4-3-1
kind: theorem
title: Equivalent characterizations of continuity
classification:
  areas:
  - real-analysis
  topics:
  - Continuity
  - Euclidean Spaces
relations: []
review: draft
---

::: {.theorem}
Let $E\subseteq\RR^n$ and let $f\colon E\to\RR^m$.
The following are equivalent:

1. $f$ is [[D-AEAAD|continuous]] on $E$, with the subspace topology on $E$.

2. For every $x\in E$ and every $\varepsilon>0$ there exists $\delta>0$ such that $\norm{f(y)-f(x)}<\varepsilon$ for all $y\in E$ with $\norm{x-y}<\delta$.

3. For every sequence $(x_n)_{n\geq1}$ in $E$ converging to a point $x\in E$, $\lim_{n\to\infty}f(x_n)=f(x)$.

4. For every open set $G\subseteq\RR^m$, the set $f\inv(G)$ is open in $E$ with the subspace topology.
[@Rud76].
:::

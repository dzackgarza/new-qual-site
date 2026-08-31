---
schema: qual/card@1
id: FR-GG457
kind: proof
title: 'Proposition: a.e. convergence implies convergence in measure (finite measure)'
classification:
  areas:
  - real-analysis
  topics:
  - Egorov
  - Convergence of Functions
  - Measure Theory
relations: []
review: draft
---

::: {.proof}
Let $E \subseteq \RR^d$ be measurable with $\mu(E) < \infty$, and suppose $f_k \to f$ almost everywhere on $E$.
Fix $\eps > 0$ and $\delta > 0$.
For each $N$, define
\[
E_N \da \ts{x \in E \st \abs{f_k(x) - f(x)} < \eps \text{ for all } k \ge N}.
\]
The sets $E_N$ are increasing, and since $f_k(x) \to f(x)$ for almost every $x$, we have $\bigcup_N E_N = E$ up to a null set.
Hence $\mu(E \sm E_N) \to 0$ as $N \to \infty$ (continuity of measure from below on the increasing union).
Choose $N$ with $\mu(E \sm E_N) < \delta$.
Then for every $k \ge N$ and every $x \in E_N$ we have $\abs{f_k(x) - f(x)} < \eps$, so
\[
\mu\ts{x \in E \st \abs{f_k(x) - f(x)} \ge \eps} \le \mu(E \sm E_N) < \delta
\]
for all $k \ge N$.
This is exactly the definition of $f_k \to f$ in measure.
:::

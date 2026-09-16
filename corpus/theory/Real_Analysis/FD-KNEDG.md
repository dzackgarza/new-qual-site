---
schema: qual/card@1
id: FD-KNEDG
kind: definition
title: Basic properties of Lebesgue outer measure
prompts:
- What four properties does outer measure have?
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
---

::: {.definition}
Let $m_*$ be the [[D-3XE77|outer measure]] on $\RR^n$.

1. Monotonicity. If $E_1\subseteq E_2\subseteq\RR^n$, then $m_*(E_1)\leq m_*(E_2)$.

2. Countable subadditivity. If $E=\bigcup_{j=1}^\infty E_j$ with $E_j\subseteq\RR^n$, then $m_*(E)\leq\sum_{j=1}^\infty m_*(E_j)$.

3. Approximation from above by open sets. For every $E\subseteq\RR^n$, $m_*(E)=\inf\theset{m_*(O)\suchthat O\supseteq E \text{ open}}$.

4. Additivity for almost disjoint cubes. If $E=\bigcup_{j=1}^\infty Q_j$ is a countable union of closed cubes that are pairwise [[FD-5T3HX|almost disjoint]], then $m_*(E)=\sum_{j=1}^\infty\abs{Q_j}$.
:::

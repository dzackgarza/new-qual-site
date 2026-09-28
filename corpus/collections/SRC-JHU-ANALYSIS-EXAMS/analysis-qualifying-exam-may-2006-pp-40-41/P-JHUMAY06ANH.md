---
schema: qual/card@1
id: P-JHUMAY06ANH
kind: problem
title: '$L^1\cap L^2\subseteq L^p$ for $1\le p\le2$'
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually compared May 2006 problem 8 on PDF page 41; the interval is arbitrary and need not have finite measure."
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Preserved the valid pointwise splitting proof and repaired the second proof's Holder exponents so the two resulting integrals are genuinely the L1 and squared L2 norms."
---

::: {.problem}
Prove that any function $f \in L^1(I) \cap L^2(I)$ on an interval $I \subset \mathbb{R}$ must belong to $L^p(I)$ for all $p \in [1, 2]$.
:::

::: {.solution}
Fix $p\in[1,2]$ and let $E_1=\{x\in I:\abs{f(x)}\le1\}$ and $E_2=\{x\in I:\abs{f(x)}>1\}$.

<1>1. $\abs f^p\le\abs f$ on $E_1$ and $\abs f^p\le\abs f^2$ on $E_2$.

::: {.proof}
For $0\le t\le1$ and $p\ge1$, $t^p\le t$; for $t>1$ and $p\le2$, $t^p\le t^2$.
:::

<1>2. Q.E.D.

::: {.proof}
By step <1>1, $\int_I\abs f^p\le\int_{E_1}\abs f+\int_{E_2}\abs f^2\le\norm f_{L^1(I)}+\norm f_{L^2(I)}^2<\infty$, so $f\in L^p(I)$.
:::
:::

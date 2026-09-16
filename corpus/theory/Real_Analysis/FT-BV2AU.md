---
schema: qual/card@1
id: FT-BV2AU
kind: theorem
title: Small tails and absolute continuity of the integral
prompts:
- What do small tails and absolute continuity say about $f \in L^1$?
classification:
  areas:
  - real-analysis
  topics:
  - Small Tails
  - Continuity of Measure
  - L¹
relations: []
review: draft
---

::: {.theorem}
Let $m$ be Lebesgue measure on $\RR^n$, let $f\in L^1(\RR^n)$, let $\varepsilon> 0$, and for $N\geq1$ let $B_N\subseteq\RR^n$ be the open ball of radius $N$ centered at $0$.

1. **Small tails.** There exists $N$ such that $\int_{B_N^c} \abs{f} < \varepsilon$.

2. **Absolute continuity.** There exists $\delta>0$ such that every [[D-MDJII|Lebesgue measurable]] $E\subseteq\RR^n$ with $m(E) < \delta$ satisfies $\int_E \abs{f} < \varepsilon$.
:::

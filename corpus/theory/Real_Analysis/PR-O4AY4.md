---
schema: qual/card@1
id: PR-O4AY4
kind: proposition
title: Absolute continuity of the integral of an $L^1$ function
classification:
  areas:
  - real-analysis
  topics:
  - Continuity of Measure
  - L¹
relations:
- kind: variant-of
  target: PR-4OXGZ
review: draft
---

::: {.proposition}
Let $m$ be Lebesgue measure on $\RR^n$ and let $f\in L^1(\RR^n)$.
For every $\varepsilon>0$ there exists $\delta>0$ such that every [[D-MDJII|Lebesgue measurable]] set $E\subseteq\RR^n$ with $m(E)<\delta$ satisfies
$$
\abs{\int_E f}\leq\int_E \abs{f} < \varepsilon .
$$
:::

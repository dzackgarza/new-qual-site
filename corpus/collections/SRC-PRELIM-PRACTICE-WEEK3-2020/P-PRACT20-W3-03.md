---
schema: qual/card@1
id: P-PRACT20-W3-03
kind: problem
title: The integral $\int_0^\infty\lfloor x\rfloor e^{-x}\,dx$
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Removed OCR junk from the integrand, checked against Week3_solns.pdf page 1 (Problem 3).
---

::: {.problem}
Compute $\int_0^\infty \lfloor x \rfloor e^{-x}\,dx$ where $\lfloor x \rfloor$ denotes the largest integer smaller than $x$.
:::

::: {.solution}
Split the integral into intervals $[ n , n + 1 )$ for $n \in  { \mathbb { N } } _ { 0 }$ and use $\lfloor x \rfloor = n \colon$

$$
\begin{array} { r c l } { \displaystyle \int _ { 0 } ^ { \infty } \lfloor x \rfloor e ^ { - x } d x = \displaystyle \sum _ { n = 1 } ^ { \infty } n \int _ { n } ^ { n + 1 } e ^ { - x } d x } \\ { \displaystyle } & { = \displaystyle \sum _ { n = 1 } ^ { \infty } n ( e ^ { - n } - e ^ { - ( n + 1 ) } ) } \\ { \displaystyle } & { = \displaystyle \sum _ { n = 1 } ^ { \infty } n e ^ { - n } - \sum _ { n = 1 } ^ { \infty } n e ^ { - ( n + 1 ) } } \\ { \displaystyle } & { = \displaystyle \sum _ { n = 1 } ^ { \infty } n e ^ { - n } - \sum _ { n = 2 } ^ { \infty } ( n - 1 ) e ^ { - n } = \sum _ { n = 1 } ^ { \infty } e ^ { - n } . } \end{array}
$$

Now this is a geometric series resulting in $\int _ { 0 } ^ { \infty } \lfloor x \rfloor e ^ { - x } d x = { \frac { e ^ { - 1 } } { 1 - e ^ { - 1 } } } = { \frac { 1 } { e - 1 } } .$
:::

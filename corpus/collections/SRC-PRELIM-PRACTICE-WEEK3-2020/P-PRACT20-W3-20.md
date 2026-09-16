---
schema: qual/card@1
id: P-PRACT20-W3-20
kind: problem
title: Minimizing $x+4z$ on the sphere $x^2+y^2+z^2=2$
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
  note: Replaced OCR 'sec' with the source's 'so' in the solution, checked against Week3_solns.pdf (Problem 20).
---

::: {.problem}
Minimize the function $f ( x , y , z ) = x + 4 z$ on the curve $x ^ { 2 } + y ^ { 2 } + z ^ { 2 } = 2$
:::

::: {.solution}
The minimum must satisfy

$$
1 = 2 \lambda x , ~ 0 = 2 \lambda y , ~ 4 = 2 \lambda z .
$$

Plugging these into the constrant gives $\scriptstyle { \frac { 1 } { 4 \lambda ^ { 2 } } } + { \frac { 4 } { \lambda ^ { 2 } } } = 2$ so $\lambda ^ { 2 } = 1 7 / 8$ . Since f is increasing in both x and z, we take the negative roots and find that f is minimized along the curve at $( - \sqrt { 2 / 1 7 } , 0 , - \sqrt { 3 2 / 1 7 } )$
:::

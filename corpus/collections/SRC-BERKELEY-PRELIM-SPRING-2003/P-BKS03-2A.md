---
schema: qual/card@1
id: P-BKS03-2A
kind: problem
title: Directional derivatives without differentiability at the origin
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Define $f:\mathbb R^2\to\mathbb R$ by $f(x,0)=0$ and, for $y\ne0$,
\[
f(x,y)=\left(1-\cos\frac{x^2}{y}\right)\sqrt{x^2+y^2}.
\]

(a) Show that $f$ is continuous at $(0,0)$.

(b) Calculate all directional derivatives at $(0,0)$.

(c) Show that $f$ is not differentiable at $(0,0)$.
:::

::: {.solution}
(a) We have $| f ( x , y ) | \leq 2 { \sqrt { x ^ { 2 } + y ^ { 2 } } }$ , and the latter tends to 0 as $( x , y ) \to ( 0 , 0 )$

(b) In the direction of $( x , y )$ with $y \ne 0$ , the directional derivative is

$$
\operatorname* { l i m } _ { t \to 0 } { \frac { f ( t x , t y ) } { t } } = \operatorname* { l i m } _ { t \to 0 } \left( 1 - \cos { \frac { t ^ { 2 } x ^ { 2 } } { t y } } \right) { \sqrt { x ^ { 2 } + y ^ { 2 } } } = 0 ,
$$

and the limit is trivially zero in the direction of $( x , 0 )$ for any x.

(c) If f were differentiable, the derivative would be zero, and then $f ( x , y ) / \sqrt { x ^ { 2 } + y ^ { 2 } } \to 0$ as $( x , y ) \to ( 0 , 0 )$ . This is false, since if we approach (0, 0) along the curve $x ^ { 2 } / y = \pi$ , the limit of $f ( x , y ) / \sqrt { x ^ { 2 } + y ^ { 2 } } \mathrm { ~ i s ~ } 1 - \cos \pi = 2$
:::

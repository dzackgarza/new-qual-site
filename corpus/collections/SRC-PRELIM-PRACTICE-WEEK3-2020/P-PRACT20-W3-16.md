---
schema: qual/card@1
id: P-PRACT20-W3-16
kind: problem
title: Recovering $f(x,y)$ from its partial derivatives $2x+y$ and $x+2y$
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.problem}
Find all functions f (x, y) satisfying ${ \frac { \partial f } { \partial x } } ( x , y ) = 2 x + y , \quad { \frac { \partial f } { \partial y } } ( x , y ) = x + 2 y .$
:::

::: {.solution}
Integrating the first equality in x, we find $f ( x , y ) = x ^ { 2 } + x y + g ( y )$ for some function g. Differentiating in y shows that $g ^ { \prime } ( y ) = 2 y$ and so $g ( y ) = y ^ { 2 } + C$ and thus $f ( x , y ) = x ^ { 2 } + x y + y ^ { 2 } + C$ where C is a constant.
:::

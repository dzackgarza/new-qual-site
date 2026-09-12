---
schema: qual/card@1
id: P-BKF09-6A
kind: problem
title: Berkeley Fall 2009 prelim problem 6A
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
For $n \geq 1$, prove that$a _ { n } + \frac { 1 } { a _ { n - 1 } + \displaystyle \frac { 1 } { \dots + \displaystyle \frac { 1 } { a _ { 1 } + \displaystyle \frac { 1 } { a _ { 0 } } } } } = \frac { \Delta _ { n } } { \Delta _ { n - 1 } } ,$
:::

::: {.solution}
Using the cofactor expansion with respect to the last row, we find that $\Delta _ { n } =$ $a _ { n } \Delta _ { n - 1 } + \Delta _ { n - 2 }$. Dividing by$\Delta _ { n - 1 }$, we get:$$\Delta _ { n } / \Delta _ { n - 1 } = a _ { n } + \frac { 1 } { \Delta _ { n - 1 } / \Delta _ { n - 2 } } .$$The required result follows by induction on n since it obviously holds for$n = 1$
:::

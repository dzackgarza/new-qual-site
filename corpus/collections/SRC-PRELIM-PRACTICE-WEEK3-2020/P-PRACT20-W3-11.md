---
schema: qual/card@1
id: P-PRACT20-W3-11
kind: problem
title: "Week 3: Calculus II (Part 2) & Calculus III, problem 11"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.problem}
Find $a _ { 0 } , a _ { 1 } , a _ { 2 } , a _ { 3 }$ such that $x ^ { 3 } - x + 1 = a _ { 0 } + a _ { 1 } ( x - 2 ) + a _ { 2 } ( x - 2 ) ^ { 2 } + a _ { 3 } ( x - 2 ) ^ { 3 }$
:::

::: {.solution}
We can view this as the Taylor series for the polynomial centered at $x = 2$ . Plugging in $x = 2$ gives $a _ { 0 } = 7$ . Taking a derivative and then plugging in $x = 2$ gives $a _ { 1 } = 1 1$ . Taking two derivatives and plugging in $x = 2$ gives $a _ { 2 } = 6$ . Finally taking three derivatives shows $a _ { 3 } = 1$ (or you can simply notice that $a _ { 3 }$ it is the coefficient of $x ^ { 3 } )$ .
:::

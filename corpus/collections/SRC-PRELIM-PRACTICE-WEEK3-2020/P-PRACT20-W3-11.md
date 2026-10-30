---
schema: qual/card@1
id: P-PRACT20-W3-11
kind: problem
title: Expanding $x^3-x+1$ in powers of $x-2$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Find $a_{0}, a_{1}, a_{2}, a_{3}$ such that $x^{3} - x + 1 = a_{0} + a_{1}(x - 2) + a_{2}(x - 2)^{2} + a_{3}(x - 2)^{3}$.
:::

::: {.solution}
We can view this as the Taylor series for the polynomial centered at $x = 2$ . Plugging in $x = 2$ gives $a _ { 0 } = 7$ . Taking a derivative and then plugging in $x = 2$ gives $a _ { 1 } = 1 1$ . Taking two derivatives and plugging in $x = 2$ gives $a _ { 2 } = 6$ . Finally taking three derivatives shows $a_3 = 1$, which is also the coefficient of $x^3$.
:::

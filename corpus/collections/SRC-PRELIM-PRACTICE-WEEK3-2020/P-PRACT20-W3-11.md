---
schema: qual/card@1
id: P-PRACT20-W3-11
kind: problem
title: Expanding $x^3-x+1$ in powers of $x-2$
classification:
  areas:
  - prelim
  topics:
  - Taylor Series
  - Polynomials
relations: []
review: draft
---

::: {.problem}
Find $a_{0}, a_{1}, a_{2}, a_{3}$ such that $x^{3} - x + 1 = a_{0} + a_{1}(x - 2) + a_{2}(x - 2)^{2} + a_{3}(x - 2)^{3}$.
:::

::: {.solution}
The right side is the Taylor expansion of $f(x)=x^3-x+1$ about $x=2$, so $a_k=f^{(k)}(2)/k!$. Then $a_0=f(2)=7$, $a_1=f'(2)=3\cdot4-1=11$, and $a_2=f''(2)/2=6\cdot2/2=6$. Finally taking three derivatives shows $a_3 = 1$, which is also the coefficient of $x^3$.
:::

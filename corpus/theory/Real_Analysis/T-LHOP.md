---
schema: qual/card@1
id: T-LHOP
kind: theorem
title: L'Hopital's rule
slogan: 'a $0/0$ or $\infty/\infty$ quotient passes to the quotient of derivatives'
classification:
  areas:
  - real-analysis
  topics:
  - Limits
  - Differentiation
relations: []
review: draft
---

::: {.theorem}
Let $-\infty\leq a<b\leq+\infty$ and let $f,g\colon(a,b)\to\RR$ be differentiable, with $g'(x)\neq0$ for all $x\in(a,b)$.
Suppose that $f'(x)/g'(x)\to A$ as $x\to a$, where $A\in\RR\union\theset{\pm\infty}$, and suppose that either $f(x)\to0$ and $g(x)\to0$ as $x\to a$, or $g(x)\to+\infty$ as $x\to a$.
Then $f(x)/g(x)\to A$ as $x\to a$.

The same conclusion holds for $x\to b$, and with $g(x)\to-\infty$ in place of $g(x)\to+\infty$.

This is [@Rud76, Theorem 5.13].
:::

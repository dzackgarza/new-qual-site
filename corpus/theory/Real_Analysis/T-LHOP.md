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
Let $-\infty\leq a<b\leq\infty$ and let $f,g\colon(a,b)\to\RR$ be differentiable, with $g'(x)\neq0$ for all $x\in(a,b)$.
Suppose that $f(x)\to0$ and $g(x)\to0$ as $x\to a$, and that $f'(x)/g'(x)\to A$ as $x\to a$, where $A\in\RR\union\theset{\pm\infty}$.
Then $f(x)/g(x)\to A$ as $x\to a$.

The same conclusion holds when $\abs{f(x)}\to\infty$ and $\abs{g(x)}\to\infty$ in place of the two limits to $0$, and at $x\to b$ in place of $x\to a$.
:::

---
schema: qual/card@1
id: P-T5VN8
kind: problem
title: $f(x)/x$ is increasing when $f'$ is increasing and $f(0)=0$
classification:
  areas:
  - complex-analysis
  topics:
  - Calculus
relations: []
review: draft
---

::: {.problem}
Let $f:[0,\infty)\to\RR$ be continuous, differentiable on
$(0,\infty)$, satisfy $f(0)=0$, and suppose $f'$ is increasing. For
$x>0$ define $g(x)=f(x)/x$. Prove that $g$ is increasing.
:::

::: {.solution}
Let $0<x<y$. By the mean value theorem
there are $\xi\in(0,x)$ and $\eta\in(x,y)$ such that
\[
\frac{f(x)-f(0)}x=f'(\xi),
\qquad
\frac{f(y)-f(x)}{y-x}=f'(\eta).
\]
Since $f'$ is increasing, the second slope is at least the first. Using
$f(0)=0$,
\[
f(y)\ge f(x)+(y-x)\frac{f(x)}x
=y\frac{f(x)}x,
\]
so $f(y)/y\ge f(x)/x$.
:::
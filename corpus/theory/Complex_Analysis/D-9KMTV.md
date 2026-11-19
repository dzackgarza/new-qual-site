---
schema: qual/card@1
id: D-9KMTV
kind: definition
title: Branch point
prompts:
- What is a branch point of a holomorphic function?
classification:
  areas:
  - complex-analysis
  topics:
  - Branch Points
  - Complex Logarithm
relations: []
review: draft
---

::: {.definition}
Let $\Omega\subseteq\CC$ be a domain and let $f$ be [[D-E7A5W|holomorphic]] on $\Omega$.
A point $a\in\bd\Omega$ is a \dfn{branch point} of $f$ if no holomorphic function on a punctured disc $\DD_r^*(a)$ agrees with $f$ on $\Omega\cap\DD_r^*(a)$.
:::

::: {.remark}
The branch point is the point at which every cut ends: $f$ continues holomorphically across each of its other boundary points, and around $a$ the continuation changes value.
The principal branch of the logarithm on $\CC\sm(-\infty,0]$ has a branch point at $0$ and at none of the points of $(-\infty,0)$, and the branch of $\sqrt z$ on $\CC\sm[0,\infty)$ with argument in $(0,\pi)$ has a branch point at $0$; the square root of $z(z-1)$ on a domain cut along $[0,1]$ has branch points at $0$ and at $1$.
:::

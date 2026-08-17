---
schema: qual/card@1
id: P-VDKZF
kind: problem
title: An entire function omitting a bounded open set is constant
classification:
  areas:
  - complex-analysis
  topics:
  - liouville-s-theorem
  - entire-functions
  - removable-singularities
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Let $f(z)$ be entire and assume values of $f(z)$ lie outside a *bounded* open set $\Omega$.
Show without using Picard's theorems that $f(z)$ is a constant.
:::

::: {.solution}
We have $\abs{f(z)}\geq M$ for some $M$, so $\abs{1/f(z)} \leq M\inv$ is bounded, and we claim it is entire as well.
This follows from the fact that $1/f$ has singularities at the zeros of $f$, but these are removable since $1/f$ is bounded in every neighborhood of each such zero.
So $1/f$ extends to a holomorphic function.
But now $1/f =c$ is constant by Liouville, which forces $f= 1/c$ to be constant.
:::

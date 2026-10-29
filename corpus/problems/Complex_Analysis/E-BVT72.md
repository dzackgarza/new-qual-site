---
schema: qual/card@1
id: E-BVT72
kind: problem
title: A nonzero analytic function on the disk with infinitely many zeros
classification:
  areas:
  - complex-analysis
  topics:
  - Zeros
  - Identity Theorem
  - Counterexamples
relations: []
review: draft
audit:
- event: statement-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: Part (1) of the source reads "which has infinitely zeros"; the statement supplies "many".
---

::: {.problem}
(1) Explicitly write down an example of a non-zero analytic function in $\abs{z}<1$ which has infinitely many zeros in $\abs{z}<1$.

(2) Why does not the phenomenon in (1) contradict the uniqueness theorem?
:::

::: {.solution}

::: pf

::: {.pf-step #example}
(1) $\boxed{f(z)=\sin\qty(\frac{1}{1-z})}$ is a nonzero holomorphic function on $\DD$ whose zeros in $\DD$ include $z_n=1-\frac{1}{n\pi}$ for all integers $n\ge1$.

::: pf-proof
The function $z\mapsto(1-z)^{-1}$ is holomorphic on $\DD$, since its only pole is the boundary point $z=1$, so $f$ is holomorphic on $\DD$; it is not identically zero because $f(0)=\sin1\neq0$.
Each $z_n$ lies in $(0,1)\subset\DD$, and $f(z_n)=\sin(n\pi)=0$.
:::

:::

::: pf-step
(2) The zero set of $f$ has no accumulation point in $\DD$, so the uniqueness theorem does not apply.

::: pf-proof
The uniqueness theorem forces a holomorphic function on a connected open set to vanish identically only when its zero set has an accumulation point inside that set.
The zeros of $f$ are the points $1-\frac{1}{n\pi}$, $n\in\ZZ\setminus\theset0$, that lie in $\DD$; these accumulate only at $1\notin\DD$.
:::

:::

:::

:::

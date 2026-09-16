---
schema: qual/card@1
id: P-F12FN
kind: problem
title: Pointwise and uniform convergence of $nx/(n+x)$ on $[0,\infty)$
classification:
  areas:
  - prelim
  topics:
  - Uniform Convergence
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $f_n(x) = \frac{nx}{n+x}$ for $x \in [0, \infty)$ and $n \in \mathbb{N}$.

(a) Find a function $f$ such that $\{f_n\}$ converges to $f$ pointwise on $[0, \infty)$.

(b) Is the convergence uniform on $[0, \infty)$?
Justify your answer.
:::

::: {.solution}
For fixed $x\ge0$,
\[
f_n(x)=\frac{nx}{n+x}=\frac{x}{1+x/n}\longrightarrow x.
\]
Thus the pointwise limit is
\[
f(x)=x.
\]

The convergence is not uniform on $[0,\infty)$. Indeed,
\[
|f_n(x)-f(x)|
=\left|\frac{nx}{n+x}-x\right|
=\frac{x^2}{n+x}.
\]
Taking $x=n$ gives
\[
|f_n(n)-f(n)|=\frac{n}{2},
\]
which does not tend to $0$. Therefore
\[
\sup_{x\ge0}|f_n(x)-f(x)|\not\to0,
\]
so convergence is not uniform.
:::

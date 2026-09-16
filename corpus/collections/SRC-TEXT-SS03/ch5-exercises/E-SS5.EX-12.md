---
schema: qual/card@1
id: E-SS5.EX-12
kind: problem
title: "Entire functions with no vanishing derivative are exponentials"
classification:
  areas:
  - complex-analysis
  topics: ['Entire Functions', 'Hadamard Factorization', "Jensen's Formula"]
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
12. Suppose f is entire and never vanishes, and that none of the higher derivatives of $f$ ever vanish.
    Prove that if $f$ is also of finite order, then $f ( z ) = e ^ { a z + b }$ for some constants a and b.
:::

::: {.solution}
Because $f$ is entire, of finite order, and never vanishes, Hadamard's factorization theorem gives
\[
f(z)=e^{P(z)}
\]
for some polynomial $P$.

Differentiating,
\[
f'(z)=P'(z)e^{P(z)}.
\]
By hypothesis $f'$ never vanishes, and $e^{P(z)}$ never vanishes, so $P'$ has no zeros. If $\deg P\ge2$, then $P'$ is a nonconstant polynomial and therefore has a complex zero by the fundamental theorem of algebra, a contradiction. Hence $\deg P\le1$.

Thus
\[
P(z)=az+b
\]
for constants $a,b\in\mathbb C$, and
\[
\boxed{f(z)=e^{az+b}}.
\]
Under the stated hypothesis that no positive-order derivative ever vanishes, necessarily $a\ne0$; indeed, if $a=0$, then $f'\equiv0$.
:::

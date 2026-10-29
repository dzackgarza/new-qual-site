---
schema: qual/card@1
id: P-ACDEH
kind: problem
title: Entire functions of quadratic growth are polynomials of degree at most $2$
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Polynomials
  - Liouville's Theorem
  - Cauchy Estimates
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
- event: source-corrected
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source reads "f(z) <= M |z|^2", comparing a complex value with a real one; the statement bounds |f(z)|.
---

::: {.problem}
Let $f(z)$ be entire and assume that $\abs{f(z)} \leq M \abs{z}^2$ outside some disk for some constant $M$.
Show that $f(z)$ is a polynomial in $z$ of degree $\leq 2$.
:::

::: {.solution}
Let $\abs{f(z)}\le M\abs z^2$ for $\abs z\ge R_0$, and write $f(z) = \sum_{n\ge0} a_n z^n$, the Taylor series of $f$ at $0$, which converges on $\CC$.

::: pf

::: {.pf-step #coefficient-bound}
For $n \ge 0$ and $R \geq R_0$, $\abs{a_n} \leq M R^{2-n}$.

::: pf-proof
Cauchy's estimate on $\abs z=R$ gives $\abs{a_n}\le R^{-n}\max_{\abs z=R}\abs{f(z)}$, and the hypothesis bounds the maximum by $MR^2$.
:::

:::

::: pf-step
$f(z) = a_0 + a_1 z + a_2 z^2$, a polynomial of degree at most $2$.

::: pf-proof
For $n\ge3$, $R^{2-n}\to0$ as $R\to\infty$, so step [](#coefficient-bound){.pf-ref} gives $a_n=0$.
:::

:::

:::

:::

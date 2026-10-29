---
schema: qual/card@1
id: E-GPFKM
kind: problem
title: Bound on $\abs{f(2i)}$ for $f:\HH\to\DD$ with $f(i)=0$
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
audit:
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source reads "Suppose f:H -> C with |f(z)| < 1 and f(i) = 0" and does not say that f is holomorphic; the statement adds that hypothesis, without which no bound exists.
---

::: {.exercise}
Suppose $f:\HH\to \CC$ is holomorphic with $\abs{f(z)}< 1$ and $f(i) = 0$.
Find an upper bound for $\abs{f(2i)}$.
:::

::: {.solution}
Let $g(z) \coloneqq i{1+z\over 1-z}$, a conformal map $\DD\to \HH$ with $g(0)=i$ and inverse $g^{-1}(w)={w-i\over w+i}$.

::: pf

::: {.pf-step #schwarz}
$F\coloneqq f\circ g$ satisfies $\abs{F(z)}\le\abs z$ on $\DD$.

::: pf-proof
$F$ is holomorphic $\DD\to\DD$ with $F(0)=f(i)=0$, so the Schwarz lemma applies.
:::

:::

::: pf-step
$\abs{f(2i)}\le\boxed{1/3}$.

::: pf-proof
Since $g^{-1}(2i)={i\over3i}={1\over3}$, step [](#schwarz){.pf-ref} gives $\abs{f(2i)}=\abs{F(1/3)}\le1/3$.
:::

:::

:::

:::

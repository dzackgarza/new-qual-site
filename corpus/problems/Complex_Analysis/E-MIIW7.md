---
schema: qual/card@1
id: E-MIIW7
kind: problem
title: Schwarz lemma for a map $\DD_R(a)\to\DD_M(0)$
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
relations: []
review: draft
audit:
- event: statement-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source prints "If f:D_R(a)->D_M(0) with f(a)=0, then |f(z)| <= (M/R)|z-a|." without saying f is holomorphic; the statement asks to show the bound for holomorphic f.
---

::: {.exercise}
Show that if $f: \DD_R(a)\to\DD_M(0)$ is holomorphic with $f(a) = 0$, then
$$
\abs{f(z)}\leq {M\over R}\abs{z-a}
.$$

:::

::: {.solution}
::: pf

::: {.pf-step #rescaled}
$g(z)\coloneqq\frac{f(Rz+a)}{M}$ is a holomorphic map $\DD\to\DD$ with $g(0)=0$, so $\abs{g(z)}\le\abs z$.

::: pf-proof
$z\mapsto Rz+a$ maps $\DD$ onto $\DD_R(a)$, $\abs f<M$, and $g(0)=f(a)/M=0$; apply the Schwarz lemma.
:::

:::

::: pf-step
$\abs{f(w)}\le\frac MR\abs{w-a}$ for $w\in\DD_R(a)$.

::: pf-proof
Put $z=\frac{w-a}R\in\DD$ in step [](#rescaled){.pf-ref}: $\frac{\abs{f(w)}}M\le\frac{\abs{w-a}}R$.
:::

:::

:::

:::

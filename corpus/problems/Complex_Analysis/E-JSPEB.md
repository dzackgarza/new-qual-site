---
schema: qual/card@1
id: E-JSPEB
kind: problem
title: Bound on $\abs{f(\frac{1+i}{2})}$ for a self-map of $\DD$ with $\abs{f}\le\abs{e^z}$ on
  $\abs z=1$
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
relations: []
review: draft
audit:
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source prints "Suppose f:D->D with f(0)=0 and |f(z)|<=|e^z| when |z|=1. Find an upper bound for f((1+i)/2)." The statement makes f holomorphic on D and continuous on the closed disk, so that the boundary condition makes sense, and asks for a bound on the modulus. The earlier solution gave sqrt(2e)/2, which exceeds the bound sqrt(2)/2 from the Schwarz lemma; the solution now gives both.
---

::: {.exercise}
Suppose $f: \DD\to \DD$ is holomorphic, extends continuously to $\overline\DD$, and satisfies $f(0) = 0$ and $\abs{f(z)} \leq \abs{e^z}$ when $\abs{z} = 1$.
Find an upper bound for $\abs{f\qty{1+i\over 2}}$.

:::

::: {.solution}
Write $z_0\coloneqq\frac{1+i}2$, so $\abs{z_0}=\frac{\sqrt2}2$ and $\Re z_0=\frac12$.

::: pf

::: pf-step
$\abs{f(z)}\le\abs z e^{\Re z}$ on $\DD$.

::: pf-proof
Set $g(z)\coloneqq f(z)e^{-z}$, holomorphic on $\DD$, continuous on $\overline\DD$, with $g(0)=0$. On $\abs z=1$, $\abs{g(z)}\le1$, so $\abs g\le1$ on $\DD$ by the maximum modulus principle; $g$ is not a unimodular constant since $g(0)=0$, so $g(\DD)\subseteq\DD$. The Schwarz lemma gives $\abs{g(z)}\le\abs z$, that is, $\abs{f(z)}\le\abs z\abs{e^z}=\abs ze^{\Re z}$.
:::

:::

::: pf-step
$\abs{f(z)}\le\abs z$ on $\DD$.

::: pf-proof
This is the Schwarz lemma for $f:\DD\to\DD$ with $f(0)=0$.
:::

:::

::: pf-step
$\abs{f(z_0)}\le\boxed{\frac{\sqrt2}2}$.

::: pf-proof
At $z_0$ the two bounds are $\frac{\sqrt2}2e^{1/2}=\frac{\sqrt{2e}}2$ and $\frac{\sqrt2}2$; the second is smaller.
:::

:::

:::

:::

::: {.remark}
The bound $\abs{f(z_0)}\le\frac{\sqrt{2e}}2$ uses only $f(0)=0$ and the boundary condition, and so also holds for a holomorphic $f:\DD\to\CC$ with these properties.
:::

---
schema: qual/card@1
id: E-LLEBI
kind: problem
title: $\frac{|f(0)|-|z|}{1+|f(0)||z|}\le|f(z)|\le\frac{|f(0)|+|z|}{1-|f(0)||z|}$
  for holomorphic $f:\DD\to\DD$
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Blaschke Factors
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-19
---

::: {.problem}
Let $f$ be a non-constant analytic function on $\DD$ with $f(\DD) \subseteq \DD$.
Use $\psi_{a} (f(z))$ (where $a=f(0)$, $\displaystyle \psi_a(z) = \frac{a - z}{1 - \bar{a}z}$) to prove that $\displaystyle \frac{\abs{f(0)} - \abs{z}}{1 + \abs{f(0)}\abs{z}} \leq \abs{f(z)} \leq \frac{\abs{f(0)} + \abs{z}}{1 - \abs{f(0)}\abs{z}}$.
:::

::: {.solution}
Fix $z\in\DD$ and write $a\coloneqq f(0)\in\DD$ and $g\coloneqq\psi_a\circ f$.

::: pf

::: {.pf-step #schwarz}
$\abs{g(z)}\le\abs z$.

::: pf-proof
For $\abs a<1$, $\psi_a$ is an automorphism of $\DD$ with $\psi_a(a)=0$. So $g:\DD\to\DD$ is holomorphic with $g(0)=0$, and the Schwarz lemma applies.
:::

:::

::: {.pf-step #inverse}
$f(z)=\dfrac{a-w}{1-\bar aw}$ with $w\coloneqq g(z)$ and $\abs w\le\abs z$.

::: pf-proof
$\psi_a\circ\psi_a=\operatorname{id}$, so $f=\psi_a\circ g$; the bound on $w$ is step [](#schwarz){.pf-ref}.
:::

:::

::: pf-step
$\abs{f(z)}\le\dfrac{\abs a+\abs z}{1-\abs a\abs z}$.

::: pf-proof
By step [](#inverse){.pf-ref}, $\abs{a-w}\le\abs a+\abs z$ and $\abs{1-\bar aw}\ge1-\abs a\abs w\ge1-\abs a\abs z>0$.
:::

:::

::: pf-step
$\abs{f(z)}\ge\dfrac{\abs a-\abs z}{1+\abs a\abs z}$.

::: pf-proof
If $\abs z\ge\abs a$ the right side is at most $0$. If $\abs z<\abs a$, step [](#inverse){.pf-ref} gives $\abs{a-w}\ge\abs a-\abs w\ge\abs a-\abs z>0$ and $\abs{1-\bar aw}\le1+\abs a\abs z$.
:::

:::

:::

:::

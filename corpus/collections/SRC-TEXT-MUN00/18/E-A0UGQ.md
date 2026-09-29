---
schema: qual/card@1
id: E-A0UGQ
kind: problem
title: A function continuous at exactly one point
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Find a function $f: \mathbb{R} \to \mathbb{R}$ that is continuous at precisely one point.
:::

::: {.solution}
Define $f\colon\mathbb R\to\mathbb R$ by $f(x)=x$ for $x\in\mathbb Q$ and $f(x)=0$ for $x\notin\mathbb Q$.

::: pf

::: {.pf-step #continuous-at-zero}
$f$ is continuous at $0$.

::: pf-proof
For every $x$, $\abs{f(x)-f(0)}=\abs{f(x)}\le\abs x$.
Given $\varepsilon>0$, take $\delta=\varepsilon$: if $\abs x<\delta$, then $\abs{f(x)-f(0)}<\varepsilon$.
:::

:::

::: {.pf-step #discontinuous-elsewhere}
$f$ is not continuous at any $x_0\ne0$.

::: pf-proof
If $x_0\in\mathbb Q$, choose irrationals $y_n\to x_0$; then $f(y_n)=0\not\to x_0=f(x_0)$.
If $x_0\notin\mathbb Q$, choose rationals $q_n\to x_0$; then $f(q_n)=q_n\to x_0\ne0=f(x_0)$.
In both cases a sequence converging to $x_0$ has images not converging to $f(x_0)$.
:::

:::

::: pf-qed
By steps [](#continuous-at-zero){.pf-ref} and [](#discontinuous-elsewhere){.pf-ref}, $f$ is continuous at $0$ and at no other point.
:::

:::

:::

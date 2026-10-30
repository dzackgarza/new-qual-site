---
schema: qual/card@1
id: P-CASP08A
kind: problem
title: "Statement and proof of Schwarz's Lemma"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
State and prove **Schwarz's Lemma** for holomorphic functions on the unit disk.
:::

::: {.solution}
Let $f:\DD\to\DD$ be holomorphic with $f(0)=0$. Schwarz's lemma states
$$
\abs{f(z)}\le \abs{z},\qquad \abs{f'(0)}\le1.
$$
Moreover, equality at one nonzero point, or $\abs{f'(0)}=1$, holds if and only if $f(z)=e^{i\theta}z$ for some $\theta\in\RR$.

::: pf

::: pf-step

Since $f(0)=0$,
$$
g(z)=\begin{cases}f(z)/z,&z\ne0,\\ f'(0),&z=0\end{cases}
$$
is holomorphic on $\DD$.

:::

::: pf-step

Fix $0<r<1$. On $\abs{z}=r$, $\abs{g(z)}\le1/r$. By the maximum-modulus principle, $\abs{g(z)}\le1/r$ for $\abs{z}\le r$. For fixed $z$, let $r\uparrow1$ through values larger than $\abs{z}$; then $\abs{g(z)}\le1$. Hence $\abs{f(z)}\le\abs{z}$ and $\abs{f'(0)}\le1$.

:::

::: pf-step

If $\abs{f(z_0)}=\abs{z_0}$ for some $z_0\ne0$, then $\abs{g(z_0)}=1$. If $\abs{f'(0)}=1$, then $\abs{g(0)}=1$. In either case $g$ attains its maximum modulus at an interior point, so $g$ is constant. Its constant value has modulus $1$, hence $g=e^{i\theta}$ and $f(z)=e^{i\theta}z$. Conversely every rotation has equality.

:::

:::

:::
